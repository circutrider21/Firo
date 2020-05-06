import setuptools

with open("README.md", "r") as fh:
    longdescription = fh.read()

setuptools.setup(
    name="Firo", 
    version="1.2.1",
    author="Peeled Fruit Studios",
    author_email="Circutrider21@gmail.com",
    description="A Realtime, No SQL Database",
    long_description=longdescription,
    long_description_content_type="text/markdown",
    url="https://github.com/circutrider21/FiroDB",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
    ],
    python_requires='>=3.6',
)
