FROM fedora:26

LABEL maintainer="Tomas Tomecek <tomas@tomecek.net>"

RUN dnf install -y make python3-pytest createrepo_c koji

ENV PYTHONDONTWRITEBYTECODE=YES

ENV LANG=en_US.utf8 \
    LC_ALL=en_US.UTF-8

RUN ln -s /src/fed-install /usr/bin/fed-install

WORKDIR /src

COPY . /src
