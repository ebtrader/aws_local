from sshtunnel import SSHTunnelForwarder
import pymysql

# https://gist.github.com/riddhi89/9d53140dec7c17e63e22a0b5ab43f99f
# https://www.linkedin.com/pulse/programmatically-access-private-rds-database-aws-from-tom-reid/

with SSHTunnelForwarder(

        ('ec2-44-202-61-2.compute-1.amazonaws.com'),
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
            sql = 'insert into javeddb.Persons (PersonID, LastName, FirstName, Address, City) VALUES (%s, %s, %s, %s, %s)'
            val = (7, "Siddiq", "Shahan", "5 loser st", "Akron")
            cur.execute(sql, val)
            db.commit()
    finally:
        db.close()


