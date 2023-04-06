#!/usr/bin/env python

import io
import os

import setuptools

dependencies = [
    "Click>=8.0",
]

# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

# Only include packages under the 'hfrschmidt_test_project' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package
    for package in setuptools.find_packages()
    if package.startswith("hfrschmidt_test_project")
]

# Determine which namespaces are needed, when namespaced packages are supposed to be used
# namespaces = ["hfrschmidt_test_project"]
# if "hfrschmidt_test_project.<namespace>" in packages:
#     namespaces.append("hfrschmidt_test_project.<namespace>")

setuptools.setup(
    name="hfrschmidt_test_project",
    version="0.1.0",
    description="An awesome test project",
    long_description=readme,
    author="Hendrik F.R. Schmidt",
    author_email="h@fr.s",
    license="MIT",
    url="https://github.com/hfrSchmidt/hfrschmidt_test_project",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Systems Administration",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=packages,
    # namespace_packages=namespaces,
    install_requires=dependencies,
    entry_points={
        "console_scripts": [
            "hfrschmidt_test_project=hfrschmidt_test_project.cli:main",
        ],
    },
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)
