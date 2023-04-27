#Write a Python program that read a file containing the name of 20 students
#together with their GWA. The program will outputs the name of the student 
#who got the highest GWA (including the GWA).

# open students_gwa.txt (read)
with open("students_gwa.txt") as students_gwa_file:
    # read students_gwa.txt each line
    for line in students_gwa_file:
        input_name, input_gwa = line.split()
        input_gwa= float(input_gwa)
    
    #gwa= []
    #gwa.append(input_gwa)
    print (input_gwa)