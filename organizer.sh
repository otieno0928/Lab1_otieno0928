#!/bin/bash

ARCHIVE_DIR="archive"
ORIGINAL_FILE="grades.csv"
LOG_FILE="organizer.log"

# Check/Create archive folder
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir -p "$ARCHIVE_DIR"
fi

# Check if grades.csv exists
if [ ! -f "$ORIGINAL_FILE" ]; then
    echo "Error: $ORIGINAL_FILE does not exist to archive."
    exit 1
fi

# Create timestamp string
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
ARCHIVED_FILENAME="grades_${TIMESTAMP}.csv"
ARCHIVED_PATH="${ARCHIVE_DIR}/${ARCHIVED_FILENAME}"

# Move and rename file
mv "$ORIGINAL_FILE" "$ARCHIVED_PATH"

# Reset workspace (create empty grades.csv)
touch "$ORIGINAL_FILE"

# Log event
echo "[${TIMESTAMP}] Archived '${ORIGINAL_FILE}' -> '${ARCHIVED_PATH}'" >> "$LOG_FILE"

echo "Successfully archived '${ORIGINAL_FILE}' to '${ARCHIVED_PATH}'."
