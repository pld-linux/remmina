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
BuildRequires:	freerdp2-devel >= 2.0.0-0.20190320
BuildRequires:	gettext
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	json-glib-devel
BuildRequires:	libappindicator-gtk3-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libsecret-devel
BuildRequires:	libsoup-devel
BuildRequires:	libssh-devel >= 0.6
BuildRequires:	libvncserver-devel
#BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	spice-gtk-devel
BuildRequires:	xorg-lib-libxkbfile-devel

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

%prep
%setup -qn Remmina-v%{version}

%build
mkdir -p build

%cmake --build=build \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DWITH_APPINDICATOR=ON \
	-DWITH_AVAHI=ON \
	-DWITH_FREERDP=ON \
	-DWITH_GCRYPT=ON \
	-DWITH_GETTEXT=ON \
	-DWITH_LIBSSH=ON \
	-DWITH_SPICE=ON \
	-DWITH_TELEPATHY=ON \
	-DWITH_VTE=ON \
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
%attr(755,root,root) %{_bindir}/remmina
%{_datadir}/metainfo/*.appdata.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/actions/*.*
%{_iconsdir}/hicolor/*/apps/*.*
%{_datadir}/mime/packages/*.xml
%{_datadir}/%{name}/
%dir %{_libdir}/remmina/
%dir %{_libdir}/remmina/plugins/
%{_mandir}/man1/%{name}.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/
%{_pkgconfigdir}/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake

%files plugins-exec
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-exec.so

%files plugins-secret
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-secret.so

%files plugins-nx
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-nx.so
%{_iconsdir}/hicolor/*/emblems/remmina-nx-symbolic.svg

%files plugins-rdp
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-rdp.so
%{_iconsdir}/hicolor/*/emblems/remmina-rdp-ssh-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-rdp-symbolic.svg

%files plugins-vnc
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-vnc.so
%{_iconsdir}/hicolor/*/emblems/remmina-vnc-ssh-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-vnc-symbolic.svg

%files plugins-xdmcp
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-xdmcp.so
%{_iconsdir}/hicolor/*/emblems/remmina-xdmcp-ssh-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-xdmcp-symbolic.svg

%files plugins-spice
%defattr(644,root,root,755)
%{_libdir}/remmina/plugins/remmina-plugin-spice.so
%{_iconsdir}/hicolor/*/emblems/remmina-spice-symbolic.svg
%{_iconsdir}/hicolor/*/emblems/remmina-spice-ssh-symbolic.svg

%changelog
