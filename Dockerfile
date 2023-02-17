FROM python:3.10.6

WORKDIR /opt/fwapp_frontent

# Copy over application code
COPY app/main.py .
COPY app/website/ ./website/
COPY requirements.txt .

# Set up environment
RUN pip install -r requirements.txt


# Configure variable from .env file

# Expose port 8000
EXPOSE 5000

# Run the application
CMD ["/bin/sh", "-c", "python3 ./app.py"]
