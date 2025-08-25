from setuptools import setup, find_packages

setup(
    name="genztranslator",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    description="A library to translate Gen Z slang into plain English",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Rohan S Sutar",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
