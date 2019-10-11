FROM nginx:latest

COPY hello.html /usr/share/nginx/html
COPY default.conf /etc/nginx/

COPY nginx.crt /etc/ssl/
COPY nginx.key /etc/ssl

EXPOSE 443