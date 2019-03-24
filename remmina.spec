#
# note: disabling plugins will still build them if deps are met
#
# Conditional build:
%bcond_without	exec		# do not build exec plugin
%bcond_with	nx		# build nx plugin
%bcond_without	rdp		# do not build rdp plugin
%bcond_without	secret		# do not build secret plugin
%bcond_without	spice		# do not build spice plugin
%bcond_without	telepathy	# do not build telepathy plugin
%bcond_without	vnc		# do not build vnc plugin
%bcond_without	vte		# do not build vte plugin
%bcond_without	xdmcp		# do not build xdmcp plugin
#
Summary:	Remote Desktop Client
Name:		remmina
Version:	1.3.4
Release:	1
License:	GPLv2+ and MIT
Group:		X11/Applications
Source0:	https://gitlab.com/Remmina/Remmina/-/archive/v1.3.4/Remmina-v%{version}.tar.bz2
# Source0-md5:	cd00d28c5b895037901d8aa9f9ace9fc
# Cmake helper file to easy build plugins outside remmina source tree
# See http://www.muflone.com/remmina-plugin-rdesktop/english/install.html which
# use http://www.muflone.com/remmina-plugin-builder/ with remmina bundled source.
# So we can't use it directly only as instructions.
Source1:	pluginBuild-CMakeLists.txt
URL:		http://remmina.org
BuildRequires:	appstream-glib
BuildRequires:	avahi-ui-gtk3-devel >= 0.6.30
BuildRequires:	cmake >= 2.8
BuildRequires:	desktop-file-utils
%{?with_rdp:BuildRequires:	freerdp2-devel >= 2.0.0-0.20190320}
BuildRequires:	gettext
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	json-glib-devel
BuildRequires:	libappindicator-gtk3-devel
BuildRequires:	libgcrypt-devel
%{?with_secret:BuildRequires:	libsecret-devel}
BuildRequires:	libsoup-devel
BuildRequires:	libssh-devel >= 0.6
%{?with_vnc:BuildRequires:	libvncserver-devel}
BuildRequires:	rpmbuild(macros) >= 1.742
%{?with_spice:BuildRequires:	spice-gtk-devel}
%{?with_telepathy:BuildRequires:	telepathy-glib-devel}
%{?with_vte:BuildRequires:	vte2.90-devel}
BuildRequires:	xorg-lib-libxkbfile-devel
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

%package        plugins-nx
Summary:	NX plugin for Remmina Remote Desktop Client
Requires:	%{name} = %{version}-%{release}
Requires:	nxproxy

%description    plugins-nx
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travelers, who need to work with
lots of remote computers in front of either large monitors or tiny
net-books.

This package contains the NX plugin for the Remmina remote desktop
client.

%package        plugins-rdp
Summary:	RDP plugin for Remmina Remote Desktop Client
Requires:	%{name} = %{version}-%{release}

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

%package        plugins-telepathy
Summary:	Telepathy plugin for Remmina Remote Desktop Client
Requires:	%{name} = %{version}-%{release}

%description    plugins-telepathy
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travelers, who need to work with
lots of remote computers in front of either large monitors or tiny
net-books.

This package contains the Telepathy plugin for the Remmina remote
desktop client.

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

%package        plugins-xdmcp
Summary:	XDMCP plugin for Remmina Remote Desktop Client
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-xserver-Xephyr

%description    plugins-xdmcp
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travelers, who need to work with
lots of remote computers in front of either large monitors or tiny
net-books.

This package contains the XDMCP plugin for the Remmina remote desktop
client.

%prep
%setup -qn Remmina-v%{version}
%{__sed} -i s/^pt_PT$// po/LINGUAS
%{__rm} -f po/pt_PT.po

%build
mkdir -p build

%cmake --build=build \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DWITH_APPINDICATOR=ON \
	-DWITH_AVAHI=ON \
	%{cmake_on_off rdp FREERDP} \
	-DWITH_GCRYPT=ON \
	-DWITH_GETTEXT=ON \
	-DWITH_LIBSSH=ON \
	%{cmake_on_off vnc LIBVNCSERVER} \
	%{cmake_on_off spice SPICE} \
	%{cmake_on_off telepathy TELEPATHY} \
	%{cmake_on_off vte VTE} \
	.

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_libdir}/cmake/%{name}/
cp -pr cmake/*.cmake $RPM_BUILD_ROOT/%{_libdir}/cmake/%{name}/
cp -pr config.h.in $RPM_BUILD_ROOT/%{_includedir}/%{name}/
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_includedir}/%{name}/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc LICENSE AUTHORS ChangeLog README.md
%attr(755,root,root) %{_bindir}/gnome-session-remmina
%attr(755,root,root) %{_bindir}/remmina
%attr(755,root,root) %{_bindir}/remmina-gnome
%{_datadir}/metainfo/*.appdata.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/actions/*.*
%{_iconsdir}/hicolor/*/apps/*.*
%{_iconsdir}/hicolor/*/emblems/remmina-sftp-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-ssh-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-tool-symbolic.svg
%{_datadir}/mime/packages/*.xml
%{_datadir}/%{name}/
%{_datadir}/xsessions/remmina-gnome.desktop
%dir %{_libdir}/remmina/
%dir %{_libdir}/remmina/plugins/
%{_libdir}/remmina/plugins/remmina-plugin-st.so
%{_mandir}/man1/remmina.1*
%{_mandir}/man1/gnome-session-remmina.1*
%{_mandir}/man1/remmina-gnome.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/
%{_pkgconfigdir}/%{name}.pc
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake

%if %{with exec}
%files plugins-exec
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-exec.so
%endif

%if %{with nx}
%files plugins-nx
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-nx.so
%{_iconsdir}/hicolor/*/emblems/remmina-nx-symbolic.svg
%endif

%if %{with rdp}
%files plugins-rdp
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-rdp.so
%{_iconsdir}/hicolor/*/emblems/remmina-rdp-ssh-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-rdp-symbolic.svg
%endif

%if %{with secret}
%files plugins-secret
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-secret.so
%endif

%if %{with spice}
%files plugins-spice
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-spice.so
%{_iconsdir}/hicolor/*/emblems/remmina-spice-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-spice-ssh-symbolic.svg
%endif

%if %{with telepathy}
%files plugins-telepathy
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-telepathy.so
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Remmina.service
%{_datadir}/telepathy/clients/Remmina.client
%endif

%if %{with vnc}
%files plugins-vnc
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-vnc.so
%{_iconsdir}/hicolor/*/emblems/remmina-vnc-ssh-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-vnc-symbolic.svg
%endif

%if %{with xdmcp}
%files plugins-xdmcp
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-xdmcp.so
%{_iconsdir}/hicolor/*/emblems/remmina-xdmcp-ssh-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-xdmcp-symbolic.svg
%endif

%changelog
