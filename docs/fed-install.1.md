% FED-INSTALL(1) Man Page
% Tomas Tomecek
% August 2017
# NAME
fed-install — install packages from specific Fedora releases or even from koji

# SYNOPSIS
**fed-install** [-h] [-v | -q] [-y] [--dnf-command DNF_COMMAND]
            [--enable-predefined-repos]
            {fedora-release,koji-tag,koji-build} ...

# DESCRIPTION
**fed-install** utilizes **dnf** to install selected packages. It usually
changes repository configuration via dnf using --enablerepo and --disablerepo
options. These are the sources you can install packages from:

 * koji tags
 * koji builds
 * stable Fedora releases

# OPTIONS
**-h**, **--help**
  Print help message.

**-v**, **--verbose**
  Output detailed information about current status (=debug logging).

**-q**, **--quiet**
  Output as few information as possible (=error logging).

**-y**, **--yes**
  Pass **-y** to dnf.

**--dnf-command DNF_COMMAND**
  Use selected dnf command (by default it's "install").

**--enable-predefined-repos**
  Do not pass "--disablerepo='\*'" to dnf.

# COMMANDS

**fed-install [options] fedora-release FEDORA_RELEASE PACKAGE [PACKAGE ...]**

  **--enable-updates-testing**
    Also enable 'updates-testing' repo.

**fed-install [options] koji-build BUILD_SPEC PACKAGE [PACKAGE ...]**

  **--arch ARCH**
    Architecture of packages to download in addition to noarch.

**fed-install [options] koji-tag KOJI_TAG PACKAGE [PACKAGE ...]**

  **--arch ARCH**
    Architecture of packages to download in addition to noarch.

# HISTORY
August 2017, Originally compiled by Tomas Tomecek
