%define	oname	PlayOnLinux

Summary:	Play your Windows games on Linux
Name:		playonlinux
Version:	4.3.4
Release:	2
License:	GPLv3+
Group:		Games/Other
Url:		http://www.playonlinux.com
#Source0:	http://www.playonlinux.com/script_files/%{oname}/%{version}/%{oname}_%{version}.tar.gz
Source0:  http://repository.playonlinux.com/%{oname}/%{version}/%{oname}_%{version}.tar.gz
Source1:	playonlinux.bin
Patch0:		%{oname}_4.3.4-disable-update-OpenMandriva.patch
Patch1:		%{oname}_4.3.4-disable-GL-check-OpenMandriva.patch
Patch2:		%{oname}_4.3.4-use-systemwide-locales-OpenMandriva.patch
# Do we still need patch3? Disable for now. Feel free to reenable it and edit it to fix patching process.
#Patch3:		%{oname}-4.2.1-fix-desktop-file.patch
# for ar
Requires:	binutils
Requires:	cabextract
Requires:	gettext
Requires:	glxinfo
Requires:	imagemagick
Requires:	lzma
Requires:	7zip
Requires:	unzip
Requires:	wget
Requires:	xterm
Requires:	curl
Recommends:	wine-bin
# used to extract icons for applications, otherwise the default icon is used
Recommends:	icoutils >= 0.29
#Not imported to cooker (yet)
#Recommends: jq
BuildArch:	noarch

%description
PlayOnLinux is a piece of sofware which allows you to install and use easily
numerous games and software designed to run with Microsoft(R)'s Windows(R).
Indeed, currently, still few games are compatible with GNU/Linux, and it could
be a factor preventing from migrating to this system. PlayOnLinux brings an 
accessible and efficient solution to this problem, cost-free and respectful of
the free software.

%files -f pol.lang
%doc LICENCE CHANGELOG.md
%{_sysconfdir}/xdg/menus/applications-merged/%{name}*.menu
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/desktop-directories/%{oname}.directory

#----------------------------------------------------------------------------

%prep
%autosetup -p0 -n %{name}

%build

%install
# Prepare the needed dirs
mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/desktop-directories
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/locale

# Add exec perms to files lacking them and kill other rpmlint warnings
chmod +x tests/bash/test-versionlower tests/python/test_versionlower.py

# Copy all in the dest dir
cp -a * %{buildroot}%{_datadir}/%{name}

# Move the needed bits in their right place
install -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}
cp etc/*.menu %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
cp etc/%{oname}.desktop %{buildroot}%{_datadir}/applications/%{oname}.desktop
cp %{buildroot}%{_datadir}/%{name}/etc/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp %{buildroot}%{_datadir}/%{name}/etc/%{oname}.directory %{buildroot}%{_datadir}/desktop-directories/%{oname}.directory
cp -a lang/locale/* %{buildroot}%{_datadir}/locale/

# (tpg) useless stuff
rm -rf %{buildroot}%{_datadir}/%{name}/bin
rm -rf %{buildroot}%{_datadir}/%{name}/src
rm -rf %{buildroot}%{_datadir}/%{name}/etc/*.menu
rm -rf %{buildroot}%{_datadir}/%{name}/etc/*.desktop
rm -rf %{buildroot}%{_datadir}/%{name}/etc/*.directory
rm -rf %{buildroot}%{_datadir}/%{name}/etc/*.applescript
rm -rf %{buildroot}%{_datadir}/%{name}/etc/*.icns
rm -rf %{buildroot}%{_datadir}/%{name}/lang
rm -rf %{buildroot}%{_datadir}/%{name}/CHANGELOG
rm -rf %{buildroot}%{_datadir}/%{name}/playonmac

%find_lang pol

