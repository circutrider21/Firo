import sqlite3

class Start(object):
  def __init__(self, dat):
    self.con = sqlite3.connect(dat)
    self.cur = self.con.cursor()
    table_sql = "CREATE TABLE IF NOT EXISTS info (name TEXT NOT NULL UNIQUE, val TEXT NOT NULL)"
    self.cur.execute(table_sql)
  def set(self, name, data):
    try:
      in_sql = "INSERT INTO info(name, val) VALUES (?, ?)"
      self.cur.execute(in_sql, (name, data))
    except:
      raise Exception('The tag {} already exists in this database and can\nonly be overwriten with update(), id 0x6'.format(name)) 
  def get(self, name):
    out_sql = "SELECT val FROM info WHERE name='{}'".format(name)
    try:
      self.cur.execute(out_sql)
      rows = self.cur.fetchall()
      counter = rows[0]
      to_ret = counter[0]
    except:
      raise Exception('{} does not exist in this database\nTherefore can\'t be fetched, id 0x7'.format(name))
    return to_ret
  def remove(self, to_do):
    try:
      remove_sql = "DELETE name, val FROM info WHERE name='{}'".format(to_do)
      self.cur.execute(remove_sql)
    except:
      raise Exception('{} Is Not in this database\nWhich means it can\'t be removed, id 0x8'.format(to_do))

  def version(self):
    value = "1.2"
    return value

  def update(self, name, value):
    try:
      up_sql = "UPDATE info SET name='{}', val='{}' WHERE name='{}'".format(name, value, name)
      self.cur.execute(up_sql)
    except:
      raise Exception("{} Is Not Present in this database\nTherefore it can't be updated, id 0x9".format(name))
