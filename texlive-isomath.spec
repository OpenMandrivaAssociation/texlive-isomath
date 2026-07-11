%global tl_name isomath
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6.1
Release:	%{tl_revision}.1
Summary:	Mathematics style for science and technology
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/isomath
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isomath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isomath.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides tools for a mathematical style that conforms to the
International Standard ISO 80000-2 and is common in science and
technology. It changes the default shape of capital Greek letters to
italic, sets up bold italic and sans-serif bold italic math alphabets
with Latin and Greek characters, and defines macros for markup of
vector, matrix and tensor symbols.

