FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app/project
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8000