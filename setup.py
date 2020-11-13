from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = [ line for line in f.read().splitlines() if line ] # remove empty lines

setup(
        name="yomikatawa",
        version="1.0.0",
        author="tensorknower69",
        license="MIT",
        description="A python cli for https://yomikatawa.com",
        long_description="Please go to README.md in the GitHub page.",
        url="https://github.com/tensorknower69/yomikatawa",

        packages=find_packages(),
        install_requires=requirements,

        entry_points = {
            "console_scripts": [
                "yomikatawa = yomikatawa.run:main"
                ]
            }
        )
