import pymysql

class MysqlHelper:
	'''python操作mysql的增删改查的封装'''
	
	def __init__(self, host='localhost', user='root', password='qq84607952', database='walle', port=3306, charset='utf8'):
		'''
		初始化参数
		:param host: 主机
		:param user: 用户名
		:param password: 密码
		:param database: 数据库
		:param port: 端口号，默认是3306
		:param charset: 编码，默认是utf8
		'''
		self.host = host
		self.port = port
		self.database = database
		self.user = user
		self.password = password
		self.charset = charset
	
	def connect(self):
		'''
		获取连接对象和执行对象
		:return:
		'''
		self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
		                            port=self.port, charset=self.charset)
		
		self.cur = self.conn.cursor()
	
	def fetchone(self, sql, params=None):
		'''
		根据sql和参数获取一行数据
		:param sql: sql语句
		:param params: sql语句对象的参数元组，默认值为None
		:return: 查询的一行数据
		'''
		dataOne = None
		try:
			count = self.cur.execute(sql, params)
			if count != 0:
				dataOne = self.cur.fetchone()
		except Exception as ex:
			print(ex)
		return dataOne
	
	def fetchall(self, sql, params=None):
		'''
		根据sql和参数获取一行数据
		:param sql: sql语句
		:param params: sql语句对象的参数列表，默认值为None
		:return: 查询的一行数据
		'''
		dataall = None
		try:
			count = self.cur.execute(sql, params)
			if count != 0:
				dataall = self.cur.fetchall()
		except Exception as ex:
			print(ex)
		return dataall
	
	def __item(self, sql, params=None):
		'''
		执行增删改
		:param sql: sql语句
		:param params: sql语句对象的参数列表，默认值为None
		:return: 受影响的行数
		'''
		count = 0
		try:
			count = self.cur.execute(sql, params)
			self.conn.commit()
		except Exception as ex:
			print(ex)
		return count
	
	def update(self, sql, params=None):
		'''
		执行修改
		:param sql: sql语句
		:param params: sql语句对象的参数列表，默认值为None
		:return: 受影响的行数
		'''
		return self.__item(sql, params)
	
	def insert(self, sql, params=None):
		'''
		执行新增
		:param sql: sql语句
		:param params: sql语句对象的参数列表，默认值为None
		:return: 受影响的行数
		'''
		return self.__item(sql, params)
	
	def delete(self, sql, params=None):
		'''
		执行删除
		:param sql: sql语句
		:param params: sql语句对象的参数列表，默认值为None
		:return: 受影响的行数
		'''
		return self.__item(sql, params)
	
	def close(self):
		'''
		关闭执行工具和连接对象
		'''
		if self.cur != None:
			self.cur.close()
		if self.conn != None:
			self.conn.close()


if __name__ == '__main__':
	
	data = None
	if data:
		print(1)
	else:
		print(2)
	
	# 初始化对象
	helper = MysqlHelper('okaiok.com', 'root', 'qq84607952', 'walle')
	# 连接
	helper.connect()
	# sql
	sql = 'select * from user '
	# params
	params = ['小茗', 1]
	# 执行
	data = helper.fetchall(sql)
	# 判断
	if data:
		for temp in data:
			print(temp)
	else:  # None,False,0
		print('没有数据.')
	
	helper.close()