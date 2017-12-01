% FED-INSTALL(1) Man Page
% Tomas Tomecek
% December 2017
# NAME
fed-install — install packages from specific Fedora releases or even from koji

# SYNOPSIS
**fed-install** [-h] [-v | -q] [-y] [--dnf-command DNF_COMMAND]
            [--enable-predefined-repos] [--dnf-options DNF_OPTIONS]
            [--disable-dnf-excludes]
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

**--dnf-options DNF_OPTIONS**
  Invalidate default dnf options and use your own.

**--disable-dnf-excludes**
  Passes '--disableexcludes=all' to dnf: the options disables excludes you may
  have specified in dnf.conf.

# COMMANDS

**fed-install** [options] from-release
            [--enable-updates-testing]
            FEDORA_RELEASE
            PACKAGE [PACKAGE ...]

  **FEDORA_RELEASE**
    Numerical identification of selected Fedora release, e.g. 27.

  **PACKAGE**
    Name of package to install.

  **--enable-updates-testing**
    Also enable 'updates-testing' repo.

**fed-install** [options] koji-build
            [--arch ARCH [ARCH ...]] [--preserve-downloaded]
            BUILD_SPEC
            PACKAGE [PACKAGE ...]

  **BUILD_SPEC**
    <n-v-r | build_id | package>, see `koji download-build -h`

  **PACKAGE**
    Name of package to install.

  **--arch ARCH [ARCH ...]**
    Architectures of packages to download in addition to noarch, pick more for multilib

  **--preserve-downloaded**
    Preserve downloaded packages (by default they are removed)

**fed-install** [options] koji-tag
            [--arch ARCH [ARCH ...]]
            KOJI_TAG
            PACKAGE [PACKAGE ...]

  **KOJI_TAG**
    name of koji tag, see `koji list-tags`

  **PACKAGE**
    Name of package to install.

  **--arch ARCH**
    Architectures of binary packages to select (this accepts multiple values so
    you can do multilib).


# HISTORY
December 2017, Originally compiled by Tomas Tomecek
