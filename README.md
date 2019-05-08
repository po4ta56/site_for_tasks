# site_for_tasks
тестовое задание


Проект доступен для запуска в контейнере Docker:

cd
mkdir docker_tasks
cd docker_tasks
curl https://raw.githubusercontent.com/po4ta56/site_for_tasks/master/docker/Dockerfile -o Dockerfile
sudo docker build -t site_tasks:ver1
sudo docker run -it -d  --name site-for-tasks --rm -p 8000:80 -p 8001:8080  site_tasks:ver1
