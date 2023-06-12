from sshtunnel import SSHTunnelForwarder
import sqlalchemy
import pymysql

# Doing it the awswrangler/sqlalchemy way
#

with SSHTunnelForwarder(

        ('ec2-52-207-214-84.compute-1.amazonaws.com'),
        ssh_username='ubuntu',
        ssh_pkey=r'C:\Users\jsidd\Documents\aws\test_key.pem',
        remote_bind_address=('database-1.c3dig9vjwrmk.us-east-1.rds.amazonaws.com', 3306)

) as tunnel:
    print("****SSH Tunnel Established****")

    db = pymysql.connect(
        host='127.0.0.1', user='admin',
        password='suite203', port=tunnel.local_bind_port
    )

    # Run sample query in the database to validate connection
    try:
        # Print all the databases
        with db.cursor() as cur:
            cur.execute('SHOW DATABASES')
            for r in cur:
                print(r)
    finally:
        db.close()

print("YAYY!!")
