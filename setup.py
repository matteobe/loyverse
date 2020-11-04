from os import path
from setuptools import setup

# Project
NAME = 'loyverse'
VERSION = '0.1.0'

# Maintainer
MAINTAINER = 'Matteo Berchier'
MAINTAINER_EMAIL = 'maberchier@gmail.com'

# Long description
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# License
LICENSE = 'MIT'

# Project URLs
REPOSITORY = 'https://github.com/matteobe/loyverse'
HOMEPAGE = 'https://loyverse.readthedocs.io'
PROJECT_URLS = {
    'Bug Tracker': f'{REPOSITORY}/issues',
    'Documentation': 'https://loyverse.readthedocs.io',
    'Source Code': REPOSITORY,
}
DOWNLOAD_URL = ''

# Classifiers
CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: Console",
    "Operating System :: OS Independent",
    "Intended Audience:: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.7",
]

# Package definition
setup(name=NAME,
      version=VERSION,
      description='Loyverse API wrapper',
      url=HOMEPAGE,
      packages=[
          'loyverse',
      ],
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      license=LICENSE,
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      download_url=DOWNLOAD_URL,
      project_urls=PROJECT_URLS,
      python_requires='>3.7.0',
      install_requires=[
          'requests',
          'python-dotenv',
          'pandas',
      ],
      include_package_data=True,
      zip_safe=False,
      )
