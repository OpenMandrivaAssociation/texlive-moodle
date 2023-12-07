Name:		texlive-moodle
Version:	65672
Release:	1
Summary:	Generating Moodle quizzes via LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/moodle
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moodle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moodle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moodle.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for writing Moodle quizzes in LaTeX. In addition to
typesetting the quizzes for proofreading, the package compiles
an XML file to be uploaded to a Moodle server.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/moodle
%{_texmfdistdir}/tex/latex/moodle
%doc %{_texmfdistdir}/doc/latex/moodle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
