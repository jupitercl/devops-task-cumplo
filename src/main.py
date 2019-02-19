from bottle import route, run, template, request, install
import os
import psycopg2

dbip = os.getenv('DB_IP', 'ip')
dbname = os.getenv('DB_NAME', 'dbname')
user = os.getenv('DB_USER', 'user')
password = os.getenv('DB_PASS', 'pass')
IP = os.getenv('GUNICORN_IP', '0.0.0.0')
PORT = os.getenv('GUNICORN_PORT', '8080')
WORKERS = os.getenv('GUNICORN_WORKERS', '1')

@route('/')
def index():
	conn = psycopg2.connect(host=dbip,database=dbname, user=user, password=password)
	status = 'CONNECTED' if conn.status == 1 else 'NOT CONNECTED'

	return template('<b>Connection Status {{status}}</b>!', status=status)
      
run(host=IP, port=PORT, server='gunicorn', workers=WORKERS)
