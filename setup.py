from setuptools import setup

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='Statistics',
    version='1.1',
    description='To find Mean,Meadian,Mode of the given numbers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['stats'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",

        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    url="https://github.com/Vishalkanna2001/statistics"
    author='Vishal Kanna AJK',
    author_email='vishalkanna.k@outlook.com'
)