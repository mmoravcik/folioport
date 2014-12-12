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
      # TODO make this less greedy nom nom
      install_requires=[
          'django==1.6.6',
          'pillow==2.4.0',
          'South==0.7.6',
          'sorl-thumbnail==11.12.1b',
          'django-mptt==0.5.5',
          'django-tagging==0.3.1',
          'django-disqus==0.4.1',
          'django-ckeditor-updated==4.2.8',
          'django-dynamic-fixture',
          'django-my-css==0.1.2',
          'django-crispy-forms',
          'django-endless-pagination==2.0',
          ],
      dependency_links = ['https://github.com/mmoravcik/django-my-css/tarball/0.1.2#egg=django-my-css-0.1.2'],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python']
      )
