import json
import pymysql

# DB config
host = "database-1-netmaze.cfwqemaqskyh.ap-south-1.rds.amazonaws.com"
user = "admin"
password = "netmazeadmin"
database = "netmaze"

def lambda_handler(event, context):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            connect_timeout=5
        )

        for record in event['Records']:
            file_key = record['s3']['object']['key']
            print("Processing file:", file_key)
            
            with connection.cursor() as cursor:
                sql = "INSERT INTO files (file_name) VALUES (%s)"
                cursor.execute(sql, (file_key,))
        
        connection.commit()
        connection.close()

        return {
            'statusCode': 200,
            'body': json.dumps('Inserted into DB')
        }

    except Exception as e:
        print(str(e))
        return {
            'statusCode': 500,
            'body': str(e)
        }
