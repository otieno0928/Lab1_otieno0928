# Lab 1: Grade Evaluator & Archiver

Repository Name: **Lab1_otieno0928**

This project consists of a Python evaluation application (`grade-evaluator.py`) and a Bash management script (`organizer.sh`).


1. `grade-evaluator.py`: Reads course data from a CSV, validates entry ranges and weights (60/40 split), calculates GPA (5.0 scale), checks standing, and flags highest-weighted failed formatives for resubmission.
2. `organizer.sh`: Automated shell script that archives `grades.csv` to an `archive/` directory with a timestamp, resets `grades.csv`, and writes log entries to `organizer.log`.
3. `Readme.md`: Usage guidelines for the project.


```bash
python3 grade-evaluator.py

grades.csv
./organizer.sh
'''
