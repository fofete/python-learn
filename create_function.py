def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 5, 7, 8, 121]))


#...........


def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temperatures = [16.3, 12.2, 19.5]
student_grades = {"Marcos": 10, "Lucía": 8.8, "Alberto": 3.3}

print(mean(student_grades))



