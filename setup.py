###############################################################################
# Copyright 2013-2019 University of Florida. All rights reserved.
# This file is part of the DChecker project.
# Use of this source code is governed by the license found in LICENSE.txt.
###############################################################################

from setuptools import setup

from dchecker import VERSION

setup(
    name="dchecker",
    version=VERSION,
    py_modules=["dchecker"],

    description="Data integrity checker for VIVO",
    long_description=open("README.md").read(),

    author="Taeber Rapczak",
    author_email="taeber@ufl.edu",

    maintainer="UF CTS-IT",
    maintainer_email="ctsit@ctsi.ufl.edu",

    url="https://github.com/ctsit/dchecker",
    download_url="https://github.com/ctsit/dchecker/releases/tag/" + VERSION,
    keywords=["VIVO", "data integrity", "SPARQL"],
    license="MIT",

    entry_points={
        "console_scripts": [
            "dchecker = dchecker:main"
        ]
    },

    python_requires=">=3.6.0",
)
