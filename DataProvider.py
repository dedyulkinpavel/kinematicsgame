import sqlite3

import ColorUtils
from PMStorage import PMObject

def save_pm_elem(cur, pm_object):
   cur.execute("""
       INSERT INTO pm_objects (id, x, y, fx, fy, color)
       VALUES (?, ?, ?,?,?,?)
       ON CONFLICT(id) DO UPDATE SET
           x = excluded.x,
           y = excluded.y,
           fx = excluded.fx,
           fy = excluded.fy,
           color = excluded.color
   """, (pm_object.id, pm_object.x,pm_object.y,pm_object.fx,pm_object.fy, pm_object.color))

def save_pg_parameters(cur, pg_parameters):
   cur.execute("""
       INSERT INTO parameters (g, friction, width, height, fps)
       VALUES (?, ?, ?,?,?)
   """, (pg_parameters.g, pg_parameters.f, pg_parameters.w, pg_parameters.h,pg_parameters.fps))



class DataProvider:
    def __init__(self):
        self.db = "./db/pymunk.db"


    def save(self, pm_objects, pg_parameters):
        con = sqlite3.connect(self.db)
        cur = con.cursor()

        cur.execute("""delete from parameters""")
        save_pg_parameters(cur, pg_parameters)

        cur.execute("""delete from pm_objects""")
        for elem in pm_objects:
            save_pm_elem(cur, elem)

        con.commit()
        con.close()

    def load_pm_objects(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        result = cur.execute("""select id, x, y, fx, fy, color from pm_objects""").fetchall()

        pm_objects = []
        for elem in result:
            pm_objects.append(PMObject(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5]))

        con.close()

        return pm_objects

    def load_pg_parameters(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        result = cur.execute("""select g,friction,width,height,fps from parameters""").fetchall()
        con.close()

        if len(result) ==0:
           return [[1400,0.8,600,800,120]]

        return result






