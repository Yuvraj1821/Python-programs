# def add(a, b):
#     return a+b
#
# print(add(4, 5))

add = lambda a, b: a + b
print(add(4, 7))

full_name = lambda f_name, l_name: f_name + " " + l_name
print(full_name("python", "programming"))

# difficult use of lambda function

students = [("Squidward", 'F', 60), ("Sandy", 'A', 40),
            ("Patrick", "D", 33), ("Spongebob", "B", 36),
            ("Mr. Crabs", "C", 85)]

students.sort()
print("Sorted elements using first index value : ", students)

grade = lambda grades: grades[1]
students.sort(key=grade)            # sorting elements in ascending order
print("Sorted elements using second index value : ", end="")
for i in students:
    print(i, end="")


age = lambda ages: ages[1]
students.sort(key=age, reverse=True)            # sorting elements in ascending order
print("")
print("", "Sorted elements in ascending order using third index value : ", end="")
for i in students:
    print(i, end=" ")