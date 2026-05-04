# FTP Setup

## Service
- vsftpd installed

---

## User
- Username: ftpuser

---

## Directory
- Upload Path: /home/ftpuser/files

---

## Configuration

- FTP server running on Ingest EC2
- Users can upload files to the directory
- Chroot: Not enabled
- TLS: Not configured

---

## Notes

- Used for uploading raw files
- Files are later processed in the pipeline
