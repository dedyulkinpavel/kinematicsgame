from PyQt6.QtCore import QModelIndex, QAbstractTableModel, Qt


def map_shape(value):
    match value:
        case 0:
            return "SQUARE"
        case 1:
            return "CIRCLE"
        case 2:
            return "TRIANGLE"
        case 3:
            return "HEXAGON"


class PMTableModel(QAbstractTableModel):
    def __init__(self, pm_objects=None):
        super().__init__()
        self.pm_objects = pm_objects or []
        self._headers = ["X", "Y", "FX", "FY", "El", "SHAPE", "SIZE"]

    def rowCount(self, parent=QModelIndex()):
        return len(self.pm_objects)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def raw_data(self, index):
        if not index.isValid() or not (0 <= index.row() < len(self.pm_objects)):
            return None

        return self.pm_objects[index.row()]


    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self.pm_objects)):
            return None

        pm_object = self.pm_objects[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:
                return str(pm_object.x)
            elif index.column() == 1:
                return str(pm_object.y)
            elif index.column() == 2:
                return str(pm_object.fx)
            elif index.column() == 3:
                return str(pm_object.fy)
            elif index.column() == 4:
                return str(pm_object.el)
            elif index.column() == 5:
                return map_shape(pm_object.shape)
            elif index.column() == 6:
                return str(pm_object.size)

        elif role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

        return None


    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        return None

    def update_data(self, pm_objects):
        self.beginResetModel()
        self.pm_objects = pm_objects
        self.endResetModel()

    def add_pm_object(self, pm_object):
        row = len(self.pm_objects)
        self.beginInsertRows(QModelIndex(), row, row)
        self.pm_objects.append(pm_object)
        self.endInsertRows()

    def remove_pm_object(self, row):
        if 0 <= row < len(self.pm_objects):
            self.beginRemoveRows(QModelIndex(), row, row)
            self.pm_objects.pop(row)
            self.endRemoveRows()
