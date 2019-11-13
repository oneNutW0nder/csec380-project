FROM nginx:latest

COPY conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY ca/server.key /etc/nginx
COPY ca/server.crt /etc/nginx

EXPOSE 80 443