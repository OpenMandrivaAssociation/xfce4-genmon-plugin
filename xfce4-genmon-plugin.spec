%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	Generic Monitor XFce panel plugin (GenMon)
Name:		xfce4-genmon-plugin
Version:	4.1.1
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-genmon-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-genmon-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4ui-2)

%description
This plugin cyclically spawns the indicated script/program, captures its 
output (stdout) and displays the resulting string into the panel.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README*
%{_libdir}/xfce4/panel/plugins/
%{_datadir}/xfce4/panel/plugins/*
%{_iconsdir}/hicolor/*x*/apps/org.xfce.genmon.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.genmon.svg
