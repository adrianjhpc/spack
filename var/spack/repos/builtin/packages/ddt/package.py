# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ddt(Package):
    """Arm DDT is the number one debugger in research, industry, and academia
    for software engineers and scientists developing C++, C, Fortran parallel
    and threaded applications on CPUs, GPUs, Intel and Arm. Arm DDT is trusted
    as a powerful tool for automatic detection of memory bugs and divergent
    behavior to achieve lightning-fast performance at all scales."""

    homepage = "https://arm.com"
    url = "https://downloads.linaroforge.com/22.1.3/arm-forge-22.1.3-linux-x86_64.tar"

    maintainers("robgics")

    license_required = True
    license_files = ["./licences/ddt.lic"]

    # Versions before 22.0 have a security vulnerability. Do not install them.
    version("22.1.3", sha256="4f8a8b1df6ad712e89c82eedf4bd85b93b57b3c8d5b37d13480ff058fa8f4467")
    version(
        "22.0.2",
        sha256="3db0c3993d1db617f850c48d25c9239f06a018c895ea305786a7ad836a44496d",
        deprecated=True,
    )

    def setup_run_environment(self, env):
        env.prepend_path("PATH", join_path(self.prefix, "bin"))

    def install(self, spec, prefix):
        install_shell = which("sh")
        args = ["./textinstall.sh", "--accept-license", prefix]
        install_shell(*args)
