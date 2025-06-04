# setup.py
{% if cookiecutter.dependency_manager == 'requirements' %}
from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_slug.replace('-', '_') }}",
    version="{{ cookiecutter.version }}",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
{% endif %}
