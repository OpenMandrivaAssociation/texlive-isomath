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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The isomath package enables formatting Greek and Latin letters
as symbols for vectors, matrices, and tensors in the typefaces
recommended for scientific papers by the International Standard
ISO 31.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
