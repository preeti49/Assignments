#Problem 2:- Word Frequency Filter
n = int(input("Enter number: "))
words = {}

with open(r"C:\Users\DELL\OneDrive\Documents\GitHub\Assignments\17th_sep_assignmt.py\story.txt", "r") as f:
    for line in f:
        for word in line.split():
            words.append(word)

            

for w in words:
    if words[w] > n:
        print(w, words[w])