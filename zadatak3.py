new_file = open("error_lines.txt","a")

with open('vegini_logovi.txt', 'r') as file:
    for line in file:
        if "ERROR" in line:
            new_file.write(line)

new_file.close()
file.close()

