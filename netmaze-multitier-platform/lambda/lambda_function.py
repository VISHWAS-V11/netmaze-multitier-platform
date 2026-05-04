# Lambda Function

## Trigger
- S3 upload event

---

## Function

- Triggered when a file is uploaded to S3
- Reads file name (object key)
- Inserts file name into RDS database

---

## Database

- Database: netmaze
- Table: files
- Column: file_name

---

## Flow

S3 Upload → Lambda Trigger → Insert into RDS

---

## Notes

- Stores S3 object key as file name
- Used by application to display uploaded files

# CODE

import json
import pymysql

# DB config

host = os.environ['DB_HOST']
user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
database = os.environ['DB_NAME']

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
