Summary:	SDL binding for OCaml
Summary(pl):	Wi±zania SDL dla OCamla
Name:		ocaml-SDL
Version:	0.7.1
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/ocamlsdl/ocamlsdl-%{version}.tar.gz
# Source0-md5:	3829b20bd975e3bef5195a54e2cd04cb
URL:		http://ocamlsdl.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDLimage-devel
BuildRequires:	glut-devel
BuildRequires:	ocaml >= 3.07
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
%setup -q -n ocamlsdl

%build
%{__make} -C gl \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"
%{__make} -C hgl \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"
%{__make} -C glfw \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC" \
	X11LIBS="-L/usr/X11R6/%{_lib}"
%{__make} -C glut \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC" \
	X11LIBS="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{gl,stublibs}

install lib/*.cm[ixa]* lib/*.a $RPM_BUILD_ROOT%{_libdir}/ocaml/gl
install lib/dll*.so $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ocamlgl-gl
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ocamlgl-gl/META <<EOF
requires = "bigarray"
version = "%{version}"
directory = "+gl"
archive(byte) = "gl.cma"
archive(native) = "gl.cmxa"
linkopts = ""
EOF

for f in glut hgl glfw ; do
	install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ocamlgl-$f
	cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ocamlgl-$f/META <<EOF
requires = "ocamlgl-gl"
version = "%{version}"
directory = "+gl"
archive(byte) = "$f.cma"
archive(native) = "$f.cmxa"
linkopts = ""
EOF
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(644,root,root,755)
%doc LICENSE glfw/license.txt README Announce doc/*
%dir %{_libdir}/ocaml/gl
%{_libdir}/ocaml/gl/*.cm[ixa]*
%{_libdir}/ocaml/gl/*.a
%{_libdir}/ocaml/site-lib/*
%{_examplesdir}/%{name}-%{version}
