from setuptools import setup, find_packages
import os

PROJECT_DIR = os.path.dirname(__file__)


setup(name='djangocms-oscar',
      version='0.1',
      #url='https://github.com/tangentlabs/django-oscar',
      author="Maik Hoepfel",
      author_email="maik.hoepfel@tangentlabs.co.uk",
      description="django CMS plugin for Oscar",
      long_description=open(os.path.join(PROJECT_DIR, 'README.rst')).read(),
      license='BSD',
      platforms=['linux'],
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'django-cms>=3.0.2',
          'django-oscar>=0.7.1',
      ],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: WWW/HTTP']
)