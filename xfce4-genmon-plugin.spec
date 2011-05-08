%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Generic Monitor XFce panel plugin (GenMon)
Name:		xfce4-genmon-plugin
Version:	3.3.0
Release:	%mkrel 1
License:	LGPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-genmon-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-genmon-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfcegui4-devel
Obsoletes:	xfce-genmon-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot 

%description
This plugin cyclically spawns the indicated script/program, captures its 
output (stdout) and displays the resulting string into the panel.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README 
%{_libdir}/xfce4/panel-plugins/
%{_datadir}/xfce4/panel-plugins/*
