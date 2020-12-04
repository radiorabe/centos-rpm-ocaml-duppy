Name:     ocaml-duppy
Version:  0.9.0
Release:  0.1%{?dist}
Summary:  OCAML duppy scheduler

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-duppy
Source0:  https://github.com/savonet/ocaml-duppy/archive/v%{version}.tar.gz?#%{name}-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-dune
BuildRequires: ocaml-ssl
BuildRequires: ocaml-pcre-devel <= 7.2.3-0.1.2.rabe
#Requires:      ocaml-pcre


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
dune build

%install
dune install \
  --prefix %{buildroot} \
  --libdir %{buildroot}$(ocamlfind printconf destdir)
rm -rf %{buildroot}/doc


%files
%doc README.md CHANGES
%license COPYING
%{_libdir}/ocaml/%{libname}
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so
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
* Thu Dec 3 2020 Lucas Bickel <hairmare@rabe.ch> - 0.9.0-0.1
- Bump to 0.9.0

* Sun Oct 20 2019 Lucas Bickel <hairmare@rabe.ch> - 0.8.1-0.1
- Bump to 0.8.1

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
