import re
from collections import Counter, defaultdict
from datetime import datetime

LOG_PATTERN = re.compile(r'^\[(.*?)\]\s+(DEBUG|INFO|WARNING|ERROR)\s+([^\s]+)\s+(.*)$')

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    timestamp, level, service, message = match.groups()
    return {
        'timestamp': timestamp,
        'level': level,
        'service': service,
        'message': message.strip()
    }


def count_log_levels(file_path):
    res={}
    with open(file_path, 'r') as f:
        for line in f:
            log = parse_log_line(line)
            if log:
                if log['level'] in res:
                    res[log['level']] += 1
                else:
                    res[log['level']] = 1
    return res
    


def get_error_files(file_path): #fajl sa najvise gresaka ima najveci prioritet 
    res={}
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            log = parse_log_line(line)
            if log and log['level'] == 'ERROR':
                if log['service'] in res:
                    res[log['service']] += 1
                else:
                    res[log['service']] = 1
                    
    return res

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

def get_top_error_files(file_path):
    error_files= get_error_files(file_path)
    sorted_files=sort_dict_by_value(error_files)
    top_files = list(sorted_files.items())[:5]  
    
    return top_files

def extract_errors_to_file(file_path, output_path='error_logs.txt'):
    with open(file_path, 'r') as f_in, open(output_path, 'w') as f_out:
        for line in f_in:
            log = parse_log_line(line)
            if log and log['level'] == 'ERROR':
                f_out.write(line)

def filter_logs(file_path, level=None, search_text=None, date_from=None, date_to=None, sort=False):
    results = []
    with open(file_path, 'r') as f:
        for line in f:
            log = parse_log_line(line)
            if not log:
                continue
            log_time = datetime.strptime(log['timestamp'], '%Y-%m-%d %H:%M:%S.%f')

            if level and log['level'] != level:
                continue
            if search_text and search_text.lower() not in log['message'].lower():
                continue
            if date_from and log_time < date_from:
                continue
            if date_to and log_time > date_to:
                continue

            results.append(log)

    if sort:
        results.sort(key=lambda l: l['timestamp'])

    return results

# print(count_log_levels('novi.txt'))
print(get_top_error_files('novi.txt'))
# print(extract_errors_to_file('novi.txt'))