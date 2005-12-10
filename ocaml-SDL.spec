Summary:	SDL binding for OCaml
Summary(pl):	Wi±zania SDL dla OCamla
Name:		ocaml-SDL
Version:	0.7.2
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/ocamlsdl/ocamlsdl-%{version}.tar.gz
# Source0-md5:	0707a9cf80bd9cfe18ad660dc077bad6
URL:		http://ocamlsdl.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	ocaml >= 3.07
BuildRequires:	ocaml-lablgl-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simply speaking, OCamlSDL is an attempt to write a software interface
between the ML programming language and the SDL C library.

This package contains files needed to run bytecode executables using
this library.

%description -l pl
OCamlSDL to próba napisania interfejsu programowego miêdzy jêzykiem
programowania ML a bibliotek± C SDL.

Ten pakiet zawiera pliki potrzebne do uruchamiania wykonywalnego
bytecodu u¿ywaj±cego tej biblioteki.

%package devel
Summary:	SDL binding for OCaml - development part
Summary(pl):	Wi±zania SDL dla OCamla - cze¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
Simply speaking, OCamlSDL is an attempt to write a software interface
between the ML programming language and the SDL C library.

This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl
OCamlSDL to próba napisania interfejsu programowego miêdzy jêzykiem
programowania ML a bibliotek± C SDL.

Ten pakiet zawiera pliki potrzebne do tworzenia programów w OCamlu
u¿ywaj±cych tej biblioteki.

%prep
%setup -q -n ocamlsdl-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	OCAMLLIBDIR=%{_libdir}/ocaml \
	OCAMLSDLDIR=%{_libdir}/ocaml/sdl \
	DESTDIR=$RPM_BUILD_ROOT \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(644,root,root,755)
%doc README AUTHORS NEWS doc/html doc/ocaml*
%dir %{_libdir}/ocaml/sdl
%{_libdir}/ocaml/sdl/*
%attr(755,root,root) %{_libdir}/ocaml/stublibs/*
