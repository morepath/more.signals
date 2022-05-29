"""
more.signals
------------
Signals for Morepath.
"""

from setuptools import setup, find_packages


def read_md(f):
    return open(f, encoding="utf-8").read()


version = "0.2.0.dev0"
long_description = "\n".join((read_md("README.md"), read_md("CHANGES.md")))
install_requires = ["morepath", "blinker"]
tests_require = ["pytest", "coverage", "pytest-cov", "webtest"]
docs_require = ["sphinx", "docutils"]
pypi_require = ["twine"]


setup(
    name="more.signals",
    version=version,
    url="https://github.com/morepath/more.signals",
    license="BSD",
    author="Blaise Laflamme",
    author_email="blaise@laflamme.org",
    description="Signals for Morepath",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="morepath events signals blinker",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    namespace_packages=["more"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require, "docs": docs_require, "pypi": pypi_require},
)
