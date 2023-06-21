FROM nginx:latest

RUN cp nginx.conf /etc/nginx/nginx.conf
RUN cp conf.d/default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]