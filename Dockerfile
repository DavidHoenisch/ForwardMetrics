FROM python:3.10.6

WORKDIR /opt/fwapp_frontent

# Copy over application code
COPY app/main.py .
COPY app/website/ ./website/
COPY requirements.txt .

# Set up environment
RUN pip install -r requirements.txt
RUN pip install "uvicorn[standard]" gunicorn

# Expose port 5001
EXPOSE 5000

# Run the application
CMD ["/bin/sh", "-c", "uvicorn main:app --workers 4 --host 0.0.0.0 --port 5000"]
