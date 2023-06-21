FROM nginx:latest

RUN COPY nginx.conf /etc/nginx/nginx.conf
RUN COPY conf.d/default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]