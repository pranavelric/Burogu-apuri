FROM python:3.8-slim
RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev


ENV PYTHONBUFFERED =1
WORKDIR /app/
copy requirements.txt ./requirements/requirements.txt
RUN pip install -r ./requirements/requirements.txt
copy . .
EXPOSE 8000
