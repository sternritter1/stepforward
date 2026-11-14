grades = {
    "Anna": [1, 2, 1],
    "Petr": [3, 4, 2],
    "Eva": [1, 1, 2],
}
best_grade = 6
best_name = ""
for name, grade in grades.items():
    avg = sum(grade) / len(grade)
    if avg < best_grade:
        best_grade = avg
        best_name = name
    print(f"{name}: {round((avg),2)}")
print("Best:", best_name)
