Summary:	Generic Monitor XFce panel plugin (GenMon)	
Name:		xfce-genmon-plugin
Version:	3.1
Release:	%mkrel 1
License:	BSD
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-genmon-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-genmon-plugin/xfce4-genmon-plugin-%{version}.tar.bz2
Group:		Graphical desktop/Xfce
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot 

%description
This plugin cyclically spawns the indicated script/program, captures its 
output (stdout) and displays the resulting string into the panel.
 
%prep
%setup -qn xfce4-genmon-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

# remove unneeded devel files
#rm -f %{buildroot}/%{_libdir}/xfce4/panel-plugins/libgenmon.a
%find_lang xfce4-genmon-plugin
%clean
rm -rf %{buildroot}

%files -f xfce4-genmon-plugin.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README 
%{_libdir}/xfce4/panel-plugins/
%{_datadir}/xfce4/panel-plugins/*

