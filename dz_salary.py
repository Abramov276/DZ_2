def total_salary(path):
    with open('salary.txt', 'r', encoding='utf-8') as sal:
        salaries = []
        for line in sal:
            path = line.split(',')

            if len(path) == 2:
                name, salary = path

                try:
                    salaries.append(int(salary.strip()))

                except ValueError:
                    print(f"Invalid format for {name.strip()}")

    if salaries:
        total_salary = sum(salaries)
        average_salary = total_salary / len(salaries)

        return f"The total amount of salary: {
            total_salary}, Average salary: {average_salary}"
    else:
        return 'No file'


print(total_salary('salary.txt'))
