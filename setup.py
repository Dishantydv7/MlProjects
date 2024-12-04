from setuptools import find_packages, setup
from typing import List

removeVar = '-e .'

def get_requirements(file_path: str) -> List[str]:
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()  # Read all lines, not just the first
        req = [x.strip() for x in req]  # Remove any leading/trailing whitespaces or newlines
        if removeVar in req:
            req.remove(removeVar)  # Remove the -e . line, as we don't need it here
    return req

setup(
    name="MyMlModel",
    version="0.1",
    author="Dishant Yadav",
    author_email="dishantrao11.code@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
