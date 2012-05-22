#!/usr/bin/env python
"""
Installation script:
"""

from setuptools import setup, find_packages

from folioport import get_version


setup(name='folioport',
      version=get_version().replace(' ', '-'),
      url='https://github.com/mmoravcik/folioport',
      author="Matus Moravcik",
      author_email="matus.moravcik@tangentlabs.co.uk",
      description="Simple portfolio app for Django 1.3+",
      long_description="",
      keywords="portfolio, gallery, showcase",
      license='BSD',
      platforms=['linux'],
      packages=find_packages(exclude=["sandbox*", "tests*"]),
      include_package_data=True,
      install_requires=[
          'django==1.4',
          'PIL==1.1.7',
          'South==0.7.3',
          'sorl-thumbnail==11.12',
          'django-mptt',
          ],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python']
      )