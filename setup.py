import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitandpip",
    version="0.0.1",
    author="Shruthi Rajasekar",
    description="pip installable",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
)