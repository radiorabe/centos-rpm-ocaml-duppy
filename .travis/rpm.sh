#!/bin/bash
#
# RPM build wrapper for ocaml-duppy, runs inside the build container on travis-ci

set -xe

curl -o /etc/yum.repos.d/ocaml.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap:/ocaml/CentOS_8/home:radiorabe:liquidsoap:ocaml.repo"

dnf config-manager --set-disabled epel

chown root:root ocaml-duppy.spec

build-rpm-package.sh ocaml-duppy.spec
