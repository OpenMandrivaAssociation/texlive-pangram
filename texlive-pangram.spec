%global tl_name pangram
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0c
Release:	%{tl_revision}.1
Summary:	A LaTeX package for testing fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pangram
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pangram.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pangram.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pangram.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a simple way for font designers and users to test
their fonts in different sizes without much input.

