subjects =["maths","english","pe","history","geography"]
marks=[]
for subject in subjects:
    mark = int(input(f"Enter marks in {subject}: "))
    marks.append(mark)
print("Marks",marks)