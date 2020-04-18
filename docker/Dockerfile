# use base python image with python 2.7
FROM python:3.6

# install mysql-client
#RUN apt-get update
#RUN apt-get install -y mysql-client

# env
ENV RUN_MODE=DEPLOY

# add project to the image
COPY run/  /app/run/
COPY blog/  /app/blog/

# set working directory to /app/
WORKDIR /app/run

# install python dependencies
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# RUN server after docker is up
CMD ./start.sh
