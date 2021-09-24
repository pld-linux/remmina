#
# note: disabling plugins will still build them if deps are met
#
# Conditional build:
%bcond_without	exec		# do not build exec plugin
%bcond_without	rdp		# do not build rdp plugin
%bcond_without	secret		# do not build secret plugin
%bcond_without	spice		# do not build spice plugin
%bcond_without	vnc		# do not build vnc plugin
%bcond_without	vte		# do not build vte plugin
%bcond_without	www		# do not build www plugin
#
Summary:	Remote Desktop Client
Name:		remmina
Version:	1.4.20
Release:	2
License:	GPLv2+ and MIT
Group:		X11/Applications
Source0:	https://gitlab.com/Remmina/Remmina/-/archive/v%{version}/Remmina-v%{version}.tar.bz2
# Source0-md5:	8fa0f57d2ebb2f35d11bab99345a8acf
# Cmake helper file to easy build plugins outside remmina source tree
# See http://www.muflone.com/remmina-plugin-rdesktop/english/install.html which
# use http://www.muflone.com/remmina-plugin-builder/ with remmina bundled source.
# So we can't use it directly only as instructions.
Source1:	pluginBuild-CMakeLists.txt
Patch0:		fix-shebangs.patch
URL:		http://remmina.org
BuildRequires:	appstream-glib
BuildRequires:	avahi-ui-gtk3-devel >= 0.6.30
BuildRequires:	cmake >= 2.8
BuildRequires:	cups-devel
BuildRequires:	desktop-file-utils
%{?with_rdp:BuildRequires:	freerdp2-devel >= 2.0.0-0.20190320}
BuildRequires:	gettext
BuildRequires:	gtk+3-devel
%{?with_www:BuildRequires:      gtk-webkit4-devel}
BuildRequires:	intltool
BuildRequires:	json-glib-devel
BuildRequires:	libappindicator-gtk3-devel
BuildRequires:	libgcrypt-devel
%{?with_secret:BuildRequires:	libsecret-devel}
BuildRequires:	libsodium-devel
BuildRequires:	libsoup-devel
%{?with_vnc:BuildRequires:	libvncserver-devel}
BuildRequires:	pcre2-8-devel
BuildRequires:	rpmbuild(macros) >= 1.742
%{?with_spice:BuildRequires:	spice-gtk-devel}
%{?with_vte:BuildRequires:	vte-devel}
BuildRequires:	xorg-lib-libxkbfile-devel
Requires(post,postun):	gtk-update-icon-cache
Requires:	avahi-ui-gtk3 >= 0.6.30
Requires:	hicolor-icon-theme
Obsoletes:	remmina-plugins-nx < 1.4.20
Obsoletes:	remmina-plugins-xdmcp < 1.4.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travelers, who need to work with
lots of remote computers in front of either large monitors or tiny
net-books.

Remmina supports multiple network protocols in an integrated and
consistent user interface. Currently RDP, VNC, XDMCP and SSH are
supported.

Please don't forget to install the plugins for the protocols you want
to use.

%package        devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description    devel
The %{name}-devel package contains header files for developing plugins
for %{name}.

%package        plugins-exec
Summary:	External execution plugin for Remmina Remote Desktop Client
Requires:	%{name} = %{version}-%{release}

%description    plugins-exec
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travelers, who need to work with
lots of remote computers in front of either large monitors or tiny
net-books.

This package contains the plugin to execute external processes
(commands or applications) from the Remmina window.

%package        plugins-rdp
Summary:	RDP plugin for Remmina Remote Desktop Client
Requires:	%{name} = %{version}-%{release}
Requires:	freerdp2-libs >= 2.0.0-0.20190320

%description    plugins-rdp
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travelers, who need to work with
lots of remote computers in front of either large monitors or tiny
net-books.

This package contains the Remote Desktop Protocol (RDP) plugin for the
Remmina remote desktop client.

%package        plugins-secret
Summary:	Keyring integration for Remmina Remote Desktop Client
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-plugins-gnome%{?_isa} = %{version}-%{release}
Obsoletes:	remmina-plugins-gnome < %{version}-%{release}

%description    plugins-secret
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travelers, who need to work with
lots of remote computers in front of either large monitors or tiny
net-books.

