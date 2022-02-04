from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='graph_profile',
    url='https://github.com/pashenkogleb/graph_profile',
    author='Gleb Pashchenko',
    author_email='pashenkogleb@gmail.com',
    # Needed to actually package something
    packages=find_packages(),
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='creates call graph',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)