import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xrayreader",
    version="0.0.1",
    author="TB",
    author_email="author@example.com",
    description="A x ray metadata reader package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git@github.com:tb-brics/dorothy-data-reader.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8.5",
    ],
    python_requires='>=3.6',
)
