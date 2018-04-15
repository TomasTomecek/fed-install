"""
This test suite is meant to be executed in a Fedora 27 environment

go-srpm-macros is a good candidate for testing since it has zero dependencies
"""

import subprocess


def test_koji_build():
    build_nvr = 'units-2.14-5.fc27'
    build_nvra = build_nvr + '.x86_64'
    cmd = ["fed-install", "-y", "-v", "--enable-predefined-repos", "koji-build", build_nvr, "units"]
    try:
        subprocess.check_call(cmd)
        installed_package = subprocess.check_output(["rpm", "-q", "units"]).strip().decode()
        assert installed_package == build_nvra
    finally:
        subprocess.call(["dnf", "-y", "remove", "units"])


def test_fedora_release():
    package_name = 'hardlink'
    cmd = ["fed-install", "-y", "-v", "from-release", "26", package_name]
    try:
        subprocess.check_call(cmd)
        installed_package = subprocess.check_output(["rpm", "-q", package_name]).strip().decode()
        assert "fc26" in installed_package
    finally:
        subprocess.check_call(["dnf", "-y", "remove", package_name])


def test_fedora_tag():
    package_name = 'hardlink'
    cmd = ["fed-install", "-y", "-v", "koji-tag", "f26-build", package_name]
    try:
        subprocess.check_call(cmd)
        installed_package = subprocess.check_output(["rpm", "-q", package_name]).strip().decode()
        assert "fc26" in installed_package
    finally:
        subprocess.check_call(["dnf", "-y", "remove", package_name])
