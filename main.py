import sys
import uuid

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView, QFileDialog

from Aboutdialog import Aboutdialog
from DataProvider import DataProvider
from EditPMObjectDialog import EditPMObject
from FileObjectsProvider import FileObjectsProvider
from PGParameters import PGParameters
from PMStorage import PMObject
from PMTableModel import PMTableModel
from logic import logic


class ParametersWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui/mainwindow.ui", self)  # Загружаем дизайн
        self.runPGbutton.clicked.connect(self.run_pg)

        self.set_pm_objects_table_view()

        self.addPmObjectButton.clicked.connect(self.add_pm)
        self.deletePmObjectButton.clicked.connect(self.del_pmobject)
        self.editPmObjectButton.clicked.connect(self.clear_all)
        self.saveBDbutton.clicked.connect(self.save_bd)
        self.importBDbutton.clicked.connect(self.load_bd)

        self.exportPmObjectButton.clicked.connect(self.export_csv)
        self.importPmObjectButton.clicked.connect(self.import_csv)
        self.aboutMenuItem.triggered.connect(self.about)

    def showEvent(self, a0):
        super().showEvent(a0)

        self.refresh_objects_grid()
        self.load_pg_parameters()

    def load_pg_parameters(self):
        pgParameters = DataProvider().load_pg_parameters()
        self.pmGspinBox.setValue(pgParameters[0][0])
        self.pmFRspinBox.setValue(pgParameters[0][1])
        self.pgWidthSpinBox.setValue(pgParameters[0][2])
        self.pgHeightSpinBox.setValue(pgParameters[0][3])
        self.pmFpsSpinBox.setValue(pgParameters[0][4])

    def set_pm_objects_table_view(self):
        self.pmObjectsViewModel = PMTableModel()
        tableView = self.gridPmObjects
        tableView.setModel(self.pmObjectsViewModel)
        tableView.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)  # Выделение целых строк
        tableView.setSelectionMode(QTableView.SelectionMode.SingleSelection)  # Одиночное выделение
        tableView.setAlternatingRowColors(True)  # Включаем встроенное чередование цветов
        # Настройка заголовков
        header = tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # Растягивание столбцов
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        # Вертикальный заголовок скрываем
        tableView.verticalHeader().setVisible(False)

    def add_pm(self):
        dialog = EditPMObject()
        dialog.setModal(True)
        dialog.onAcceptSignal.connect(self.on_add)
        dialog.exec()

    def about(self):
        dialog = Aboutdialog()
        dialog.exec()

    def save_bd(self):
        g = self.pmGspinBox.value()
        f = self.pmFRspinBox.value()
        w = self.pgWidthSpinBox.value()
        h = self.pgHeightSpinBox.value()
        fps = self.pmFpsSpinBox.value()

        logic.save(PGParameters(g, f, w, h, fps))

    def export_csv(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            'Экспортировать в файл',
            '.',
            'CSV (*.csv);;Все файлы (*)'
        )
        if file_name == "": return
        FileObjectsProvider().export_pm(file_name, logic.pmStorage.listOjects)

    def import_csv(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            'Импортировать файл',
            '.',
            'CSV (*.csv);;Все файлы (*)'
        )
        if file_name == "": return
        logic.pmStorage.reset(FileObjectsProvider().import_pm(file_name))
        self.refresh_objects_grid()

    def clear_all(self):
        logic.pmStorage.reset([])
        self.refresh_objects_grid()

    def load_bd(self):
        logic.load()
        self.refresh_objects_grid()
        self.load_pg_parameters()

    def on_add(self, x, y, fx, fy, color):
        pmob = PMObject(str(uuid.uuid4()), x, y, fx, fy, color)
        self.pmObjectsViewModel.add_pm_object(pmob)

    def del_pmobject(self):
        selected_indexes = self.gridPmObjects.selectionModel().selectedRows()
        if selected_indexes:
            for row_index in selected_indexes:
                row = self.pmObjectsViewModel.raw_data(row_index)
                self.pmObjectsViewModel.remove_pm_object(row_index.row())

    def refresh_objects_grid(self):
        self.pmObjectsViewModel.update_data(logic.pmStorage.listOjects)

    def run_pg(self):
        g = self.pmGspinBox.value()
        f = self.pmFRspinBox.value()
        w = self.pgWidthSpinBox.value()
        h = self.pgHeightSpinBox.value()
        fps = self.pmFpsSpinBox.value()
        logic.run_pygame(PGParameters(g, f, w, h, fps))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ParametersWindow()
    ex.show()
    sys.exit(app.exec())
