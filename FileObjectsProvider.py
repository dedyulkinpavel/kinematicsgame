import csv

import ErrorUtils
from PMStorage import PMObject
import ColorUtils


class FileObjectsProvider():
    def export_pm(self, filename, pm_objects):
        with open(filename, 'w', encoding='utf-8') as f:
            print('id,x,y,fx,fy,color', file=f)
            for elem in pm_objects:
                s = f'{elem.id},{elem.x},{elem.y},{elem.fx},{elem.fy},{ColorUtils.to_str(elem.color)}'
                print(s, file=f)

    def import_pm(self, filename):
      try:
        with open(filename, 'r', encoding='utf-8') as f:
            r = []
            reader = csv.reader(f, delimiter=',')
            h = next(reader)
            for row in reader:
                r.append(PMObject(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),ColorUtils.from_str(row[5])))
        return r
      except Exception as e:
          ErrorUtils.show_error("Импорт", e)

