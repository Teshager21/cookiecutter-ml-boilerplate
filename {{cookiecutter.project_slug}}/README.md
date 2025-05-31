# {{ cookiecutter.project_name }}
> A production-grade, end-to-end Data Science project scaffold.

## 🚀 Overview

Welcome to **{{ cookiecutter.project_name }}**, a powerful project template designed to help you kick-start machine learning, analytics, or MLOps projects with modern best practices.

## 🛠️ Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

{% if cookiecutter.include_docker == "y" %}
### 2. Docker (Optional)

Build and run using Docker:

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run -p 8000:8000 {{ cookiecutter.project_slug }}
```
{% endif %}

{% if cookiecutter.use_dvc == "y" %}
### 3. DVC Setup (Optional)

Initialize and pull versioned data:

```bash
dvc init
dvc pull
```
{% endif %}

{% if cookiecutter.include_fastapi == "y" %}
### 4. FastAPI Dev Server

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```
{% endif %}

## 📁 Project Structure

```
{{ cookiecutter.project_slug }}/
├── data/                 # Data folders (raw, processed, external, etc.)
├── notebooks/            # Jupyter notebooks for exploration and reporting
├── src/                  # Python package: data, features, models, utils
├── tests/                # Unit & integration tests
├── config/               # Environment-specific configs
├── reports/              # Generated outputs and visualizations
├── api/                  # FastAPI backend (if enabled)
├── edge/                 # Edge deployment tools (e.g., quantization)
├── infra/                # Terraform infrastructure code
├── .github/              # Workflows, PR templates, issue templates
├── Makefile              # Automation commands
├── Dockerfile            # Containerization (if enabled)
├── dvc.yaml              # DVC pipelines (if enabled)
```

## ✅ Features

- Clean, modular structure
{% if cookiecutter.use_dvc == "y" %}- Integrated DVC for data versioning{% endif %}
{% if cookiecutter.include_fastapi == "y" %}- FastAPI for serving models or APIs{% endif %}
{% if cookiecutter.include_docker == "y" %}- Docker for reproducible environments{% endif %}
- MLFlow-ready experiment tracking
- GitHub Actions CI/CD pipeline
- Infrastructure-as-Code with Terraform

## 📜 License

Distributed under the **{{ cookiecutter.license }}** License. See `LICENSE` for more information.
