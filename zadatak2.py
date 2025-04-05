
list = []
with open('vegini_logovi.txt', 'r') as file:
    for line in file:
        if "ERROR" in line:
            words = line.split(" ")
            for w in words:
                if ".cs" in w:
                    list.append(w.strip(":"))
                    if len(list)==5:
                        file.close()
                        print(list)
                        exit()


