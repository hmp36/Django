from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'books_db')

@app.route("/")
def index():
	return render_template("index.html", books=mysql.query_db("SELECT * FROM books"))

@app.route("/create_book", methods=["POST"])
def create():
	data = {
		"title": request.form["title"],
		"author": request.form["author"]
	}
	mysql.query_db("INSERT INTO books(title, author, created_at, updated_at) VALUES(:title, :author, NOW(), NOW());", data)
	return redirect("/")

@app.route("/edit/<id>")
def edit(id):
	query = "SELECT * FROM books WHERE id={}".format(id)
	book = mysql.query_db(query)
	return render_template("edit.html", book=book[0])

@app.route("/update_book/<id>", methods=["POST"])
def update(id):
	query = "UPDATE books SET title=:title, author=:author, updated_at=NOW() WHERE id=:id;"
	data = {
		"title": request.form["title"],
		"author": request.form["author"],
		"id": id
	}
	mysql.query_db(query, data)
	return redirect("/")

@app.route("/delete/<id>")
def delete(id):
	query = "DELETE FROM books WHERE id={}".format(id)
	mysql.query_db(query)
	return redirect("/")

app.run(debug=True)