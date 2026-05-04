# Cron Jobs

## Schedule

*/2 * * * * /home/ec2-user/pipeline.sh

---

## Description

- Runs every 2 minutes on Ingest EC2  
- Executes the pipeline script to move files and upload to S3  

---

## Importance

- Automates the entire data flow without manual intervention  
- Ensures files are processed continuously and reliably
