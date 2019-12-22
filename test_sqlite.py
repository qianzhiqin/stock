import sqlite3

conn = sqlite3.connect('stock.db')
print("Opened database successfully")
cursor = conn.cursor()
# c.execute('''create table stock
#      (
#        id         INTEGER not null
#          constraint table_name_pk
#            primary key autoincrement,
#        stock      VARCHAR,
#        type       VARCHAR,
#        price      REAL,
#        source     VARCHAR,
#        userid     VARCHAR,
#        user       VARCHAR,
#        date       VARCHAR,
#        proportion VARCHAR,
#        createTime VARCHAR
#      );''')
print("Table created successfully")

# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");
#
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
#
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
#
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

# date = "2019-12-19"
# stock = "1"
# user = "张三"
# proportion = "9"
# type ="买"
#
# select_sql = "select * from stock where stock=? and type=? and user=? and date = ?  and proportion=?"
# inset_sql = " insert into stock  (stock,type,price,source,userid,user,date,createTime,proportion) values (?,?,?,?,?,?,?,?,?)"
# stock1 = "2"
# type1 = "卖"
# price1 = 2
# source1 = "eastmoney"
# userid1 = "234"
# user1 = "sdfsd"
# createTime1 = "2019-12-19 01:00:00"
# proportion1 = "8"
#
# cursor = c.execute(select_sql, (stock, type, user, date, proportion))
# print(cursor.arraysize)
# for row in cursor:
# 	print("222:" + str(row[0]))
# if cursor.__sizeof__() == 0:
# 	c.execute(inset_sql, (stock1, type1, price1, source1, userid1, user1, date, createTime1, proportion1))
insert_sql = "insert into user (userId,user,source,success,createTime,updateTime) values (?,?,?,?,?,?)"

user_id = "1"
user = "1"
proportion = "1"
create_time = "1"
update_time = "1"
source = "1"
# execute = cursor.execute(insert_sql, [user_id, user, source, proportion, create_time, update_time])
# execute = cursor.execute(insert_sql, ("1","1","1","1","1","1"))
execute = cursor.execute('insert into user (id,userId,user,source,success,createTime,updateTime) values ( 1,"1","1","1","1","1","1")')
print(execute)
conn.commit()
conn.close()
