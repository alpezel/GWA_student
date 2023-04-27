#Write a Python program that read a file containing the name of 20 students
#together with their GWA. The program will outputs the name of the student 
#who got the highest GWA (including the GWA).

#initial value of highest gwa and students name
highest_gwa= 0
highest_gwa_name= ""
# open students_gwa.txt (read)
with open("students_gwa.txt") as students_gwa_file:
    # read students_gwa.txt each line
    for line in students_gwa_file:
        input_name, input_gwa = line.split()
        # minus 5.0 to input_gwa that will be converted to float
        input_gwa= 5.0 - float(input_gwa)

print(input_gwa)