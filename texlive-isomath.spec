# revision 27654
# category Package
# catalog-ctan /macros/latex/contrib/isomath
# catalog-date 2012-09-12 18:41:18 +0200
# catalog-license lppl
# catalog-version 0.6.1
Name:		texlive-isomath
Version:	0.6.1
Release:	1
Summary:	Mathematics style for science and technology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isomath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isomath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isomath.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides tools for a mathematical style that
conforms to the International Standard ISO 80000-2 and is
common in science and technology. It changes the default shape
of capital Greek letters to italic, sets up bold italic and
sans-serif bold italic math alphabets with Latin and Greek
characters, and defines macros for markup of vector, matrix and
tensor symbols.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/isomath/isomath.sty
%doc %{_texmfdistdir}/doc/latex/isomath/README.html
%doc %{_texmfdistdir}/doc/latex/isomath/README.txt
%doc %{_texmfdistdir}/doc/latex/isomath/isomath-test.pdf
%doc %{_texmfdistdir}/doc/latex/isomath/isomath-test.tex
%doc %{_texmfdistdir}/doc/latex/isomath/isomath.html
%doc %{_texmfdistdir}/doc/latex/isomath/isomath.pdf
%doc %{_texmfdistdir}/doc/latex/isomath/isomath.sty.html
%doc %{_texmfdistdir}/doc/latex/isomath/isomath.sty.txt
%doc %{_texmfdistdir}/doc/latex/isomath/isomath.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
