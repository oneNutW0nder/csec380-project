FROM python:3.7.1

# Setup files
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

# Update system and install requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Add all app files and expose port 5000
ADD . /app/
EXPOSE 5000

# Run flask
CMD flask run
