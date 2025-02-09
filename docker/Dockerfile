FROM python:3.9
WORKDIR /app

# Copy the application code and requirements.txt into the container
COPY app.py /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Flask app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
