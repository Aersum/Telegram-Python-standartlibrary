import csv


def create_csv(students_list: list, file_name: str):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = list(students_list[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students_list)
    print(f'"{file_name}" created')
