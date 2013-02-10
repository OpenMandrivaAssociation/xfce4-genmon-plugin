%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Generic Monitor XFce panel plugin (GenMon)
Name:		xfce4-genmon-plugin
Version:	3.4.0
Release:	2
License:	LGPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-genmon-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-genmon-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.9.0
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4ui-1)

%description
This plugin cyclically spawns the indicated script/program, captures its 
output (stdout) and displays the resulting string into the panel.

%prep
%setup -qn %{name}-%{url_ver}

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README 
%{_libdir}/xfce4/panel/plugins/
%{_datadir}/xfce4/panel/plugins/*


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 3.3.1-2
+ Revision: 791556
- Rebuild

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 3.3.1-1
+ Revision: 789804
- update to new version 3.3.1

* Sun May 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 3.3.0-1
+ Revision: 672532
- update to new version 3.3.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2-8mdv2010.1
+ Revision: 543426
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 3.2-7mdv2010.0
+ Revision: 446026
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2-6mdv2009.1
+ Revision: 349456
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2-5mdv2009.1
+ Revision: 294996
- rebuild for new Xfce4.6 beta1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 3.2-4mdv2009.0
+ Revision: 269786
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2-3mdv2009.0
+ Revision: 199474
- Patch1: kill unused pipes

* Thu Apr 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2-2mdv2009.0
+ Revision: 195034
- Patch0: prevent genmon to spawn zobie processes (upstream bug #3896)

* Mon Mar 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2-1mdv2008.1
+ Revision: 188248
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1-2mdv2008.1
+ Revision: 110120
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING and INSTALL
- use upstream name

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1-1mdv2008.0
+ Revision: 30370
- add buildrequires on per-XML-Parser
- own translation files
- new version

