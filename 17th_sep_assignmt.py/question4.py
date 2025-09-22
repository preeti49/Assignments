#Problem 4: unique numbers and stastics

num = input("Enter your numbers: ")
x = num.split() 
print("Numbers are:", x)

# Convert strings to integers
x_int = [int(i) for i in x]

unique = set(x_int)
print("Unique numbers are:", unique)

count = len(unique)
print("Count:", count)

# Total sum
total_sum = sum(unique)
print("Sum:", total_sum)

#average of number
Average = total_sum/len(unique)

print("Average:", Average)

print("Min:", min(unique))
print("Max:", max(unique))
