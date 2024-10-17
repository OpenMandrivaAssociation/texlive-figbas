Name:		texlive-figbas
Version:	28943
Release:	2
Summary:	Mini-fonts for figured-bass notation in music
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/figbas
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figbas.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figbas.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package consists of three mini-fonts (and associated
metrics) of conventional ligatures for the figured-bass
notations 2+, 4+, 5+, 6+ and 9+ in music manuscripts. The fonts
are usable with Computer Modern Roman and Sans, and
Palatino/Palladio, respectively.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/figbas/cmrj.afm
%{_texmfdistdir}/fonts/afm/public/figbas/cmssj.afm
%{_texmfdistdir}/fonts/afm/public/figbas/plrj.afm
%{_texmfdistdir}/fonts/map/dvips/figbas/figbas.map
%{_texmfdistdir}/fonts/tfm/public/figbas/cmrj.tfm
%{_texmfdistdir}/fonts/tfm/public/figbas/cmssj.tfm
%{_texmfdistdir}/fonts/tfm/public/figbas/plrj.tfm
%{_texmfdistdir}/fonts/type1/public/figbas/cmrj.pfb
%{_texmfdistdir}/fonts/type1/public/figbas/cmssj.pfb
%{_texmfdistdir}/fonts/type1/public/figbas/plrj.pfb
%doc %{_texmfdistdir}/doc/fonts/figbas/README
%doc %{_texmfdistdir}/doc/fonts/figbas/example.pdf
%doc %{_texmfdistdir}/doc/fonts/figbas/example.tex
%doc %{_texmfdistdir}/doc/fonts/figbas/figbas.pdf
%doc %{_texmfdistdir}/doc/fonts/figbas/figbas.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
