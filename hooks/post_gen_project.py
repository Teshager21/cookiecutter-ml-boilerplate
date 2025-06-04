import os
import shutil


def remove_path(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


# --- Conditional Cleanup Based on User Inputs ---

if "{{ cookiecutter.include_docker }}" != "y":
    remove_path("Dockerfile")
    remove_path("docker-compose.yml")

if "{{ cookiecutter.use_dvc }}" != "y":
    remove_path("dvc.yaml")
    remove_path(".dvcignore")
    # remove_path("data")

if "{{ cookiecutter.include_fastapi }}" != "y":
    remove_path("api")

if "{{ cookiecutter.include_api }}" != "y":
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

if "{{ cookiecutter.include_serving }}" != "y":
    remove_path("serving")
    remove_path("Dockerfile.serving")  # ✅ Remove the specific serving Dockerfile

if "{{ cookiecutter.include_edge_deployment }}" != "y":
    remove_path("edge")

if "{{ cookiecutter.include_infra }}" == "n":
    remove_path("infra")

if "{{ cookiecutter.include_experiments }}" != "y":
    remove_path("experiments")

if "{{ cookiecutter.include_paper }}" != "y":
    remove_path("paper")

if "{{ cookiecutter.include_demo }}" != "y":
    remove_path("demo")

if "{{ cookiecutter.include_audit }}" != "y":
    remove_path("audit")

if "{{ cookiecutter.include_contracts }}" != "y":
    remove_path("contracts")

if "{{ cookiecutter.include_references }}" != "y":
    remove_path("references")

# Clean up empty reports folder if needed
reports_dir = "reports"
if os.path.exists(reports_dir) and not os.listdir(reports_dir):
    remove_path(reports_dir)


# --- License File Handling ---

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
    shutil.rmtree("licenses", ignore_errors=True)


# --- Documentation Engine Selection ---

def rename_or_remove(src_folder, dest_folder):
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
    if os.path.exists(src_folder):
        shutil.move(src_folder, dest_folder)


include_docs = "{{ cookiecutter.include_docs }}"

if include_docs == "mkdocs":
    rename_or_remove("sphinx_docs", "docs")
    rename_or_remove("mkdocs_docs", "docs")
elif include_docs == "sphinx":
    rename_or_remove("mkdocs_docs", "docs")
    rename_or_remove("sphinx_docs", "docs")
else:
    for d in ["docs", "mkdocs_docs", "sphinx_docs"]:
        remove_path(d)


# --- Dependency Manager File Handling ---

dep_manager = "{{ cookiecutter.dependency_manager }}".lower()

files_poetry = ["pyproject.toml", "poetry.lock"]
files_pipenv = ["Pipfile", "Pipfile.lock"]
files_requirements = ["requirements.txt", "dev-requirements.txt", "setup.py"]

all_dep_files = set(files_poetry + files_pipenv + files_requirements)

if dep_manager == "poetry":
    for f in all_dep_files:
        if f not in files_poetry:
            remove_path(f)
elif dep_manager == "pipenv":
    for f in all_dep_files:
        if f not in files_pipenv:
            remove_path(f)
elif dep_manager == "requirements":
    for f in all_dep_files:
        if f not in files_requirements:
            remove_path(f)
else:
    print(f"Warning: Unknown dependency manager '{dep_manager}', no dependency files removed.")


# --- Pre-commit Config Cleanup and Setup ---

precommit_files = {
    "poetry": ".pre-commit-config.poetry.yaml",
    "pipenv": ".pre-commit-config.pipenv.yaml",
    "requirements": ".pre-commit-config.venv.yaml",
}

selected_file = precommit_files.get(dep_manager)
final_name = ".pre-commit-config.yaml"

# Remove existing final config file if present
remove_path(final_name)

# Rename selected config to .pre-commit-config.yaml
if selected_file and os.path.exists(selected_file):
    shutil.move(selected_file, final_name)

# Remove the unused pre-commit config files
for key, filename in precommit_files.items():
    if filename != selected_file:
        remove_path(filename)
