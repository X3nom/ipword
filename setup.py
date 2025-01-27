from setuptools import setup, find_packages

setup(
    name="ipword-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "ipword=ipword.ipword:main",  # Register the CLI tool
        ]
    },
    package_data={
        "tool_src": ["hex-word-dict.pickle"],
    },
    include_package_data=True, 
    include_package_data=True,
    description="Simple CLI tool for conversion of ipv6 addresses to more human-readable format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="X3nom",
    url="https://github.com/X3nom/ipword",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
