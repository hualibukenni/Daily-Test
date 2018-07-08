import pymysql

data = {
    'id':'20120001',
    'name':'Bob',
    'age':25
}
db = pymysql.connect(host='localhost',user='root',password='lhyaiwh',port=3306,db='spiders')
cursor = db.cursor()
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('Sucessful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
