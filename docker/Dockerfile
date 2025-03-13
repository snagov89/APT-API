FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app


RUN apt-get update && apt-get install -y \
    apt-utils \
    libgl1-mesa-glx \
    libglib2.0-0 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


RUN pip install poetry

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock /app/

COPY . /app
RUN poetry install --no-root 

COPY docker/entrypoint.sh /app/docker/entrypoint.sh

RUN chmod +x /app/docker/entrypoint.sh

ARG ENVIRONMENT=prod
ENV ENVIRONMENT=${ENVIRONMENT}

ENV FLASK_APP=app \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=1337

CMD ["/app/docker/entrypoint.sh"]