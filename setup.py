from setuptools import setup, find_packages

setup(
    name='frap',
    packages=find_packages(),
    description=""" The description of the package   """,
    long_description_content_type="text/markdown",
    install_requires=[
        "click"
    ],
    versions='0.0.0',
    entry_points='''
    [console_scripts]
    frap=frap:frap
    '''
)