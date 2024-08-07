from setuptools import setup, find_packages

setup(
    name='marketing_tool',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
        'nltk',
    ],
)
