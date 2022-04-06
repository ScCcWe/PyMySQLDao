# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: setup.py.py
# author: ScCcWe
# time: 2022/3/6 11:34 下午
# import os
import setuptools

with open("./README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version_str = "0.0.9"


def get_install_requires():
    install_requires = ["PyMySQL", "pydantic"]

    # if os.name == "nt":  # Windows
    #     install_requires.append("")

    return install_requires


setuptools.setup(
    name="pymysql_dao",
    version=version_str,
    author="ScCcWe",
    author_email="scccwe@163.com",
    description="A functional enhancement package that focus on crud based PyMySQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ScCcWe/PyMySQLDao",
    project_urls={
        "Bug Tracker": "https://github.com/ScCcWe/PyMySQLDao/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir={"": "pymysqldao"},
    # packages=setuptools.find_packages(where="pymysqldao", exclude=["tests*"]),
    packages=setuptools.find_packages(exclude=["tests*"]),
    install_requires=get_install_requires(),
    python_requires=">=3.7",
)
