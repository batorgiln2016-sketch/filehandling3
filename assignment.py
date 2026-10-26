# You can remove 'pass' if you written code in the function
# Exercise 1

def read_line(filename, line_number):
    if line_number <= 0:
        return ""
    file = open(filename, "r")
    current_line = 1
    for i in range(line_number):
        line = file.readline()
        if line == "":
            file.close()
            return ""
        if current_line == line_number:
            file.close()
            return line.strip("\n")
        current_line = current_line + 1
    file.close()
    return ""
print(read_line("days.txt", 2))
# Exercise 2
def reverse_lines(source, destination):
    # Write your code here
    pass

# Exercise 3
def merge_files(first, second, destination):
    # Write your code here
    pass

# Exercise 4
def find_score(filename, name):
    # Write your code here
    pass

# Exercise 5
def update_score(filename, name, new_score):
    # Write your code here
    pass
