Summary:	Generic Monitor XFce panel plugin (GenMon)	
Name:		xfce4-genmon-plugin
Version:	3.2
Release:	%mkrel 8
License:	LGPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-genmon-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-genmon-plugin/%{name}-%{version}.tar.bz2
Patch0:		%{name}-3.2-dont-spawn-zobies.patch
Patch1:		%{name}-3.2-kill-unused-pipes.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-genmon-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot 

%description
This plugin cyclically spawns the indicated script/program, captures its 
output (stdout) and displays the resulting string into the panel.
 
%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

# remove unneeded devel files
#rm -f %{buildroot}/%{_libdir}/xfce4/panel-plugins/libgenmon.a

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README 
%{_libdir}/xfce4/panel-plugins/
%{_datadir}/xfce4/panel-plugins/*
