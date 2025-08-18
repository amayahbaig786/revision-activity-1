marks = []
for i in range(5):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)