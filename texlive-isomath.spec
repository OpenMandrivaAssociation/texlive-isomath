# revision 21296
# category Package
# catalog-ctan /macros/latex/contrib/isomath
# catalog-date 2011-02-02 19:41:03 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-isomath
Version:	0.5
Release:	1
Summary:	Mathematics "for scientists" (conformant to ISO 31)
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
The isomath package enables formatting Greek and Latin letters
as symbols for vectors, matrices, and tensors in the typefaces
recommended for scientific papers by the International Standard
ISO 31.

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
