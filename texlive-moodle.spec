%global tl_name moodle
%global tl_revision 65672

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Generating Moodle quizzes via LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/moodle
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moodle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moodle.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moodle.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for writing Moodle quizzes in LaTeX. In addition to
typesetting the quizzes for proofreading, the package compiles an XML
file to be uploaded to a Moodle server.

