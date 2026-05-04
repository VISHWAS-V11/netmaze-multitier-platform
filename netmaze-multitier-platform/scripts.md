#!/bin/bash

# ---- CONFIG ----
KEY_PATH="/path/to/private-key.pem"
PROCESS_DEST="ec2-user@10.50.20.210:/home/ec2-user/process/"
BUCKET_NAME="netmaze-vishwas"

# ---- STEP 1: Ingest → Process ----
for file in /home/ftpuser/files/*; do
    scp -i "$KEY_PATH" "$file" "$PROCESS_DEST"
    rm "$file"
done

# ---- STEP 2: Process → S3 ----
for file in /home/ec2-user/process/*; do
    aws s3 cp "$file" s3://$BUCKET_NAME/
    rm "$file"
done


# Pipeline Script

## pipeline.sh

This script handles the complete file flow.

### Step 1
- Moves files from Ingest EC2 to Process EC2
- Source: /home/ftpuser/files
- Destination: /home/ec2-user/process/

### Step 2
- Uploads files from Process EC2 to S3
- Source: /home/ec2-user/process/
- Destination: S3 bucket

### Notes
- Uses SCP for transfer
- Uses AWS CLI for S3 upload
- Deletes files after processing
