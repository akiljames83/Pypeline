from setuptools import setup

setup(
    name = "python-pypeline",
    url = "https://github.com/akiljames83/Pypeline",
    version = "1.0.1",
    install_requires = ['docutils>=0.3','numpy>=0.1'],

    # metadata for upload to PyPI
    author = "Akil Hamilton",
    packages=['Pypeline', 'Pypeline.Pypes'],
    author_email = "akil.james83@gmail.com",
    description = "This is a package which will allow for easy implementation of basic Data Structures.",
    license = "MIT",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords = "data structures implementation"
)