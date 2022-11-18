import pathlib

from setuptools import setup

README = (pathlib.Path(__file__).resolve().parent / "README.md").read_text()

setup(
    name="python-summer-boot",
    version="1.0.5",
    description="After spring it comes the summer.",
    python_requires=">=3.8",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Joan Travé",
    author_email="jtravegordillo@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    package_dir={
        "summer": "summer",
    },
    packages=["summer.inversion_of_control", "summer.models"],
    include_package_data=True,
    install_requires=["pydantic"],
    entry_points={},
    project_urls={
        "Source": "https://github.com/joanTrave/summer-boot",
    },
)
