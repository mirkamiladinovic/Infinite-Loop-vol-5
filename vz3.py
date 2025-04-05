def extract_error_lines(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            if "ERROR" in line:
                outfile.write(line)

if __name__ == "__main__":
    extract_error_lines("VEGINDIO/vegini_logovi.txt", "VEGINDIO/error_logs.txt")
