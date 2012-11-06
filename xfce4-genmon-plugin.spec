%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Generic Monitor XFce panel plugin (GenMon)
Name:		xfce4-genmon-plugin
Version:	3.4.0
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-genmon-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-genmon-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.9.0
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfce4ui-devel
Obsoletes:	xfce-genmon-plugin

%description
This plugin cyclically spawns the indicated script/program, captures its 
output (stdout) and displays the resulting string into the panel.

%prep
%setup -qn %{name}-3.4

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel/plugins/libgenmon.so
%{_datadir}/xfce4/panel/plugins/*.desktop
