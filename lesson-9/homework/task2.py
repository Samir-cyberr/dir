import csv

def calculate_average_grades():
    # Read grades from CSV
    grades = []
    with open('grades.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append({
                'Name': row['Name'],
                'Subject': row['Subject'],
                'Grade': int(row['Grade'])
            })
    
    # Calculate average grades by subject
    subject_grades = {}
    for entry in grades:
        subject = entry['Subject']
        if subject not in subject_grades:
            subject_grades[subject] = []
        subject_grades[subject].append(entry['Grade'])
    
    averages = []
    for subject, grades in subject_grades.items():
        avg = sum(grades) / len(grades)
        averages.append({'Subject': subject, 'Average Grade': avg})
    
    # Write averages to new CSV
    with open('average_grades.csv', mode='w', newline='') as file:
        fieldnames = ['Subject', 'Average Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in averages:
            writer.writerow(row)
    
    print("Average grades calculated and saved to average_grades.csv")

if __name__ == "__main__":
    calculate_average_grades()