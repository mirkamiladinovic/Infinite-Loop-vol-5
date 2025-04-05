
# Log Analyzer Application

This application is designed for analyzing log files. It allows you to load logs, filter them based on various criteria, and export errors.

## Description

The application loads a text log file, parses it, displays logs in a text area, and provides various tools for analysis:

- Filtering by text, log type, and date.
- Counting the number of logs for each log type.
- Showing the top 5 problematic files based on error count.
- Exporting all errors to a separate file.

---

## Installation

To run the application, you need Python 3.7 or higher. Follow these steps to install and run:

1. Clone the repository:
   ```bash
   git clone https://github.com/mirkamiladinovic/Infinite-Loop-vol-5.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Infinite-Loop-vol-5
   ```

3. Change current branch to AVG:
   ```bash
   git checkout AVG
   ```

4. Install virtual environment:
   MacOS/Linux
   ```bash
   python3 -m venv .venv
   ```
   Windows
   ```bash
   python -m venv .venv
   ```

5. Install all dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

1. To start the application, run the following command:
   ```bash
   python main.py
   ```

2. A GUI window will open where you can load log files and use the various functions.

---

## Usage

### Loading Logs

1. Click the **"Load Log File"** button and select a text log file (with the `.txt` extension).
2. After loading, the logs will be automatically parsed and displayed in the text area.

### Counting Log Types

1. Click the **"Count Types"** button to see the count of each log type (DEBUG, INFO, WARNING, ERROR).

### Top 5 Problematic Files

1. Click the **"Top 5 Problem Files"** button to get a list of files with the highest number of errors.

### Exporting Errors

1. Click the **"Export ERROR Logs"** button to export all logs with the `ERROR` type into a file called `errors_only.txt`.

### Sorting logs by Date (Asc/Desc)

1. Click the **"Sort by Date"** button to sort logs by date (ascending or descending).

### Filtering

1. In the **"Filters"** section:
   - **Search Text**: Enter text to search within the log messages.
   - **Log Type**: Choose a log type to filter (e.g., `ERROR`, `INFO`, etc.).
   - **From Date / To Date**: Specify a date range to filter the logs.
   - **Limit**: Specify the maximum number of logs to display.
   - **Offset**: Specify an offset for the logs displayed.

2. Click **"Apply Filters"** to apply the filters.

---

## Requirements

- Python 3.7+
- Libraries:
  - `tkcalendar==1.6.1`

---

## Notes

- Logs should be in the following format:
  ```
  [YYYY-MM-DD HH:MM:SS.mmm] LOG_LEVEL FILENAME: message
  ```
- The program ignores parsing errors if the date or log format is incorrect.
