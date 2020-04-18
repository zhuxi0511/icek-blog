docker run -d --restart=unless-stopped --name blog1.1 -v /home/zhuxi/blog/:/app/blog -v /home/zhuxi/blog/run/static_files/:/app/run/static_files -p:8080:8080 docker_blog:1.1
