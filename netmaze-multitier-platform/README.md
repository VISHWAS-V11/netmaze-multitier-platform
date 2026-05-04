# NetMaze – Multi-Tier Secure Data Processing Platform 🚀

## 📌 Overview

NetMaze is a cloud-based multi-tier architecture designed to securely process and serve data using AWS services and Linux systems.
The project emphasizes **network isolation, secure communication, and controlled data flow across multiple layers**.

---

## 🏗️ Current Architecture (Implemented)

User → ALB → App EC2 (Private) → RDS
↑
Lambda
↑
S3

---

## 🔄 Data Flow (Implemented)

1. File uploaded to S3
2. S3 triggers Lambda function
3. Lambda inserts metadata into RDS
4. Flask application reads data from RDS
5. Application served via ALB

---

## 🌐 Infrastructure Setup

### VPC Design

* CIDR: 10.50.0.0/16
* Public Subnets: ALB
* Private Subnets:

  * Application EC2
  * RDS Database

### Connectivity

* Internet Gateway → Public subnets
* NAT Gateway → Private subnets

---

## 🔐 Security Architecture

* Application EC2 is **private (no public IP)**
* Access via **Bastion Host** only
* ALB → EC2 communication via Security Groups
* RDS → Accessible only from EC2
* No direct internet access to backend

---

## ⚙️ Tech Stack

* Python (Flask)
* AWS EC2 (Private instances)
* Amazon RDS (MySQL)
* AWS Lambda
* Amazon S3
* Application Load Balancer
* VPC (Subnets, Routing, NAT, IGW)
* Linux (Amazon Linux 2023)

---

## 🚀 Features

✔ Event-driven architecture (S3 → Lambda)
✔ Private backend infrastructure
✔ Secure DB access
✔ Load balancing using ALB
✔ Bastion-based SSH access
✔ Real-world debugging of AWS networking

---

## 🛠️ What I Implemented

* Designed VPC with multiple subnets
* Configured NAT Gateway & routing
* Deployed private EC2 instances
* Built Flask app connected to RDS
* Created Lambda function for DB insertion
* Configured S3 event triggers
* Set up ALB and Target Groups
* Debugged ALB ↔ EC2 connectivity

---

## 🔄 Work in Progress

* Ingest EC2 (FTP with TLS)
* Process EC2 pipeline (cron automation)
* Vault EC2 with LUKS encryption
* Auto Scaling Group for App EC2
* CloudFront integration
* API Gateway integration

---

## ▶️ Run Application

```bash
pip3 install -r requirements.txt
sudo python3 app.py
```

---

## 🌐 Access

http://<ALB-DNS>

---

## 🧠 Key Learning

* Deep understanding of AWS VPC architecture
* Debugging real-world network issues
* Security group and routing design
* Multi-tier cloud system implementation

---
