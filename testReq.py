from gpiozero import LED
from time import sleep
from urllib.parse import urlparse
import psycopg2

led = LED(17)

def pcOn():
	led.on()
	sleep(1)
	led.off()

def pcOff():
	led.on()
	sleep(3)
	led.off()

result = urlparse("postgres://hcgetrdwryayat:70f2b4d1ce6e04b79648b6d0abdc20b16e564c41a52ad2db62417e2768f3d795@ec2-35-153-114-74.compute-1.amazonaws.com:5432/dbqb6im16itd60")

username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port
connection = psycopg2.connect(
    database = database,
    user = username,
    password = password,
    host = hostname,
    port = port
)




while True:
	cursor = connection.cursor()
	postgreSQL_select_Query = "select * from onoff;"

	cursor.execute(postgreSQL_select_Query)
	mobile_records = cursor.fetchall()
	for row in mobile_records:
	    cursor.execute("DELETE FROM onoff WHERE onoff='off'")
	    connection.commit()
	    cursor.execute("DELETE FROM onoff WHERE onoff='on'")
	    connection.commit()

	    if row[0] == "on":
	    	pcOn()
	    else:
	    	pcOff()
	    print(row[0])
