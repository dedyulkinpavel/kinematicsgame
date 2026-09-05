import logging
import sys
import os
from logging.handlers import RotatingFileHandler

# Настройка логирования
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
LOG_FILE = 'app.log'
MAX_LOG_SIZE = 1_000_000  # 1 MB
BACKUP_COUNT = 3

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        RotatingFileHandler(
            LOG_FILE,
            maxBytes=MAX_LOG_SIZE,
            backupCount=BACKUP_COUNT,
            encoding='utf-8'
        ),
        logging.StreamHandler()
    ]
)

def global_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

def show_error(error_header: str, e: Exception):
    logging.error("%s: %s (%s)", error_header, e, type(e).__name__)

def clear_log_file(log_file_path: str, max_lines: int = 500):
    """
    Очищает файл логов, если количество строк превышает max_lines.
    Функция оставлена для обратной совместимости; при использовании
    RotatingFileHandler ручная очистка не требуется.
    """
    if not os.path.exists(log_file_path):
        return

    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if len(lines) > max_lines:
            with open(log_file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines[-max_lines:])
    except OSError as e:
        logging.warning("Не удалось очистить лог-файл %s: %s", log_file_path, e)
