import pymysql
data = {
    'id':'20120003',
    'name':'Bob',
    'age':25
}
db = pymysql.connect(host='localhost',user='root',password='lhyaiwh',port=3306,db='spiders')
cursor = db.cursor()
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s']*len(data))
sql =   'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('Succesful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
