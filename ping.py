# -*- coding:utf-8 -*-
import pymysql
import os
import time

def get_loan_number(file):
    connect = pymysql.connect(
        host="localhost",
        port=3306,
        user="ping",
        passwd="bLSbNxbWJAGjjba5",
        db="ping",
        charset='utf8'
    )
    cursor = connect.cursor() #获取游标
    sql = "select ipaddress from ip_table"  #执行的sql
    cursor.execute(sql) #执行数据库操作
    number = cursor.fetchall() #查询并返回所有结果
    fp = open(file, "w")
    loan_count = 0
    for loanNumber in number:
        loan_count += 1
        fp.write(loanNumber[0] + "\n")
    fp.close()
    f = os.system('sh fping.sh')
 
    content = open('result.txt','r')
    first= content.read().split('\n')  #通过指定分隔符对字符串进行切片
    for i in range(0,len(first)-1):
         tmp = first[i]
         ip = tmp[:tmp.index('is')-1]
         status = '1'
         if 'unreachable' in tmp:
             status = '0'
         cursor.execute('update ip_table set status="%s" where ipaddress="%s"'%(status,ip))
    connect.commit()
    content.close()
    cursor.close()  #关闭指针对象
    connect.close() #关闭数据库连接

if __name__ == "__main__":
    while True:
        get_loan_number(r"ip.txt")
        time.sleep(3)