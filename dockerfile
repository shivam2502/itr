FROM python:3.10-slim

COPY itr_service /app/itr_service

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.itr_service.main:app", "--host", "0.0.0.0", "--port", "8000"]