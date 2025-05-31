import os
import shutil


def remove_path(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


# Conditions based on user input
if "{{ cookiecutter.include_docker }}" != "y":
    remove_path("Dockerfile")
    remove_path("docker-compose.yml")

if "{{ cookiecutter.use_dvc }}" != "y":
    remove_path("dvc.yaml")
    remove_path(".dvcignore")
    remove_path("data")

if "{{ cookiecutter.include_fastapi }}" != "y":
    remove_path("api")

if "{{ cookiecutter.include_monitoring }}" != "y":
    remove_path("monitoring")

if "{{ cookiecutter.include_publication }}" != "y":
    remove_path("paper")

if "{{ cookiecutter.include_cloud }}" != "y":
    remove_path("infra")

if "{{ cookiecutter.include_stakeholder_material }}" != "y":
    remove_path("pitch")
    remove_path("reports/final")

if "{{ cookiecutter.include_mlflow }}" != "y":
    remove_path("mlruns")


license_map = {
    "MIT": "MIT.txt",
    "Apache-2.0": "Apache-2.0.txt",
    "Proprietary": "Proprietary.txt",
}

selected = "{{ cookiecutter.license }}"
license_file = license_map.get(selected)

if license_file:
    shutil.copyfile(
        os.path.join("licenses", license_file),
        "LICENSE"
    )
    # Remove the licenses directory afterwards if desired
    shutil.rmtree("licenses", ignore_errors=True)


def rename_or_remove(src_folder, dest_folder):
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
    if os.path.exists(src_folder):
        shutil.move(src_folder, dest_folder)


include_docs = "{{ cookiecutter.include_docs }}"

if include_docs == "mkdocs":
    rename_or_remove("sphinx_docs", "docs")  # remove sphinx_docs if exists
    rename_or_remove("mkdocs_docs", "docs")  # rename mkdocs_docs to docs
elif include_docs == "sphinx":
    rename_or_remove("mkdocs_docs", "docs")  # remove mkdocs_docs if exists
    rename_or_remove("sphinx_docs", "docs")  # rename sphinx_docs to docs
else:  # none
    # remove all docs folders
    for d in ["docs", "mkdocs_docs", "sphinx_docs"]:
        if os.path.exists(d):
            shutil.rmtree(d)
