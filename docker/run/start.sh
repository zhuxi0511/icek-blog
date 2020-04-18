cd /app/blog
python manage.py collectstatic
cd /app/run
uwsgi --ini uwsgi.ini
