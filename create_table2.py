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
            # cur.execute('select * from javeddb.yahoo_create')
            cur.execute('''CREATE TABLE javeddb.tqqq_raw_temp (
  `id` int NOT NULL AUTO_INCREMENT,
  `ticker` varchar(10) DEFAULT NULL,
  `strike` int DEFAULT NULL,
  `expiration` datetime DEFAULT NULL,
  `time_created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32235 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci''')
            db.commit()

            # cur.execute('insert into javeddb.Persons (PersonID, LastName, FirstName, Address, City) '
            #            'VALUES (2, "Song", "Jane", "5 hoe st", "Philadelphia"); ')

    finally:
        db.close()


