%define oname PlayOnLinux

Summary:	Play your Windows games on Linux
Name:		playonlinux
Version:	3.2.2
Release:	%mkrel 2
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
Requires:	wine
Requires:	mesa-demos
# for ar
Requires:	binutils
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PlayOnLinux is a piece of sofware which allow you to install 
and use easily numerous games and softwares designed to run 
with Microsoft(R)'s Windows(R).Indeed, currently, still few 
games are compatible with GNU/Linux, and it could be a factor 
preventing from migrate to this system. PlayOnLinux brings an 
accessible and efficient solution to this problem, cost-free 
and rescpetful of the free softwares.

%prep
%setup -q -n %{name}

%install
rm -rf %{buildroot}
mkdir %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/desktop-directories
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

cp -a * %{buildroot}%{_datadir}/%{name}

install -p %{SOURCE1} %{buildroot}%{_bindir}/
rm %{buildroot}%{_datadir}/%{name}/LICENCE
cp etc/PlayOnLinux.desktop %{buildroot}%{_datadir}/applications/%{oname}.desktop
cp  %{buildroot}%{_datadir}/%{name}/etc/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp %{buildroot}%{_datadir}/%{name}/etc/PlayOnLinux.directory %{buildroot}%{_datadir}/desktop-directories/%{oname}.directory

desktop-file-install \
	--add-category="Game" \
	--remove-category="%{oname}" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*  

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENCE CHANGELOG
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/desktop-directories/%{oname}.directory
