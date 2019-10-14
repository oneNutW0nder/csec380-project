FROM python:3.7.1

# Set env vars
ENV FLASK_APP "application/"
ENV FLASK_ENV "development"
ENV DATABASE_URL "mysql+pymysql://root:root-password@database:3306/firewagon"

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

# Run the flask app with certs
CMD flask run --host 0.0.0.0
