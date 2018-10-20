from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(name='example_pybr',
      version='0.2',
      description='Example of a simple Python package',
      url='http://github.com/deboraazevedo/example_pybr',
      author='Debora Azevedo',
      author_email='deboraazevedo@gmail.com',
      long_description=long_description,
      license='MIT',
      packages=['example_pybr'],
      zip_safe=False)
