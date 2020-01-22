#! /usr/bin/bash

SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && cd .. && pwd)"
PARAMS=$@

podman run --rm -it -v $SRC_DIR:/fmlinfragit:z fmlinfragit:dev \
	bash -c "cd /fmlinfragit && tox $PARAMS"
