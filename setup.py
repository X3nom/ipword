from setuptools import setup, find_packages


def load_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name="ipword-tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=load_requirements(),
    entry_points={
        "console_scripts": [
            "ipword=ipword_tool.ipword:main",  # Register the CLI tool
        ]
    },
    package_data={
        "ipword-tool": ["hex-word-dict.pickle"],
    },
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
