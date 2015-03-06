from setuptools import setup, find_packages

setup(name='nose-lock',
      version='0.1.0',
      author='Alxander Artemenko',
      author_email='svetlyak.40wt@gmail.com',
      description=('A plugin for python-nose which locks test execution '
                   'and doesn\'t allow to run them in parallel '
                   'from two terminals.'),
      long_description=open('README.md').read(),
      packages=find_packages(),
      install_requires=['lockfile>=0.10,<0.11'],
      entry_points = {
          'nose.plugins.0.10': [
              'lock = nose_lock:NoseLock'
          ]
      })
