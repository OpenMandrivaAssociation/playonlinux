%define oname PlayOnLinux

Summary:	Play your Windows games on Linux
Name:		playonlinux
Version:	4.1.8
Release:	1
License:	GPLv3
Group:		Games/Other
Url:		http://www.playonlinux.com
Source0:	http://www.playonlinux.com/script_files/%{oname}/%{version}/%{oname}_%{version}.tar.gz
Source1:	playonlinux.bin
Patch0:		PlayOnLinux_4.0.17-disable-update.patch
Patch1:		PlayOnLinux_4.0.18-disable-GL-checks.patch
Patch2:		PlayOnLinux_4.0.17-use-systemwide-locales-path.patch
BuildRequires:	desktop-file-utils
Requires:	wxPythonGTK
Requires:	imagemagick
Requires:	wget
Requires:	gettext
Requires:	unzip
Requires:	cabextract
Requires:	lzma
Requires:	xterm
Requires:	wine-full
%if %mdkversion > 201000
Requires:	glxinfo
%else
Requires:	mesa-demos
%endif
# for ar
Requires:	binutils
# used to extract icons for applications, otherwise the default icon is used
Suggests:	icoutils
BuildArch:	noarch

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
#%patch0 -p1
#%patch1 -p1
%patch2 -p1

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}
%__mkdir_p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
%__mkdir_p %{buildroot}%{_bindir}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__mkdir_p %{buildroot}%{_datadir}/desktop-directories
%__mkdir_p %{buildroot}%{_datadir}/applications
%__mkdir_p %{buildroot}%{_datadir}/pixmaps

cp -a * %{buildroot}%{_datadir}/%{name}
cp etc/*.menu %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
%__install -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}

cp etc/PlayOnLinux.desktop %{buildroot}%{_datadir}/applications/%{oname}.desktop
cp %{buildroot}%{_datadir}/%{name}/etc/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp %{buildroot}%{_datadir}/%{name}/etc/PlayOnLinux.directory %{buildroot}%{_datadir}/desktop-directories/%{oname}.directory

desktop-file-install \
	--add-category="Game" \
	--remove-category="%{oname}" \
	--remove-key="Encoding" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%__mkdir_p %{buildroot}%{_datadir}/locale
cp -a lang/locale/* %{buildroot}%{_datadir}/locale/

# (tpg) useless stuff
%__rm -rf %{buildroot}%{_datadir}/%{name}/bin
%__rm -rf %{buildroot}%{_datadir}/%{name}/src
%__rm -rf %{buildroot}%{_datadir}/%{name}/etc/*.menu
%__rm -rf %{buildroot}%{_datadir}/%{name}/etc/*.desktop
%__rm -rf %{buildroot}%{_datadir}/%{name}/etc/*.directory
%__rm -rf %{buildroot}%{_datadir}/%{name}/lang
%__rm -rf %{buildroot}%{_datadir}/%{name}/CHANGELOG
%__rm -rf %{buildroot}%{_datadir}/%{name}/playonmac

%find_lang pol

%files -f pol.lang
%doc LICENCE CHANGELOG
%{_sysconfdir}/xdg/menus/applications-merged/%{name}*.menu
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/desktop-directories/%{oname}.directory

