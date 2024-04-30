FROM python:3.8-slim

RUN pip install flask tensorflow

WORKDIR /app

COPY inference.py /app/

EXPOSE 5000

CMD ["python", "inference.py"]

