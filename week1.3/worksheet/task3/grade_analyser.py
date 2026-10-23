# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
filename = input("Enter student file name: ")

# open the file and read the data
with open(filename) as f:
    lines = f.readlines()

# output filename
out_filename = filename + "_out.csv"

# process each student and write results
with open(out_filename, "w") as out:
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        student_id = parts[0]
        # collect only the non-empty grade values
        grades = [int(g) for g in parts[1:] if g.strip() != ""]
        
        # calculate the mean average
        avg = sum(grades) / len(grades)
        
        # determine the classification
        if avg >= 70:
            classification = "1"
        elif avg >= 60:
            classification = "2:1"
        elif avg >= 50:
            classification = "2:2"
        elif avg >= 40:
            classification = "3"
        else:
            classification = "F"
        
        # write out student_id,average_grade,classification
        out.write(f"{student_id},{avg:.2f},{classification}\n")





# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder