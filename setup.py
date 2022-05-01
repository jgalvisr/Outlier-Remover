from setuptools import find_packages, setup
setup(
    name='outlremover',
    packages=find_packages(include=['outlremover']),
    version='0.1.0',
    description='Transforms outliers into nulls',
    author='Grupo maravilla',
    license='MIT',
    install_requires=['sklearn', 'numpy', 'pandas']
)