FROM python:3.11-slim

WORKDIR /app

COPY . .

COPY modelo_tree_tuneado.pkl .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8080"]

