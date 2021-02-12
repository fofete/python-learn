#for list

monday_temperatures = [9.1, 2.3, 5.5, 8.6, 7.3, 4.23]

for temperatures in monday_temperatures:
    print(round(temperatures))





#for dict:

student_grades = {"Carlos": 2.3, "Samuel": 6.7, "Laura": 9.9}

for grades in student_grades.items():
    print(grades)




#combine a dictionary

phone_numbers = {"Sonirico": "+37682929928", "Homer": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))