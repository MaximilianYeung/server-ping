from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
import pymysql
app = Flask(__name__)
bootstrap = Bootstrap(app)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    status = request.args.get('status')
    conn = pymysql.connect(host="localhost",
        port=3306,
        user="ping",
        passwd="bLSbNxbWJAGjjba5",
        db="ping",
        charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM ip_table"
    if status != "":
        sql += ' where status = "%s"'%(status)
    cur.execute(sql)
    data = cur.fetchall()
    conn.close()
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)