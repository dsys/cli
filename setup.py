import sys, os
from setuptools import setup, find_packages

version = "0.0.1"

base_reqs = []

setup(
       name="pavlovcli",
       description="interact with your pavlov models and create new ones from the command line",
       classifiers=["Programming Language :: Python :: 2.7"],
       keywords="pavlovml pavlov machine learning deep",
       author="Zain Shah",
       author_email="zan2434@gmail.com",
       url="http://github.com/pavlovml/cli",
       license="BSD-3",
       version=version,
       packages=find_packages(),
       install_requires=base_reqs,
       entry_points={"console_scripts":["pavlov = pavlov.train:main"]}
)
