# revision 21037
# category Package
# catalog-ctan /fonts/figbas
# catalog-date 2009-05-20 15:30:38 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-figbas
Version:	1.0
Release:	1
Summary:	Mini-fonts for figured-bass notation in music
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/figbas
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figbas.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
This package consists of three mini-fonts (and associated
metrics) of conventional ligatures for the figured-bass
notations 2+, 4+, 5+, 6+ and 9+ in music manuscripts. The fonts
are usable with Computer Modern Roman and Sans, and
Palatino/Palladio, respectively.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
