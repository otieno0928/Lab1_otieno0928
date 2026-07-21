import csv
import sys
import os

def load_csv_data():
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    print("\n--- Processing Grades ---")

    if not data:
        print("Error: The CSV file contains no valid records.")
        return

    total_weight = 0.0
    formative_weight = 0.0
    summative_weight = 0.0

    formative_score = 0.0
    summative_score = 0.0

    failed_formatives = []

    for item in data:
        name = item['assignment']
        group = item['group'].strip()
        score = item['score']
        weight = item['weight']

        if not (0 <= score <= 100):
            print(f"Validation Error: Score for '{name}' must be between 0 and 100 (got {score}).")
            return

        weighted_score = (score / 100.0) * weight
        total_weight += weight

        if group.lower() == 'formative':
            formative_weight += weight
            formative_score += weighted_score

            if score < 50:
                failed_formatives.append((name, weight))

        elif group.lower() == 'summative':
            summative_weight += weight
            summative_score += weighted_score
        else:
            print(f"Validation Error: Unknown group category '{group}' for assignment '{name}'.")
            return

    # Weight Validations
    if round(total_weight, 2) != 100.0:
        print(f"Validation Error: Total weight must equal 100 (got {total_weight}).")
        return

    if round(formative_weight, 2) != 60.0 or round(summative_weight, 2) != 40.0:
        print(f"Validation Error: Formative weight must equal 60 (got {formative_weight}) "
              f"and Summative weight must equal 40 (got {summative_weight}).")
        return
    total_grade = formative_score + summative_score
    gpa = (total_grade / 100.0) * 5.0

    passed = (formative_score >= 30.0) and (summative_score >= 20.0)
    status = "PASSED" if passed else "FAILED"

    resubmission_str = "None"
    if failed_formatives:
        max_weight = max(item[1] for item in failed_formatives)
        eligible = [item[0] for item in failed_formatives if item[1] == max_weight]
        resubmission_str = ", ".join(eligible)

    print(f"Formatives (60): {formative_score:.1f}")
    print(f"Summatives (40): {summative_score:.1f}")
    print(f"GPA: {gpa:.3f}")
    print(f"Status: {status}")
    print(f"Available for resubmission: {resubmission_str}")

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
