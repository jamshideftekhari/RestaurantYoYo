from flask import Flask, render_template, request, redirect, url_for
from mySqlConnector import MySqlConnector

app = Flask(__name__)

localHost = "localhost"
user = "root"
pw = "jam2003eft" 
db = "resturantyoyosimple"                   
dbconnection=MySqlConnector(localHost, user, pw, db)
dbconnection.connect()
query = "SELECT * FROM resturantyoyosimple.resturant"

@app.route('/')
def Welcome():
    return """  <h1> Welcome to Resturant yoyo test page </h1>
                <h2> <a href="/delivery"> delivery page </a> </h2>
                <h2> <a href="/pos"> point of sale </a> </h2>
                <h2> <a href="/marketing"> Marketing Interface </a> </h2>
                <h2> <a href="/pos2"> point of sale with layout </a> </h2>"""
                
@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/pos')
def pos():
    return render_template('pos.html')

@app.route('/pos2')
def pos2():
    return render_template('PosWithCss.html')

@app.route('/marketing')
def marketing():
    return render_template('marketing.html')

@app.route('/deliverer')
def deliverer():
    return render_template('deliverer.html')

@app.route('/resturant')
def resturant():
    resturants1 = ['yoyo', 'yoyo2', 'yoyo3']
    resturants2 = [('yoyo', 'adress', 'phone number', 'Email'),
                   ('yoyo2', 'adress2', 'phone number 2', 'Email 2'), 
                   ('yoyo3', 'adress3', 'phone number 3', 'Email 3')]
    resturants = dbconnection.queryDB(query)
    return render_template('resturant.html', r1=resturants1, r2=resturants2, r3=resturants)

@app.route('/resturantBS')
def resturantBS():
    resturants1 = ['yoyo', 'yoyo2', 'yoyo3']
    resturants2 = [('yoyo', 'adress', 'phone number', 'Email'),
                   ('yoyo2', 'adress2', 'phone number 2', 'Email 2'), 
                   ('yoyo3', 'adress3', 'phone number 3', 'Email 3'),
                   ('yoyo4', 'adress4', 'phone number 4', 'Email 4')]
    resturants = dbconnection.queryDB(query)
    return render_template('resturantBS.html', r1=resturants1, r2=resturants2, r3=resturants)

@app.route('/deliveryOrder')
def deliveryOrder():
    return render_template('deliveryOrder.html')

# post methods
@app.route('/createResturant')
def createResturant():
    return render_template('createResturant.html')

@app.route('/addResturant', methods=['POST'])
def addResturant():
    print(request.form['rname'], request.form['adress'], request.form['phone'], request.form['email'])
    name = request.form['rname']
    adress = request.form['adress']
    phone = request.form['phone']
    email = request.form['email']
    query = "INSERT INTO resturantyoyosimple.resturant (ResturantName, Address, Tlf, Email) VALUES ('{}', '{}', '{}', '{}')".format(name, adress, phone, email)
    #dbconnection.connect()
    dbconnection.queryDB(query)
    return redirect(url_for('resturantBS'))



if __name__ == '__main__':
    app.run(debug=True)                