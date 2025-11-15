"""
Setup configuration for webl CLI tool
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="webl",
    version="0.2.0",
    author="Website Launches",
    author_email="support@websitelaunches.com",
    description="Command-line tool for domain intelligence and authority lookups",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/websitelaunches/webl-cli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "click>=8.0.0",
        "requests>=2.28.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "webl=webl.cli:main",
        ],
    },
)
