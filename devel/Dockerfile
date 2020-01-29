FROM registry.fedoraproject.org/fedora:31
LABEL maintainer="Randy Barlow <bowlofeggs@fedoraproject.org>"

RUN dnf install -y gcc make python3.6 python3.8 python3-pip
RUN pip install tox
# This way we can cache all the build dependencies
RUN cd /fmlinfragit && tox

CMD ["bash"]
