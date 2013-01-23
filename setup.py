from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='mappapp',
      version=version,
      description="myapp",
      long_description="""\
my app for scilifelab python course""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python course',
      author='Anders Gabrielsson',
      author_email='anders.gabrielsson@scilifelab.se',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
