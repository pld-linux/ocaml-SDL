#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		ocaml_ver	1:3.09.2
Summary:	SDL binding for OCaml
Summary(pl.UTF-8):	Wiązania SDL dla OCamla
Name:		ocaml-SDL
Version:	0.9.1
Release:	4
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/ocamlsdl/ocamlsdl-%{version}.tar.gz
# Source0-md5:	c3086423991fcdc1ba468afd52fc112b
URL:		http://ocamlsdl.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-lablgl-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simply speaking, OCamlSDL is an attempt to write a software interface
between the ML programming language and the SDL C library.

This package contains files needed to run bytecode executables using
this library.

%description -l pl.UTF-8
OCamlSDL to próba napisania interfejsu programowego między językiem
programowania ML a biblioteką C SDL.

Ten pakiet zawiera pliki potrzebne do uruchamiania wykonywalnego
bytecodu używającego tej biblioteki.

%package devel
Summary:	SDL binding for OCaml - development part
Summary(pl.UTF-8):	Wiązania SDL dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
Simply speaking, OCamlSDL is an attempt to write a software interface
between the ML programming language and the SDL C library.

This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl.UTF-8
OCamlSDL to próba napisania interfejsu programowego między językiem
programowania ML a biblioteką C SDL.

Ten pakiet zawiera pliki potrzebne do tworzenia programów w OCamlu
używających tej biblioteki.

%prep
%setup -q -n ocamlsdl-%{version}

%build
cp -f /usr/share/automake/config.* support
%{__aclocal} -I support
%{__autoconf}
%configure
%{__make} \
	%{!?with_ocaml_opt:OCAMLOPT=}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs

%{__make} install \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	%{!?with_ocaml_opt:OCAMLOPT=}

# ocamlfind-specific, useless in rpm
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/*.owner

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllsdlstub.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllsdlgfxstub.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllsdlloaderstub.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllsdlmixerstub.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllsdlttfstub.so

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%dir %{_libdir}/ocaml/sdl
%{_libdir}/ocaml/sdl/META
%{_libdir}/ocaml/sdl/libsdl*.a
%{_libdir}/ocaml/sdl/sdl*.cma
%{_libdir}/ocaml/sdl/sdl*.cmi
# doc?
%{_libdir}/ocaml/sdl/sdl*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/sdl/sdl*.a
%{_libdir}/ocaml/sdl/sdl*.cmx
%{_libdir}/ocaml/sdl/sdl*.cmxa
%endif
