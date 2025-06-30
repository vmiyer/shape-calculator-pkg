# setup.py
from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="shape-calculator-pkg", # This is the name your package will be installed as
    version="0.1.0",
    author="Your Name", # Replace with your name
    author_email="your.email@example.com", # Replace with your email
    description="A simple Python package to calculate area and perimeter of geometric shapes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/shape-calculator-pkg", # Replace with your GitHub repo URL
    packages=find_packages(), # This will automatically find your 'shape_calculator' package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires='>=3.6',
    install_requires=[], # Add any dependencies your package needs, e.g., ['numpy']
)