This package contains the plugin with keyring support for the Remmina
remote desktop client.

%package        plugins-spice
Summary:	SPICE plugin for Remmina Remote Desktop Client
Requires:	%{name} = %{version}-%{release}

%description    plugins-spice
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travelers, who need to work with
lots of remote computers in front of either large monitors or tiny
net-books.

This package contains the SPICE plugin for the Remmina remote desktop
client.

%package        plugins-vnc
Summary:	VNC plugin for Remmina Remote Desktop Client
Requires:	%{name} = %{version}-%{release}

%description    plugins-vnc
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travelers, who need to work with
lots of remote computers in front of either large monitors or tiny
net-books.

This package contains the VNC plugin for the Remmina remote desktop
client.

%package        plugins-www
Summary:	Browser plugin for Remmina Remote Desktop Client
Requires:	%{name} = %{version}-%{release}

%description    plugins-www
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travelers, who need to work with
lots of remote computers in front of either large monitors or tiny
net-books.

This package contains the www plugin for the Remmina remote desktop
client.

%prep
%setup -qn Remmina-v%{version}
%{__sed} -i s/^pt_PT$// po/LINGUAS
%{__rm} -f po/pt_PT.po
%patch0 -p1

%build
mkdir -p build

%cmake --build=build \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DWITH_APPINDICATOR=ON \
	-DWITH_AVAHI=ON \
	-DWITH_CUPS=ON \
	-DWITH_GCRYPT=ON \
	-DWITH_GETTEXT=ON \
	-DWITH_LIBSECRET=ON \
	%{cmake_on_off vnc WITH_LIBVNCSERVER} \
	%{cmake_on_off spice WITH_SPICE} \
	%{cmake_on_off vte WITH_VTE} \
	.

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/cmake/%{name}/
cp -pr cmake/*.cmake $RPM_BUILD_ROOT%{_libdir}/cmake/%{name}/
cp -pr config.h.in $RPM_BUILD_ROOT%{_includedir}/%{name}/
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/%{name}/

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ber,br,ckb,eo,ie,ka,hi,shn}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc LICENSE AUTHORS ChangeLog README.md
%attr(755,root,root) %{_bindir}/remmina-file-wrapper
%attr(755,root,root) %{_bindir}/remmina
%{_datadir}/metainfo/*.appdata.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/actions/*.*
%{_iconsdir}/hicolor/*/apps/*.*
%{_iconsdir}/hicolor/*/emblems/remmina-sftp-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-ssh-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-tool-symbolic.svg
%{_iconsdir}/hicolor/*/status/remmina-status.svg
%dir %{_iconsdir}/hicolor/apps
%{_iconsdir}/hicolor/apps/*.*
%{_datadir}/mime/packages/*.xml
%{_datadir}/%{name}/
%dir %{_libdir}/remmina/
%dir %{_libdir}/remmina/plugins/
%{_mandir}/man1/remmina.1*
%{_mandir}/man1/remmina-file-wrapper.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/
%{_pkgconfigdir}/%{name}.pc
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake

%if %{with exec}
%files plugins-exec
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/remmina/plugins/remmina-plugin-exec.so
%endif

%if %{with rdp}
%files plugins-rdp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/remmina/plugins/remmina-plugin-rdp.so
%{_iconsdir}/hicolor/*/emblems/remmina-rdp-ssh-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-rdp-symbolic.svg
%endif

%if %{with secret}
%files plugins-secret
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/remmina/plugins/remmina-plugin-secret.so
%endif

%if %{with spice}
%files plugins-spice
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/remmina/plugins/remmina-plugin-spice.so
%{_iconsdir}/hicolor/*/emblems/remmina-spice-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-spice-ssh-symbolic.svg
%endif

%if %{with vnc}
%files plugins-vnc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/remmina/plugins/remmina-plugin-vnc.so
%{_iconsdir}/hicolor/*/emblems/remmina-vnc-ssh-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-vnc-symbolic.svg
%endif

%if %{with www}
%files plugins-www
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/remmina/plugins/remmina-plugin-www.so
%{_iconsdir}/hicolor/*/emblems/remmina-www-symbolic.svg
%endif

%changelog
