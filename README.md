# Firo

![PyPI](https://img.shields.io/pypi/v/Firo?color=brightgreen) - ![License](https://img.shields.io/pypi/l/Firo?color=red) - ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Firo?color=brightgreen)

Firo is a small and efficient database system for python programs that eases learning to use a database for begenners at programing

Firo is also very functional and can be used in professional application due to the fact that it is very robust and functional

## Usage

Below is a simple example that shows how to use Firo

```` python

from Firo import FiroDB

con = FiroDB.Start("data.db")

con.set("msg", "Hello")

print(con.get("msg"))

````

## Installation

There are 2 ways to install this application

#### Method 1 | Ofline installation

1. Install the latest version of Firo from the releases tab

2. install with this command

```` bash

$ pip install Firo-1.1.2.whl

````

#### Method 2 | Online Installation

1. Install The latest version of Firo from PyPi With this command

```` bash

$ pip install Firo

````

### What's New

- Fixed a glitch that returned an array instad of a singular sting

- Created readme

- Added a remove function and fixed a bug that returned tuple instad of string
