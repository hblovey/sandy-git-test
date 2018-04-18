#coding=utf-8
import pymysql

def get_userinfo():
    key_list=['user','password']
    user_list=[]
    data_list=[]
    conn=pymysql.connect(
        port=3306,
        database='test',
        user='root',
        passwd='root',
        host='localhost')
    cur=conn.cursor()
    aa=cur.execute('select * from tb1')
    value=cur.fetchmany(aa)
    for i in value:
        user_list.append(list(i))
        for k in user_list:
            tmp=zip(key_list,k)
        data_list.append(dict(tmp))
    cur.close()
    conn.commit()
    conn.close()
    return data_list

if __name__=='__main__':
    re=get_userinfo()
    print(re)



