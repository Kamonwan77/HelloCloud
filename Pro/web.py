from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
app = Flask(__name__)

@app.route('/')
def index():
    connection = psycopg2.connect(user='webadmin',
                                    password='HESadn49621',
                                    host='node36959-kamonwan.proen.app.ruk-com.cloud',
                                    port='5432',
                                    database='project')

                                    
    cursor = connection.cursor()

    select_copper = 'select * from copper'

    cursor.execute(select_copper)
    Data = cursor.fetchall()


    return render_template('test.html',DataCopper=Data)
'''

@app.route('/home')
def home():

    return render_template('home.html')
'''
if __name__  == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

