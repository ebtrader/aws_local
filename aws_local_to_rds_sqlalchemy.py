from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine

# https://gist.github.com/riddhi89/9d53140dec7c17e63e22a0b5ab43f99f
# https://www.linkedin.com/pulse/programmatically-access-private-rds-database-aws-from-tom-reid/

with SSHTunnelForwarder(

        ('ec2-44-202-61-2.compute-1.amazonaws.com'),
        ssh_username='ubuntu',
        ssh_pkey=r'C:\Users\jsidd\Documents\aws\test_key.pem',
        remote_bind_address=('database-1.c3dig9vjwrmk.us-east-1.rds.amazonaws.com', 3306)

) as tunnel:
    print("****SSH Tunnel Established****")

    host = '127.0.0.1'
    user = 'admin'
    password = 'suite203'
    database = 'javeddb'

    connection_string = 'mysql+mysqlconnector://' + user + password + host + database

    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = create_engine(connection_string)
        print(
            f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

