import re
import string
from datetime import datetime


def filter_by_log_type():
    print("Unesite tip loga koji zelite da filtrirate:")
    log_type = input()
    with open('vegini_logovi.txt', 'r') as file:
        for line in file:
            if log_type in line:
                print(line)

    file.close()
def search_text():
    print("Unesite text po kojem pretrazujete:")
    text = input()
    with open('vegini_logovi.txt', 'r') as file:
        for line in file:
            if text in line:
                print(line)

    file.close()

def filter_time():
    print("Unesite prvi datum:")
    first_date = input()
    print("Unesite drugi datum:")
    second_date = input()


    with open('vegini_logovi.txt', 'r') as file:
        for line in file:
            date = line[1:24]
            if date>= first_date and date <= second_date:
                print(line)
    file.close()



def limit():
    print("Unesite limit:")
    limit = input()
    with open('vegini_logovi.txt', 'r') as file:
        for i, line in enumerate(file):
            if i < int(limit):
                print(line)

    file.close()

def offset():
    print("Unesite offset:")
    offset = input()
    with open('vegini_logovi.txt', 'r') as file:
        for i, line in enumerate(file):
            if i >= int(offset):
                print(line)

    file.close()

def sort_function(line):
    return line[1:24]

def sort_date_time():
    lines = []
    with open('vegini_logovi.txt', 'r') as file:
        for line in file:
            lines.append(line)

    lines.sort(key=sort_function)
    for line in lines:
        print(line)   
    file.close()

sort_date_time()
#limit()
#filter_by_log_type()
#filter_time()
#search_text()
#offset()
