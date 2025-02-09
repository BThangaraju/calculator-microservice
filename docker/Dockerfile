FROM python:3.9

# Set working directory to /app
WORKDIR /app

# Copy the application code
COPY ./app /app/

# Copy the tests directory
COPY ./tests /tests/

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "/app/app.py"]

