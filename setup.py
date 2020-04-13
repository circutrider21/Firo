import setuptools

with open("README.md", "r") as fh:
    longdescription = fh.read()

setuptools.setup(
    name="Firo", 
    version="1.1.4",
    author="Peeled Fruit Studios",
    author_email="Circutrider21@gmail.com",
    description="A Database That stores and gets values simply",
    long_description=longdescription,
    long_description_content_type="text/markdown",
    url="https://github.com/circutrider21/FiroDB",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
