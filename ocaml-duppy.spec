Name:     ocaml-duppy

Version:  0.7.0
Release:  1
Summary:  OCAML duppy scheduler
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-duppy
Source0:  https://github.com/savonet/ocaml-duppy/releases/download/%{version}/ocaml-duppy-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: pcre-ocaml
BuildRequires: ocaml-camlp4
BuildRequires: ocaml-camlp4-devel
Requires:      pcre-ocaml

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
/usr/lib64/ocaml/duppy/duppy_ssl.mli
/usr/lib64/ocaml/duppy/libduppy_stubs.a
/usr/lib64/ocaml/duppy/pa_duppy.mli
/usr/lib64/ocaml/stublibs/dllduppy_stubs.so
/usr/lib64/ocaml/stublibs/dllduppy_stubs.so.owner
/usr/lib64/ocaml/duppy/duppy_secure_transport.mli
/usr/lib64/ocaml/duppy/pa_duppy.cmi
/usr/lib64/ocaml/duppy/pa_duppy.cmo

%description
OCaml asynchronous scheduler and monad for server-oriented programming.

%changelog
* Fri Apr 14 2017 Lucas Bickel <hairmare@rabe.ch>
- Bump version to 0.6.0

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-duppy.spec
