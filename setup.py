from setuptools import setup

# README for PyPi
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='loyverse',
      version='0.0.2',
      description='Loyverse API wrapper',
      url='https://github.com/matteobe/loyverse',
      packages=[
          'loyverse'
      ],
      python_requires='>3.7.0',
      install_requires=[
            'requests',
            'python-dotenv',
            'pandas',
      ],
      include_package_data=True,
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown'
      )
