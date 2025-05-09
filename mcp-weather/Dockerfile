FROM python:3.13-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml weather.py ./

# Install dependencies
RUN pip install --no-cache-dir .

# Run the weather service
CMD ["python", "weather.py"]