from setuptools import find_packages, setup

setup(
    name="words",
    version="1.0.0",
    description="helper library for random words",
    package_dir={"": "src"},
    packages=find_packages(where="src")
)