Name:     ocaml-duppy

Version:  0.8.0
Release:  0.1
Summary:  OCAML duppy scheduler
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-duppy
Source0:  https://github.com/savonet/ocaml-duppy/releases/download/%{version}/ocaml-duppy-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ssl
BuildRequires: ocaml-pcre-devel
Requires:      ocaml-pcre

%prep
%setup -q 

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
/usr/lib64/ocaml/duppy/META
/usr/lib64/ocaml/duppy/duppy.a
/usr/lib64/ocaml/duppy/duppy.cma
/usr/lib64/ocaml/duppy/duppy.cmi
/usr/lib64/ocaml/duppy/duppy.cmx
/usr/lib64/ocaml/duppy/duppy.cmxa
/usr/lib64/ocaml/duppy/duppy.mli
/usr/lib64/ocaml/duppy/duppy_ssl.a
/usr/lib64/ocaml/duppy/duppy_ssl.cma
/usr/lib64/ocaml/duppy/duppy_ssl.cmi
/usr/lib64/ocaml/duppy/duppy_ssl.cmx
/usr/lib64/ocaml/duppy/duppy_ssl.cmxa
/usr/lib64/ocaml/duppy/libduppy_stubs.a
/usr/lib64/ocaml/stublibs/dllduppy_stubs.so
/usr/lib64/ocaml/stublibs/dllduppy_stubs.so.owner

%description
OCaml asynchronous scheduler and monad for server-oriented programming.

%changelog
* Tue Nov 13 2018 Lucas Bickel <hairmare@rabe.ch> - 0.8.0-0.1
- Remove dropped caml4p support

* Tue Nov 13 2018 Lucas Bickel <hairmare@rabe.ch> - 0.8.0-0.0
- Bump to 0.8.0

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.7.4-0.0
- Bump to 0.7.4

* Sun Aug 19 2018 Lucas Bickel <hairmare@rabe.ch> 0.7.1-1
- Bump to 0.7.1
