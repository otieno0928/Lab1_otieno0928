# Lab 1: Grade Evaluator & Archiver

Repository Name: **Lab1_otieno0928**

This repository contains an automated grade processing system and archiving tool built for **Lab 1**. The project consists of a Python script that validates student grades, calculates GPAs, and determines pass/fail status, alongside a Bash shell script that automates the file archiving and logging process.


## Repository Files

* `grade-evaluator.py`: A Python application that loads course data from a CSV file, performs strict range and weight validations (60% Formative / 40% Summative), computes the student's overall GPA on a 5.0 scale, checks for passing criteria (≥ 50% in both categories), and identifies any failed formative assignments eligible for resubmission.
* `organizer.sh`: A shell script that checks for or creates an `archive/` directory, renames and moves the active `grades.csv` file using a date-time timestamp, resets the workspace by creating a fresh empty `grades.csv`, and logs every execution to `organizer.log`.
* `Readme.md`: Instructions and documentation on how to run and test the application.


Ensure you have Python 3 installed on your system and a properly formatted CSV file (e.g., `grades.csv`) in the repository directory.

1. Open your terminal in the repository directory.
2. Execute the script:
   ```bash
   python3 grade-evaluator.py
   input the file ie "grades.csv"
   chmod +x organizer.sh
   ./organizer.sh
   add the files,commit and push  

N/B:
**Execution Behavior:**
<!--Directory Management: Checks if the archive/ folder exists; if not, it automatically creates it.--!>
#Archival & Timestamping: Renames the active grades.csv using the timestamp format grades_YYYYMMDD-HHMMSS.csv and moves it into the archive/ directory.
#Workspace Reset: Instantly generates a brand new, empty grades.csv file in the main folder using touch so the workspace is ready for new input.
#Event Logging: Appends an entry recording the execution timestamp and file paths into organizer.log. EOF

