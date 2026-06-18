import re

from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("samplot/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

# Look for this section around line 12 and replace it with this:
try:
    with open("requirements.txt", "r") as f:
        requires = f.read().splitlines()
except FileNotFoundError:
    requires = []

setup(
    name="samplot-ic", # 1. Changed to your unique fork name
    version=version,   # Automatically reads "1.3.1" from your __init__.py!
    description="Samplot fork with InterChromosomal coordinate axis fixes", # 2. Updated description
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Jonathan Belyeu",
    author_email="jrbelyeu@gmail.com",
    url="https://github.com/ramyala/samplot", # 3. Optional: Points to your GitHub fork URL
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    package_data={"": ["LICENSE", "README.md"]},
    data_files=[("samplot", ["samplot/templates/samplot_vcf.html"])],
    include_package_data=True,
    install_requires=requires,
    license="MIT",
    zip_safe=False,
    # 4. Changed the command name to samplot-ic so users type your tool name to run it
    entry_points={"console_scripts": ["samplot-ic = samplot.__main__:main"]}, 
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)