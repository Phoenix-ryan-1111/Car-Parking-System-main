import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="Anshi@2002", database="CarParkingsystem")
mycur = conn.cursor()

def SqlConnectivity_Login(query1):
    mycur.execute(query1)
    result1 = mycur.fetchone()
    return result1

def SqlConnectivity_Insert(query):
    try:
        mycur.execute(query)
        conn.commit()
        return 0 ##returns nothing
    except Exception as e:
        return e

def SqlConnectivity_Insert1(query1):
    try:
        mycur.execute(query1)
        conn.commit()
        return mycur.rowcount ## rowcount will return number of lines effected ## means answer will be 1 one row effected
    except Exception as e:
        return e


def SqlConnectivity_Update_record(query1, query2):
    mycur.execute(query1)
    result = mycur.fetchone()  ## method returns a single record from table
    if not result:
        return result
    else:
        mycur.execute(query2)
        conn.commit()## will comit changes to the table
        return result

def SqlConnectivity_Update_record1(query1):
    x1= 1
    try:
        mycur.execute(query1)
        conn.commit()
    except Exception as e:
        x1=0
    return mycur.rowcount

def SqlConnectivity_Delete_Record(query):
    x=1
    try:
        mycur.execute(query)
        conn.commit()
    except Exception as e:
        x=0
    return mycur.rowcount

def Auto_Fill(query1):
    mycur.execute(query1)
    result1 = mycur.fetchone()  ## method returns a single record from table
    return result1
   
        
def SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query):
    mycur.execute(query)
    result = mycur.fetchall()    ## to fetch all the rows from the database
    return result





