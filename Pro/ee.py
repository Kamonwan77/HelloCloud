import psycopg2
connection = psycopg2.connect(user='webadmin',
                                    password='HESadn49621',
                                    host='node36959-kamonwan.proen.app.ruk-com.cloud',
                                    port='11261',
                                    database='postgres')

                                    
cursor = connection.cursor()


select_copper = 'select copper.Price  from copper'

cursor.execute(select_copper)


Data = cursor.fetchall()


s = []
vb = []
for i in Data:
    for z in i:
        s.append(z)
vb.append(s)
ytyt = vb[0]
print(s)
l = [',']

out_list = [ x.replace(y,'')  for x in s for y in l if y in x ]

print(out_list)





from flask import Flask, render_template

app = Flask(__name__)


data = out_list




@app.route('/')


def chart ():
    chart_data = data
    return render_template("chart.html", chart_data=chart_data)


if __name__ == "__main__":
    app.run(debug=True)