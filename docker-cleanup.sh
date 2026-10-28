#!/bin/bash
# ==============================================================================
# ThaiD Cloud Automated Docker Maintenance & Disk Auto-Reclaimer
# ==============================================================================
LOG_FILE="/var/log/docker-cleanup.log"

echo "=== [$(date '+%Y-%m-%d %H:%M:%S')] Starting Automated Docker Cleanup ===" >> "$LOG_FILE"

# 1. Prune unused images older than 24 hours
docker image prune -a --filter "until=24h" -f >> "$LOG_FILE" 2>&1

# 2. Prune build cache older than 24 hours
docker builder prune --filter "until=24h" -f >> "$LOG_FILE" 2>&1

# 3. Prune exited containers older than 24 hours
docker container prune --filter "until=24h" -f >> "$LOG_FILE" 2>&1

# 4. Log disk status
echo "Disk Space After Cleanup:" >> "$LOG_FILE"
df -h / >> "$LOG_FILE"

echo "=== [$(date '+%Y-%m-%d %H:%M:%S')] Cleanup Complete ===" >> "$LOG_FILE"
