from sshtunnel import SSHTunnelForwarder
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import os

# https://gist.github.com/riddhi89/9d53140dec7c17e63e22a0b5ab43f99f
# https://www.linkedin.com/pulse/programmatically-access-private-rds-database-aws-from-tom-reid/

with SSHTunnelForwarder(

        ('ec2-54-226-23-54.compute-1.amazonaws.com'),
        ssh_username='ubuntu',
        ssh_pkey=r'C:\Users\jsidd\Documents\aws\test_key.pem',
        remote_bind_address=('database-1.c3dig9vjwrmk.us-east-1.rds.amazonaws.com', 3306)

) as tunnel:
    print("****SSH Tunnel Established****")

    username = 'admin'
    hostname = '127.0.0.1'
    pwd = 'suite203'
    dbname = 'javeddb'
    port = tunnel.local_bind_port

    connection_string = 'mysql+mysqlconnector://' + username + ':' + pwd + '@' + hostname + ':' + str(port) + '/' + dbname
    engine = create_engine(connection_string)

    directory_path = r'C:\Users\jsidd\Documents\test_files\test_data'

    # filepath = r'C:\Users\jsidd\Documents\test_files\test_data\testdata.csv'

    for file_name in os.listdir(directory_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(directory_path, file_name)
            df = pd.read_csv(file_path)

            # Add an extra column with the filename
            df['filename'] = file_name

            print(df)
            df.to_sql('hair', con=engine, if_exists='append', index=False)
