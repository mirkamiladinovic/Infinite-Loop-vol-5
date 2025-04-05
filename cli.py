import argparse
from datetime import datetime
from log_utils import *

def main():
    parser=argparse.ArgumentParser(description="Vega Log")
    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--count', action='store_true')
    parser.add_argument('--errors', action='store_true')
    parser.add_argument('--top', action='store_true')
    parser.add_argument('--filter', action='store_true')
    parser.add_argument('--level', type=str, )
    parser.add_argument('--search', type=str, )
    parser.add_argument('--from_date', type=str)
    parser.add_argument('--to_date', type=str)
    parser.add_argument('--sort', action='store_true')
    

    args = parser.parse_args()

    file_path = args.file 
    # argumnti -- count, -errors, --top, --filter

    if args.count:  
        print("Log counts:")
        print(count_log_levels(file_path))

    if args.errors:
        extract_errors_to_file(file_path)

    if args.top:
        print("Top 5")
        top_files = get_top_error_files(file_path)
        for service, count in top_files:
            print(f"{service} {count} ")

    if args.filter:
        date_from = datetime.strptime(args.from_date, '%Y-%m-%d') if args.from_date else None
        date_to = datetime.strptime(args.to_date, '%Y-%m-%d') if args.to_date else None

        logs = filter_logs(
            file_path=file_path,
            level=args.level,
            search_text=args.search,
            date_from=date_from,
            date_to=date_to,
            sort=args.sort
        )
        for log in logs:
            print(f"[{log['timestamp']}] {log['level']} {log['service']} {log['message']}")

if __name__ == "__main__":
    main()
    



