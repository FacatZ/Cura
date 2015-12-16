
import sqlite3

class SqliteHelper(object):
	'''
	this sqlite3 helper class only provide the read (namely, select) functionality,
	and without any exception handling to save time
	'''
	
	db_file = ''
	conn = None
	cursor = None
	
	def __init__(self, file):
		self.db_file = file
		self.conn = sqlite3.connect(self.db_file)
		self.conn.row_factory = sqlite3.Row
		self.cursor = self.conn.cursor()
	
	def select_cmd(self, sqlcmd):
		return self.cursor.execute(sqlcmd)
		
	def select_cmd_data(self, cmd, data):
		return self.cursor.execute(cmd, data)
	
		