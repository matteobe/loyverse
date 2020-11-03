# Loyverse API wrapper

[![PyPi Latest Release](https://img.shields.io/pypi/v/loyverse)](https://img.shields.io/pypi/v/loyverse)
[![PyPI - Status](https://img.shields.io/pypi/status/loyverse)](https://img.shields.io/pypi/status/loyverse)
[![GitHub Release Date](https://img.shields.io/github/release-date/matteobe/loyverse)](https://img.shields.io/github/release-date/matteobe/loyverse)
[![Documentation Status](https://readthedocs.org/projects/loyverse/badge/?version=latest)](https://loyverse.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/github/license/matteobe/loyverse)](https://img.shields.io/github/license/matteobe/loyverse)
[![GitHub All Releases](https://img.shields.io/github/downloads/matteobe/loyverse/total)](https://img.shields.io/github/downloads/matteobe/loyverse/total)

The loyverse package provides a wrapper around the Loyverse API (v1.0).

Currently the package implements the following endpoints:
* Customers
* Receipts

## Getting started


### Setup
#### Documentation
After cloning into the repository, the user can compile the documentation using the following terminal commands:
```bash
cd docs
make html
```
To view the documentation, open the following [file](docs/build/html/index.html).

#### Secrets
The API needs access to the following environment variables to work:
* LOYVERSE_ACCESS_TOKEN: access token as defined on the Loyverse Website

These environment variables can be pre-defined in a an .env file that can be loaded using the python-dotenv package.
