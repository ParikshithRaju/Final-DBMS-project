# Nothing to do

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='parikshith',
    password='wasupmynigga',
    database='practice'
)
mycursor = mydb.cursor(buffered=True)
victim = []
crime=[]
class addcriminal:
    def addcrim(self,res,file):
            if res:
                mycursor.execute(
                    "select crime_id from crime order by crime_id desc limit 1")
                r = mycursor.fetchall()

                crime.append(r[0][0])

                for val in res.values():
                    crime.append(val)
                crime[5]=file.replace(' ','_')
                crime[6]=res['cadhar']
                formula = "insert into criminals(crime_id,first,last,address,gender,photo,adhar_number) values(%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(formula, crime)
                crime.clear()
                mydb.commit()    

class addvictim:
    def addvi(self, res, file):
        if res:
            mycursor.execute(
                "select crime_id from crime order by crime_id desc limit 1")
            r = mycursor.fetchall()

            victim.append(r[0][0])

            for i in res.values():
                victim.append(i)
            victim[5]=file.replace(' ','_')
            victim[6]=res['adhar_number']
            formula = "insert into victims(crime_id,first,last,address,gender,photo,adhaar_number) values(%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(formula, victim)
            victim.clear()
            mydb.commit()



crime = []


class addcrime:
    def addcr(self, res):
        if res:
            for val in res.values():
                crime.append(val)
            sqlformula = 'insert into crime(location,date,dept,crime_type) value(%s,%s,%s,%s)'
            mycursor.execute(sqlformula, crime[:4])
            mydb.commit()
            crime.clear()

class getview:
    def get(self, res):
        datastr = 'select * from crime where '
        if res['location']:
        
            lval = res['location']
            datastr += ('location="'+lval+'" and ')
        if res['start_date']:
            sdval = res['start_date']
            datastr += ('date>"'+sdval+'" and ')
        if res['end_date']:
            edval = res['end_date']
            datastr += ('date<"'+edval+' "and ')
        if res['dept']:
            dval = res['dept']
            datastr += ('dept="'+dval+'" and ')
        if res['Id']:
            ival = res['Id']
            datastr += ('crime_id='+ival+' and ')
        if res['Type']:
            cval = res['Type']
            datastr += ('crime_type="'+cval+'   "and ')

        vicstr=mycursor.execute('select * from victims;')
        v=mycursor.fetchall()
        datastr=datastr[:-4]
        print(vicstr)
        datastr += ';'
        print(datastr)
        mycursor.execute(datastr)
        r = mycursor.fetchall()
        for i in r:
                print(i)
        mycursor.execute('select * from criminals;')
        c=mycursor.fetchall()
        return r,v,c