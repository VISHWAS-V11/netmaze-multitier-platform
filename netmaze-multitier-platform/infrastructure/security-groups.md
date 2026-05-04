# Security Groups

## ALB Security Group
Inbound:
- HTTP (80) → 0.0.0.0/0

Outbound:
- HTTP (80) → App EC2 Security Group

---

## App EC2 Security Group
Inbound:
- HTTP (80) → ALB Security Group
- SSH (22) → Bastion Host

Outbound:
- MySQL (3306) → RDS Security Group
- Internet access via NAT Gateway

---

## RDS Security Group
Inbound:
- MySQL (3306) → App EC2 Security Group

Outbound:
- Default

---

## Bastion Security Group
Inbound:
- SSH (22) → Your IP

Outbound:
- SSH (22) → Private EC2 instances

---

## Notes

- App EC2 is not publicly accessible
- SSH access is only through Bastion
- RDS is private and not exposed to internet
