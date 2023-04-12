from setuptools import setup, find_packages

setup(
    name="cooltest",
    version="19.0",
    author="Halyna",
    author_email="firstmy555@gmail.com",
    packages=find_packages(),
    description="Interface library for minimalist autograding site",
    python_requires=">=3.5",
    url="https://github.com/mehalyna/cooltest.git",
    install_requires=["numpy >= 1.15"],
    zip_safe=False,
    setup_requires=["numpy >= 1.15"]
)
