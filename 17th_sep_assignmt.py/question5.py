#Master list of all roll numbers
master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # example roll numbers

# Read attendance from file
with open(r"C:\Users\DELL\OneDrive\Documents\GitHub\Assignments\17th_sep_assignmt.py\attendance.txt", "r") as file:
    attended = file.read().splitlines()
    attended = [int(roll) for roll in attended]  # convert to integers

# Compare and find present and absent students
present = [roll for roll in master_list if roll in attended]
absent = [roll for roll in master_list if roll not in attended]

# Print results
print("Present students:", present)
print("Absent students:", absent)

# Save absent students to absent.txt
with open(r"C:\Users\DELL\OneDrive\Documents\GitHub\Assignments\17th_sep_assignmt.py\absent.txt", "w") as file:
    for roll in absent:
        file.write(str(roll) + "\n")
                