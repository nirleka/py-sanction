import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()

requires = ["coverage",
    "nose",
    "nose-cov",
    "pyopenssl",
    "sphinx"]

setup(name="sanction",
    version="0.9-alpha-1",
    description="",
    author="Demian Brecht",
    author_email="demianbrecht@gmail.com",
    url="",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration :: Authentication/Directory"
    ],
    long_description=README,
    install_requires=requires
)
