# Base image with Python and necessary tools
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Start Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.headless=true"]
