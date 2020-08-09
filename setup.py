import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="downcast", # Replace with your own username
    version="0.0.7",
    author="dky",
    author_email="dky.united@gmail.com",
    description="Reduce the pandas dataframe size automatically.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepak7376/downcast",
    py_modules=["downcast"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)