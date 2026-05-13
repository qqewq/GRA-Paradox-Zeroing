from setuptools import setup, find_packages

setup(
    name="gra-paradox-zeroing",
    version="0.1.0",
    author="Oleg Bits",
    description="GRA Bulldozer: active paradox generation + adversarial zeroing for AGI landscapes",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/qqewq/GRA-Paradox-Zeroing",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21",
        "scipy>=1.7",
        "matplotlib>=3.4",
        "streamlit>=1.12",
        "plotly>=5.5",
        "pytest>=6.0",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
