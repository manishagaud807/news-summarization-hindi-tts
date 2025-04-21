# Use a base image
FROM python:3.10-slim

WORKDIR /app
COPY . /app

# RUN pip install --upgrade pip && \
#     pip install -r requirements.txt
RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
