"""Build a Log Monitoring System using OOP concepts. Your Python script 
will process a log file, categorize log entries (INFO, WARNING, ERROR), 
and provide various operations, such as filtering logs by type, counting 
occurrences of errors, and exporting logs to a file.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class LogEntry(ABC):
    def __init__(self, timestamp, message):
        self.timestamp = timestamp
        self.message = message

    @abstractmethod
    def display_log(self):
        pass


class InfoLogEntry(LogEntry):
    def display_log(self):
        print(f"[INFO] {self.timestamp}:{self.message}")


class WarningLogEntry(LogEntry):
    def display_log(self):
        print(f"[WARNING] {self.timestamp}:{self.message}")


class ErrorLogEntry(LogEntry):
    def display_log(self):
        print(f"[ERROR] {self.timestamp}:{self.message}")


class LogFileProcessor:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__log = []

    def read_log(self):
        with open(self.__file_path, 'r') as log_file:
            for line in log_file:
                log = self.__process_log_line(line)
                if log:
                    self.__log.append(log)

    def __process_log_line(self, line):
        try:
            timestamp_str, log_level, message = line.strip().split(" ", 2)
            timestamp = datetime.strftime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            if log_level == 'INFO':
                return InfoLogEntry(timestamp, message)
            elif log_level == "WARNING":
                return WarningLogEntry(timestamp, message)
            elif log_level == "ERROR":
                return ErrorLogEntry(timestamp, message)
        except ValueError:
            print(f"Invalid log format:{line}")
            return None

    def filter_logs_by_type(self, log_type):
        filtered_logs = [log for log in self.__log if isinstance(log, log_type)]
        return filtered_logs

    def count_error_logs(self):
        error_logs = self.filter_logs_by_type(ErrorLogEntry)
        return len(error_logs)

    def export_logs(self, log_type, output_file):
        filtered_log = self.filter_logs_by_type(log_type)
        with open(output_file, 'w') as file:
            for log in filtered_log:
                file.write(f"{log.timestamp}{log.message}\n")

    def display_all_logs(self):
        for log in self.__log:
            log.display_log()


def create_sample_log_file():
    sample_log_data = """
2024-09-15 12:00:00 INFO Application started
2024-09-15 12:01:00 WARNING Low memory warning
2024-09-15 12:02:00 ERROR Unable to connect to database
2024-09-15 12:03:00 INFO User login successful
2024-09-15 12:04:00 ERROR File not found
2024-09-15 12:05:00 WARNING Disk space running low
    """
    with open("sample_log.txt", "w") as file:
        file.write(sample_log_data)


def test_log_monitoring_system():
    create_sample_log_file()
    log_processor=LogFileProcessor("Sample_log.txt")

    log_processor.display_all_logs()
    error_count=log_processor.count_error_logs()
    print(f"\n Total number of error logs:{error_count}")
    log_processor.export_logs(ErrorLogEntry,"error_logs.txt")
    print("Error logs have been exported to 'error_logs.txt'")

test_log_monitoring_system()
