from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="calculator_91",
    version="0.0.1",
    author="Eduardo",
    author_email="eduardo@gmail.com",
    description="Calcula simples numeros",
    long_description=page_description,
    long_description_content_type="calculator",
    url="https://github.com/EduardoHonda/package-template"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
