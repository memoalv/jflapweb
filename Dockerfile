FROM python:3.8-slim-bookworm

RUN \
    apt update && \
    apt install --no-install-recommends -y \
        git && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /jflapweb

COPY . .

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN GIT_PYTHON_REFRESH=quiet

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "-c", "gunicorn.conf.py", "wsgi"]
