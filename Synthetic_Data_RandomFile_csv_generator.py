import random
import csv
no_of_rows = 15000

columns = ['hours_studied', 'previous_grade', 'parental_support', 'attendance', 'extracurricular', 'family_income', 'class_participation', 'homework_completion', 'sleep_hours', 'final_grade']
def generate_data():

    # change the data fields here for random generation and return the elementss of the function accordingly.

    hours_studied = random.randrange(start=1, stop=14)
    previous_grade = random.randrange(start=30, stop=100)
    parental_support = random.randrange(start=0, stop=2)
    attendance = random.randrange(start=40, stop=100)
    extracurricular = random.randrange(start=0, stop=2)
    family_income = random.randrange(start=50000, stop=200000)
    class_participation = random.randrange(start=0, stop=2)
    homework_completion = random.randrange(start=0, stop=100)
    sleep_hours = random.randrange(start=5, stop=24)
    final_grade = random.randrange(start=40, stop=100)

    return [hours_studied, previous_grade, parental_support, attendance, extracurricular, family_income, class_participation, homework_completion, sleep_hours, final_grade]

with open('Synthetic_data_for_ML_model.csv', mode='w', newline='') as file:
    
    # For writing the sybthetic generated data into the csv file

    writer = csv.writer(file)

    writer.writerow(columns)
    for _ in range(no_of_rows):
        writer.writerow(generate_data())

print("Synthetic Data generated Successfully")
