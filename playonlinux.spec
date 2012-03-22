%define oname PlayOnLinux

Summary:	Play your Windows games on Linux
Name:		playonlinux
Version:	4.0.16
Release:	%mkrel 1
License:	GPLv3
Group:		Games/Other
Url:		http://www.playonlinux.com
Source0:	http://www.playonlinux.com/script_files/%{oname}/%{version}/%{oname}_%{version}.tar.gz
Source1:	playonlinux
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

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}/
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__mkdir_p %{buildroot}%{_datadir}/desktop-directories
%__mkdir_p %{buildroot}%{_datadir}/applications
%__mkdir_p %{buildroot}%{_datadir}/pixmaps

%__cp -a * %{buildroot}%{_datadir}/%{name}

%ifarch x86_64
%__rm -rf %{buildroot}%{_datadir}/%{name}/bin/*x86
%else
%__rm -rf %{buildroot}%{_datadir}/%{name}/bin/*amd64
%endif

%__install -p %{SOURCE1} %{buildroot}%{_bindir}/
%__cp etc/PlayOnLinux.desktop %{buildroot}%{_datadir}/applications/%{oname}.desktop
%__cp  %{buildroot}%{_datadir}/%{name}/etc/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%__cp %{buildroot}%{_datadir}/%{name}/etc/PlayOnLinux.directory %{buildroot}%{_datadir}/desktop-directories/%{oname}.directory

desktop-file-install \
	--add-category="Game" \
	--remove-category="%{oname}" \
	--remove-key="Encoding" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*  

%clean
%__rm -rf %{buildroot}

%files
%doc LICENCE CHANGELOG
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/desktop-directories/%{oname}.directory
