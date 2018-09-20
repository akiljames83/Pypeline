from setuptools import setup

setup(
    name = "Pypeline",
    url = "https://github.com/akiljames83/Pypeline",
    version = "0.1.0",
    packages = find_packages(),
    install_requires = ['docutils>=0.3','heapq'],

    # metadata for upload to PyPI
    author = "Akil Hamilton",
    author_email = "akil.james83@gmail.com",
    description = "This is a package which will allow for easy implementation of basic Data Structures.",
    license = "PSF",
    keywords = "data structures implementation"
)