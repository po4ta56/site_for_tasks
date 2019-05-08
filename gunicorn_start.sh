#!/bin/bash
cd /home/site-for-tasks
service nginx start
gunicorn --workers=5 -b :8080  site_for_tasks.wsgi:application 
