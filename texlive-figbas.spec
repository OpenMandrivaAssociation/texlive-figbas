%global tl_name figbas
%global tl_revision 28943

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.3
Release:	%{tl_revision}.1
Summary:	Mini-fonts for figured-bass notation in music
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/figbas
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figbas.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figbas.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package consists of three mini-fonts (and associated metrics) of
conventional ligatures for the figured-bass notations 2+, 4+, 5+, 6+ and
9+ in music manuscripts. The fonts are usable with Computer Modern Roman
and Sans, and Palatino/Palladio, respectively.

