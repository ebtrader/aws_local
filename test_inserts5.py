from sshtunnel import SSHTunnelForwarder
import pymysql
import pandas as pd

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
    df = pd.read_csv('testdata.csv')
    print(df)

    try:
        # Print all the databases

        with db.cursor() as cur:
            for i, row in df.iterrows():
                sql = 'insert into aliensdb.Animals (PersonID, LastName, FirstName, Address, City) VALUES (%s, %s, %s, %s, %s)'
                cur.execute(sql, tuple(row))
                db.commit()
    finally:
        db.close()


