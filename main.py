#Завдання1

def total_salary(path):
    total_salary = 0
    count = 0

    try:
        with open("salary.txt", "r") as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total_salary += float(salary)
                    count += 1
                except ValueError:
                    print('Incorrect string found')
                    continue
    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0

    if count == 0:
        print("No salary found")
    else:
        average = total_salary / count
        return average, total_salary

path_salary = "/Users/user/PycharmProjects/Homework/Salary.txt"

print(total_salary(path_salary))

#Завдання 2

def get_cats_info(path):
    cats_info = []
    with open("CatsInfo.txt", "r") as file:
        for line in file:
            try:
                id, name, age = line.strip().split(',')

                cats_info.append ({
                    "id": id,
                    "name": name,
                    "age": age
                })
            except ValueError:
                print("Incorrect data found")
                continue
    return cats_info

path_cats_info = "/Users/user/PycharmProjects/Homework/CatsInfo.txt"
print(get_cats_info(path_cats_info))