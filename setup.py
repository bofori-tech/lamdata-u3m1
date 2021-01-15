from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-helper-name", # the name that you will install via pip
    version="1.0",
    author="Bryt O",
    author_email="sharpko@yahoo.com",
    description="helpful functions",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/bofori-tech/lamdata-u3m1",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)