FROM python:3.9

# Set the working directory to /app for subsequent commands
WORKDIR /app

# Copy the application code into the container
COPY ./app /app/

# Copy the tests directory into the container
COPY ./tests /tests/

# Install the required Python packages
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port that the Flask app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

