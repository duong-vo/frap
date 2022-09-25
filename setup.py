from setuptools import setup, find_packages

setup(
    name='frap',
    packages=find_packages(),
    install_requires=[
        "click"
    ],
    versions='0.0.0',
    entry_points='''
    [console_scripts]
    frap=frap:frap
    '''
)