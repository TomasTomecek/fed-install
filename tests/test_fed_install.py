import subprocess

"""
This test suite is meant to be executed in a Fedora 26 environment

go-srpm-macros is a good candidate for testing since it has zero dependencies
"""


def test_koji_build():
    build_nvr = 'units-2.14-1.fc27'
    build_nvra = build_nvr + '.x86_64'
    cmd = ["fed-install", "-y", "--enable-predefined-repos", "koji-build", build_nvr, "units"]
    subprocess.check_call(cmd)
    installed_package = subprocess.check_output(["rpm", "-q", "units"]).strip().decode()

    assert installed_package == build_nvra

    subprocess.check_call(["dnf", "-y", "remove", "units"])


def test_fedora_release():
    package_name = 'hardlink'
    cmd = ["fed-install", "-y", "fedora-release", "25", package_name]
    subprocess.check_call(cmd)
    installed_package = subprocess.check_output(["rpm", "-q", package_name]).strip().decode()

    assert "fc25" in installed_package

    subprocess.check_call(["dnf", "-y", "remove", package_name])
