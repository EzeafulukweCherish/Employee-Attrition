FROM python:3.12-slim

WORKDIR /code

# Install dependencies first (better Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY ./app ./app
COPY ./model ./model

# Render sets $PORT at runtime; default to 8000 for local runs
ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
