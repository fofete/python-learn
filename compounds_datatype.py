student_grades = {"Marcos": 9.7, "Carlos": 5.5, "Hernan": 7.8}

mysum = sum(student_grades.values())
length = len(student_grades.keys())
resultado = mysum / length

print(resultado)

#------------------ 

def mean(grades):
    if type(grades) == dict:
        the_mean = sum(value.values()) / len(value)
        return the_mean

print(mean(student_grades))