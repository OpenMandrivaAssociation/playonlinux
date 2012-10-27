%define oname PlayOnLinux

Summary:	Play your Windows games on Linux
Name:		playonlinux
Version:	4.1.8
Release:	%mkrel 1
License:	GPLv3
Group:		Games/Other
Url:		http://www.playonlinux.com
Source0:	http://www.playonlinux.com/script_files/%{oname}/%{version}/%{oname}_%{version}.tar.gz
Source1:	playonlinux
Patch0:         %{oname}_4.1.6-disable-GL-checks.patch
Patch1:		%{oname}_4.1.6-fix-desktop-file.patch
BuildRequires:	desktop-file-utils
Requires:	wxPythonGTK
Requires:	imagemagick
Requires:	wget
Requires:	gettext
Requires:	unzip
Requires:	cabextract
Requires:	xz
Requires:	xterm
%ifarch x86_64
Requires:	wine64
%else
Requires:	wine-full
%endif
Requires:	glxinfo
Requires:       icoutils
# for ar
Requires:	binutils

%description
PlayOnLinux is a piece of sofware which allows you to install 
and use easily numerous games and software designed to run 
with Microsoft(R)'s Windows(R). Indeed, currently, still few 
games are compatible with GNU/Linux, and it could be a factor 
preventing from migrating to this system. PlayOnLinux brings an 
accessible and efficient solution to this problem, cost-free 
and respectful of the free software.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/desktop-directories
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

cp -a * %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_datadir}/%{name}/bin/

install -p %{SOURCE1} %{buildroot}%{_bindir}/
cp etc/PlayOnLinux.desktop %{buildroot}%{_datadir}/applications/%{oname}.desktop
cp  %{buildroot}%{_datadir}/%{name}/etc/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp %{buildroot}%{_datadir}/%{name}/etc/PlayOnLinux.directory %{buildroot}%{_datadir}/desktop-directories/%{oname}.directory

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*  

%files
%doc LICENCE CHANGELOG
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/desktop-directories/%{oname}.directory


%changelog

* Tue Oct 02 2012 tv <tv> 4.1.8-1.mga3
+ Revision: 302226
- new release
- require xz instead of lzma

* Sun Aug 19 2012 stormi <stormi> 4.1.6-1.mga3
+ Revision: 282291
- fix disable-GL-checks patch again
- add patch to fix desktop file
- rediff disable-GL-checks patch
- new version 4.1.6

* Sat Aug 04 2012 tv <tv> 4.1.3-4.mga3
+ Revision: 278478
- seems to be 64bit friendly now

* Wed Aug 01 2012 tv <tv> 4.1.3-3.mga3
+ Revision: 277680
- make it installable with wine64

* Sun Jul 29 2012 dmorgan <dmorgan> 4.1.3-2.mga3
+ Revision: 275814
- Add icoutils as Requires

* Sun Jul 22 2012 dmorgan <dmorgan> 4.1.3-1.mga3
+ Revision: 273571
- New version

* Tue Jun 26 2012 dams <dams> 4.1.2-1.mga3
+ Revision: 264003
- new version 4.1.2
- rediff patch
- clean specfile

* Tue Mar 06 2012 pterjan <pterjan> 4.0.15-2.mga2
+ Revision: 220557
- Drop the GL check binaries and use Debian patch to not call them

* Sun Mar 04 2012 stormi <stormi> 4.0.15-1.mga2
+ Revision: 218248
- new version 4.0.15

* Sun Jan 29 2012 stormi <stormi> 4.0.14-1.mga2
+ Revision: 202906
- new version 4.0.14

* Sat Jan 28 2012 tv <tv> 4.0.13-2.mga2
+ Revision: 202547
- rebuild for missing packages

* Sun Oct 23 2011 stormi <stormi> 4.0.13-1.mga2
+ Revision: 157541
- update to version 4.0.13

* Mon May 16 2011 ahmad <ahmad> 3.8.12-2.mga1
+ Revision: 99316
- playonlinux explicitly requires wine-full (i.e. i586 wine package), so it
  shouldn't exist in x86_64 repos; i.e. it should be exclusive arch %%ix86

* Fri Mar 11 2011 stormi <stormi> 3.8.12-1.mga1
+ Revision: 68233
- new version 3.8.12

* Fri Mar 11 2011 stormi <stormi> 3.8.8-2.mga1
+ Revision: 68228
- clean spec
- imported package playonlinux

