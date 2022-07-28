FROM python:3.10.5-alpine3.16
RUN pip install azure-storage-queue flask
ADD main.py .
ENV PYTHONUNBUFFERED=0
CMD ["python", "./main.py"]
