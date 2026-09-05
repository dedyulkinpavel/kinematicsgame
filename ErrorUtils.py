import logging
import sys
import os

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def global_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

def show_error(error_header: str, e: Exception):
    logging.error(f"{error_header}: {str(e)}")

def clear_log_file(log_file_path: str, max_lines: int = 500):
    """
    Очищает файл логов, если количество строк превышает max_lines.
    """
    if not os.path.exists(log_file_path):
        return

    with open(log_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if len(lines) > max_lines:
        with open(log_file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines[-max_lines:])
