FROM python:3.8-slim
ENV PYTHONBUFFERED =1
WORKDIR /app/
copy requirements.txt ./requirements/requirements.txt
RUN pip install -r ./requirements/requirements.txt
copy . .
EXPOSE 8000
