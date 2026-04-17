with open('students.txt', 'w') as f:
    f.write('Name: Shreyas, Marks: 100/n')
    f.write('Name: Virat, Marks: 99/n')
    f.write('Name: Dhoni, Marks: 111/n')

print('Data written successfully!')
#reading data from a file
with open('students.txt', 'r') as f:
    content = f.read()
print('File content:/n', content)
