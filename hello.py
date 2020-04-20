from flask import Flask, render_template, url_for, request, redirect, session, flash
import pymysql
from forms import ContactForm
app= Flask(__name__)
app.secret_key = 'development kay'
db = pymysql.connect('localhost', 'yonny', 'yonny', 'database')

cursor = db.cursor()
cursor.execute("DROP TABLE if exists login")
sql= "CREATE TABLE login(username CHAR(200), password INT(8))"

cursor.execute(sql)
sql= "INSERT INTO login (username, password) VALUES ('Tom','10001000'),('May','21002100'), ('Kevin','30003000');"
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()

db = pymysql.connect('localhost', 'yonny', 'yonny', 'database')
cursor = db.cursor()
sql= "INSERT INTO orderForm (product_name, order_quantity, customer_name, customer_phone_number, customer_email, customer_address, payment_method) VALUES  ('VitaminD','2','Tom','20200202','Tom20@gmail.com','55/F SI Building A, NT','Credit card'),('VitaminA','1','May','30102010','May001@gmail.com','20/F maful building, NY','Paypal'), ('VitaminC','5','David','40402042','Tim2David@gmail.com','8/F June building, HK','Paypal'), ('VitaminB12','2','Mary','30112010','Maryma1@hotmail.com','22/F Yak building, NY','credit card')"

try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()
#sql= "CREATE TABLE STUDENT(FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20), AGE INT, GENDER CHAR(1))"
#cursor.execute(sql)
@app.route("/index")
def index():
	if 'username' in session:
		return 'Logged in as ' + session['username']+ '<br>' + "<a href = '/logout'>Logout</a> " + render_template('product.html')
	else:	
		return 'You have logged out' + '<br>' +"<a href = '/login'>Click here to log in</a>" +  render_template('product.html')


@app.route("/login", methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		usernames = request.form["username"]
		pwd = request.form['password']
	db = pymysql.connect('localhost', 'yonny', 'yonny', 'database')
	cursor = db.cursor()
	sql = ("SELECT * FROM login")
	cursor.execute(sql)
	db.commit()
	result = cursor.fetchall()
	for row in result:
		custName = row[0]
		custPassword = row[1]
		session['username'] = custName
		return redirect(url_for("index"))
	return render_template("loginPage.html", error = error)
	db.close()
		#return render_template('login.html', guest = custName)
		#redirect(url_for('login', guest = custName))
@app.route("/logout")
def logout():
	#remove the username from the session
	session.pop('username', None)
	return "You've logged out."+  render_template('product.html')

@app.route("/loginPage")
def loginPage():
	return render_template('loginPage.html')

@app.route("/cart", methods = ['GET','POST'])
def cart():
	form= ContactForm()

	if request.method=='POST':
		if form.validate_on_submit():
			return redirect('/success')
		return "<a href = '/logout'>Logout</a> " + render_template('success.html') +  render_template('product.html')
	else:
		return  render_template('cart.html', form=form) 

@app.route("/VitaminA")
def a():
	if 'product' in session:
		return render_template('cart.html') +'Added' + session['product']
	

@app.route("/success", methods=['POST','GET'])
def shoppingCart():
	error = None
	if request.method == 'POST':
		product = request.form["product"]
		price = request.form['price']
	db = pymysql.connect('localhost', 'yonny', 'yonny', 'database')
	cursor = db.cursor()
	sql = ("SELECT * FROM shoppingCart")
	cursor.execute(sql)
	db.commit()
	result = cursor.fetchall()
	for row in result:
		vit = row[0]
		price = row[1]
		session['product'] = vit
		
		return redirect(url_for("/product")  + session['product'])
	return render_template("product.html", error = error)
	db.close()

@app.route("/")
def setup():
	return render_template('setup.html')
@app.route("/product")
def product():
	return render_template('product.html')	
@app.route("/list")
def list():
	return render_template('list.html')
@app.route("/article")
def article():
	return render_template('article.html')

if __name__ == '__main__':
	app.run(debug=True)
