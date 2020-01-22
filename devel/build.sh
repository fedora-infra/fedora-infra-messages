#! /usr/bin/bash

SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && cd .. && pwd)"

podman build --pull -t fmlinfragit:dev -v $SRC_DIR:/fmlinfragit:z --force-rm=true \
	-f devel/Dockerfile
