import mysql.connector as c
con = c.connect(user = 'root', host = "localhost", passwd = "admin")
cur = con.cursor()
cmd= "create database if not exists blood_bank"
cur.execute(cmd)
con.commit()
cmd = "use blood_bank"
cur.execute(cmd)
cmd ="create table if not exists bank(blood_type varchar(100), qty int(100))"
cur.execute(cmd)
con.commit()
cmd = "create table if not exists user(name varchar(200), blood_type varchar(200))"
cur.execute(cmd)
con.commit()
ls = ["A+","B+","AB+","O+","A-","B-","AB-","O-"]
for i in ls:
    cmd = "insert into bank values('{}', 0)".format(i)
    cur.execute(cmd)
    con.commit()
