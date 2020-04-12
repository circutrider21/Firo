import sqlite3

class Start(object):
  def __init__(self, dat):
    self.con = sqlite3.connect(dat)
    self.cur = self.con.cursor()
    table_sql = "CREATE TABLE IF NOT EXISTS info (name TEXT NOT NULL UNIQUE, val TEXT NOT NULL)"
    self.cur.execute(table_sql)
  def set(self, name, data):
    in_sql = "INSERT INTO info(name, val) VALUES (?, ?)"
    self.cur.execute(in_sql, (name, data))
  def get(self, name):
    out_sql = "SELECT val FROM info WHERE name='" + name + "'"
    self.cur.execute(out_sql)
    rows = self.cur.fetchall()
    return rows[0]
