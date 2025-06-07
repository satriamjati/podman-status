FROM python:alpine

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and templates
COPY app.py .
COPY templates ./templates

EXPOSE 80

CMD ["python", "app.py"]
