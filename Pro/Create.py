import psycopg2
try:
    connection = psycopg2.connect(user='webadmin',
                                    password='HESadn49621',
                                    host='node36959-kamonwan.proen.app.ruk-com.cloud',
                                    port='11261',
                                    database='postgres')
    
    connection.autocommit = True


    cursor = connection.cursor()

    sql = '''CREATE database project'''


    cursor.execute(sql)
    print("Datadase created successfully.........")


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")