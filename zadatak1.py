debug = 0
info = 0
warning = 0
error = 0
with open('vegini_logovi.txt', 'r') as file:
    for line in file:
        if "DEBUG" in line:
            debug = debug + 1
        if "INFO" in line:
            info = info + 1
        if "WARNING" in line:
            warning = warning + 1
        if "ERROR" in line:
            error = error + 1

    print(debug,info,warning,error)

file.close()

