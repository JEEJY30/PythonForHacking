# dictionary = {"name": "Alice", "age": "30"}


# dictionary["id"] = "lmao" 
# dictionary["key"] = "encryptedkey"


# for thing in dictionary:
#     print(dictionary[thing])

student_grades = {}


off = False

while not off:
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    student_grades[name] = grade
    print("Student added succesfully")
    add_anoother = input("Would you like to add another student? Y or N" ).lower()
    print(student_grades)
    if add_anoother == "y":
        continue
    else:
        off = True





