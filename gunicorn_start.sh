#!/bin/bash
cd /home/site-for-tasks
gunicorn --workers=5 -b :8080  site_for_tasks.wsgi:application &
