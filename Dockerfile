FROM python:3.10

# Ensure logging is up to date despite possible buffering
ENV PYTHONUNBUFFERED 1

WORKDIR /app


# Install dependencies for mysqlclient
RUN set -eux && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]