% FED-INSTALL(1) Man Page
% Tomas Tomecek
% August 2017
# NAME
fed-install — install RPM packages from well-known repositories

# SYNOPSIS
**fed-install** [OPTIONS] COMMAND [arg...]
  {fedora-release,koji-tag,koji-build}

# DESCRIPTION
**fed-install** utilizes **dnf** to install selected packages. It usually
changes repository configuration via dnf using --enablerepo and --disablerepo
options. The well-known repositories are:

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



# HISTORY
August 2017, Originally compiled by Tomas Tomecek
