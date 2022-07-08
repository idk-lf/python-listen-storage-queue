FROM python:3.10.5-alpine3.16
ADD main.py .
RUN pip install azure-storage-queue
CMD ["python", "./main.py"]
