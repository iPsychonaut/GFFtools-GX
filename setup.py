from setuptools import setup, find_packages
import os

# Read the long description from the README file.
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="GFFtoolsGX",
    version="0.0.1",
    description="A collection of tools for converting genome annotation between GTF, BED, GenBank and GFF.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vipin T Sreedharan",
    author_email="vipin@cbio.mskcc.org",
    url="https://github.com/iPsychonaut/GFFtools-GX",
    packages=find_packages(),
    install_requires=[
        "biopython",
    ],
    entry_points={
        "console_scripts": [
            "gff_parser=GFFtoolsGX.GFFParser:main",
            "bed_to_gff=GFFtoolsGX.bed_to_gff:main",
            "gbk_to_gff=GFFtoolsGX.gbk_to_gff:main",
            "gff_to_bed=GFFtoolsGX.gff_to_bed:main",
            "gff_to_gtf=GFFtoolsGX.gff_to_gtf:main",
            "gtf_to_gff=GFFtoolsGX.gtf_to_gff:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
