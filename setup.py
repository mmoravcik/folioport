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
      author_email="matus.moravcik@gmail.com",
      description="Simple portfolio app",
      long_description=open('README.rst').read(),
      keywords="portfolio, gallery, showcase",
      license='BSD',
      platforms=['linux'],
      packages=find_packages(exclude=["sandbox*", "tests*"]),
      include_package_data=True,
      install_requires=[
          'django==1.5.1',
          'PIL==1.1.7',
          'South==0.7.6',
          'sorl-thumbnail==11.12',
          'django-mptt==0.5.5',
          'django-ratings==0.3.7',
          'django-tagging==0.3.1',
          'django-disqus==0.4.1',
          ],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python']
      )
