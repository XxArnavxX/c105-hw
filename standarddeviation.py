import csv
import math

with open('class1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks / total_entries
square = []
for marks in file_data:
    difference = mean - float(marks[1])
    difference = difference**2
    square.append(difference)

sum = 0
for i in square:
    sum = sum + i
print(sum)
result = sum/(len(file_data)-1)
print(result)
standarddeviation = math.sqrt(result)

print(standarddeviation) 