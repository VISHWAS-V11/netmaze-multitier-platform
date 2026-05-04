# VPC Configuration

## VPC
- CIDR: 10.50.0.0/16

---

## Subnets

### Public Subnets
- 10.50.1.0/24 → ALB + NAT Gateway
- 10.50.2.0/24 → ALB

### Private Subnets
- 10.50.10.0/24 → Ingest EC2
- 10.50.20.0/24 → Process EC2
- 10.50.30.0/24 → Application EC2
- 10.50.40.0/24 → RDS Database
---

## Internet Access

### Internet Gateway
- Attached to VPC
- Used only by public subnets

### NAT Gateway
- Created in 10.50.1.0/24
- Used by:
  - Ingest EC2
  - Process EC2
  - App EC2

---

## Route Tables

### Public Route Table
- 0.0.0.0/0 → Internet Gateway

### Private Route Table (Ingest / Process / App)
- 0.0.0.0/0 → NAT Gateway

### DB Route Table
- No internet access
- Only internal VPC communication

---

## Notes

- ALB is public
- All EC2 instances are private
- RDS is private
- Internet access for private EC2 is via NAT only
