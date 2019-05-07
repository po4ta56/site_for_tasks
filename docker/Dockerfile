FROM ubuntu
WORKDIR /home 
RUN apt-get update && apt-get install -y python3 python3-distutils git nginx curl
RUN curl https://bootstrap.pypa.io/get-pip.py -o /home/get-pip.py
RUN python3 /home/get-pip.py 
RUN pip install Django && pip install gunicorn
RUN git clone https://github.com/po4ta56/site_for_tasks.git site-for-tasks
RUN unlink /etc/nginx/sites-enabled/default && ln -s /home/site-for-tasks/nginx_site-for-tast.conf /etc/nginx/sites-enabled/site-for-tasks.conf
RUN chmod +x /home/site-for-tasks/gunicorn_start.sh
RUN ln -s /home/site-for-tasks/gunicorn_start.sh /usr/bin/gunicorn_start
RUN service nginx start
ENTRYPOINT ["gunicorn_start"]
EXPOSE 80
EXPOSE 8080