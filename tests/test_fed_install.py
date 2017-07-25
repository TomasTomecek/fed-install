import subprocess


def test_koji_build():
    build_nvr = 'units-2.14-1.fc27'
    build_nvra = build_nvr + '.x86_64'
    cmd = ["fed-install", "-y", "--enable-predefined-repos", "koji-build", build_nvr, "units"]
    subprocess.check_call(cmd)
    installed_package = subprocess.check_output(["rpm", "-q", "units"]).strip().decode()

    assert installed_package == build_nvra
