# Ubuntu Full OS Backup (Daily & Free)

This guide provides a simple way to back up your entire Ubuntu system daily, using free tools.

## Method: `rsync` with Cron Job

### Prerequisites
- An external drive, network location, or another disk partition to store the backups.
- `rsync` installed (pre-installed on most Ubuntu systems).
- `cron` to automate backups.

### Step 1: Identify Backup Destination
Decide where you want to store your backups. Example paths:
- External drive: `/mnt/backup`
- Network storage: `/media/nas`
- Another disk partition: `/backup`

Ensure the destination is mounted before backup.

### Step 2: Create Backup Script
Create a backup script `/usr/local/bin/backup.sh`:

```bash
#!/bin/bash
BACKUP_DIR="/mnt/backup/ubuntu_backup_$(date +%Y-%m-%d)"
mkdir -p "$BACKUP_DIR"
rsync -aAXv / "$BACKUP_DIR" --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"}
```

Make the script executable:
```bash
sudo chmod +x /usr/local/bin/backup.sh
```

### Step 3: Automate with Cron
Edit the cron jobs:
```bash
crontab -e
```
Add the following line to run the backup daily at 2 AM:
```bash
0 2 * * * /usr/local/bin/backup.sh
```

### Step 4: Restore Backup
To restore a backup, boot from a live USB and use `rsync`:
```bash
sudo rsync -aAXv /mnt/backup/ubuntu_backup_YYYY-MM-DD/ / --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"}
```
Replace `YYYY-MM-DD` with the desired backup date.

### Optional: Rotate Backups
To keep only the last 7 backups, modify the script:
```bash
find /mnt/backup/ -maxdepth 1 -type d -mtime +7 -exec rm -rf {} \;
```
Add this line before the `rsync` command in `backup.sh`.

---

Now your Ubuntu system will back up daily for free using `rsync` and `cron`. 🚀

