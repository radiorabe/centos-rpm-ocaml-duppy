Name:     ocaml-duppy
Version:  0.8.0
Release:  0.2
Summary:  OCAML duppy scheduler

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-duppy
Source0:  https://github.com/savonet/ocaml-duppy/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ssl
BuildRequires: ocaml-pcre-devel
Requires:      ocaml-pcre


%description
OCaml asynchronous scheduler and monad for server-oriented programming.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs

make install

%files
%doc README
%license COPYING
%{_libdir}/ocaml/%{libname}
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so.owner
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.8.0-0.2
- Cleanup and add seperate -devel subpackage

* Tue Nov 13 2018 Lucas Bickel <hairmare@rabe.ch> - 0.8.0-0.1
- Remove dropped caml4p support

* Tue Nov 13 2018 Lucas Bickel <hairmare@rabe.ch> - 0.8.0-0.0
- Bump to 0.8.0

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.7.4-0.0
- Bump to 0.7.4

* Sun Aug 19 2018 Lucas Bickel <hairmare@rabe.ch> 0.7.1-1
- Bump to 0.7.1
