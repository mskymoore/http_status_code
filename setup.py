import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="http-status-code",
    version="0.0.1",
    author="Muhammad Samer Sallam",
    author_email="samersallam92@gmail.com",
    license='MIT',
    description="This module contains a simple library with a single class to define HTTP status codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Samer92/http_status_code",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    platform=['Any'],
    python_requires='>=3.6',
)