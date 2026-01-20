import sys
import traceback

from PyQt6.QtWidgets import QMessageBox


def global_exception_handler(exc_type, exc_value, exc_traceback):
    """Глобальный обработчик исключений"""
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))

    # Показываем диалог с ошибкой
    show_error("Непридвиденная ошибка", exc_value)


def show_error(error_header:str, e: Exception):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setText(error_header)
    msg.setInformativeText(error_header)

    tb = e.__traceback__
    tb_str = traceback.format_exception(type(e), e, tb)

    msg.setDetailedText(' '.join(tb_str))
    msg.setWindowTitle("Ошибка приложения")
    msg.exec()


# Устанавливаем глобальный обработчик
sys.excepthook = global_exception_handler

