FROM python:3.12-slim
WORKDIR /app
COPY app.py /app/app.py
RUN useradd -r -u 10001 appuser && chown -R appuser:appuser /app
USER appuser
CMD ["python", "/app/app.py"]
