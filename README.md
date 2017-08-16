# fed-install

Install packages from specific Fedora releases or even from koji.

This tool is using dnf, this is not a new package manager.


## Installation

fed-install requires these packages to be present on your system:

```
koji
createrepo_c
dnf
python3
```

At some point, I will package fed-install as an RPM so these dependencies will
be handled automatically.


## Features


### Install packages from koji tags or koji builds.

Install selected package, in this case `docker`, from a specific koji build:
```
$ ./fed-install koji-build docker-1.13.1-20.git27e468e.fc27 docker
```

You can easily check what packages are present in a specific koji tag:
```
$ koji list-tagged f27 kernel
Build                                     Tag                   Built by
----------------------------------------  --------------------  ----------------
kernel-4.12.0-0.rc2.git0.1.fc27           f27                   jforbes
kernel-4.12.0-0.rc2.git1.1.fc27           f27                   jforbes
kernel-4.12.0-0.rc2.git2.1.fc27           f27                   jforbes
```

or what's a latest build of a specific package:
```
$ koji latest-build f27 docker
Build                                     Tag                   Built by
----------------------------------------  --------------------  ----------------
docker-1.13.1-26.gitb5e3294.fc27          f27                   lsm5
```

This is how I recently reinstalled a package which is not available in respositories anymore:
```
$ ./fed-install --dnf-command=reinstall koji-build $(rpm -q docker) docker
```


### Install a package from a selected Fedora release.

Do you need a newer build?

```
$ ./fed-install fedora-release 26 docker
```

or an older, stable build?

```
$ ./fed-install fedora-release 25 docker
```

or the newest build?

```
$ ./fed-install koji-tag rawhide docker
```


### If you are on rawhide, easily install a kernel from stable Fedora release.

This is how you can install latest kernel from Fedora 26:

```
$ ./fed-install --dnf-command=update fedora-release 26 kernel
```


## TODO

* RPM packaging
* python packaging
* unit tests
