FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

{% if cookiecutter.include_fastapi == "y" %}
COPY api/ ./api/
{% endif %}
COPY src/ ./src/

CMD ["python", "api/main.py"]
