Summary:	SDL binding for OCaml
Summary(pl):	Wi±zania SDL dla OCamla
Name:		ocaml-SDL
Version:	0.7.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/ocamlsdl/ocamlsdl-%{version}.tar.gz
# Source0-md5:	3829b20bd975e3bef5195a54e2cd04cb
URL:		http://ocamlsdl.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_image-devel
BuildRequires:	ocaml >= 3.07
BuildRequires:	ocaml-lablgl-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simply speaking, OCamlSDL is an attempt to write a software interface
between the ML programming language and the SDL C library.

This package contains files needed to run bytecode executables using
this library.

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
	DESTDIR=$RPM_BUILD_ROOT		

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
%attr(755, root, root) %{_libdir}/ocaml/stublibs/*
