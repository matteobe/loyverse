from setuptools import setup


setup(name='loyverse',
      version='0.0.1',
      description='Loyverse API wrapper',
      url='https://github.com/matteobe/loyverse',
      packages=[
          'loyverse'
      ],
      python_requires='>3.7.0',
      install_requires=[
            'requests',
            'pandas',
            'python-dotenv',
      ],
      include_package_data=True,
      zip_safe=False,
      )
