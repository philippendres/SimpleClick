from setuptools import setup, find_packages

setup(
    name="isegm",
    version="1.0.0",
    packages=["isegm/"] + find_packages(),
    url="",
    author="Qin Liu",
    include_package_data=True,
    zip_safe=False,
)