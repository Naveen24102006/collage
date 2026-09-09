FROM python:3.14.6-slim
WORKDIR /app
COPY . .
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r
requirements.txt; fi
CMD ["python", "main.py"]
