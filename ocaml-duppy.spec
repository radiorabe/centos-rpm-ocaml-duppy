Name:     ocaml-duppy

Version:  0.5.2
Release:  1
Summary:  OCAML duppy scheduler
License:  GPLv2+
URL:      https://github.com/chambart/ocaml-duppy
Source0:  https://github.com/savonet/ocaml-duppy/releases/download/0.5.2/ocaml-duppy-0.5.2.tar.gz

BuildRequires: ocaml
BuildRequires: pcre-ocaml
BuildRequires: ocaml-bytes
Requires:      pcre-ocaml
Requires:      ocaml-bytes

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
/usr/lib64/ocaml/duppy/libduppy_stubs.a
/usr/lib64/ocaml/duppy/pa_duppy.mli
/usr/lib64/ocaml/stublibs/dllduppy_stubs.so
/usr/lib64/ocaml/stublibs/dllduppy_stubs.so.owner

%description
OCaml asynchronous scheduler and monad for server-oriented programming.

%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-duppy.spec
