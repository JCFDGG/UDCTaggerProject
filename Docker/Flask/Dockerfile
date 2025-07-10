FROM python:3.9.23-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy the entire app
COPY . .


# Expose port
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0:5000", "app:app"]