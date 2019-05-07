#!/bin/bash
gunicorn --workers=5 -b :8080  site_for_tasks.wsgi:application &
