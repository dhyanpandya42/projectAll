from flask import  Flask,render_template,jsonify
import csv
import os


app=Flask(__name__)
@app.route("/")
def helloapp():
    return render_template('home.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/welcome")
def welcome():
    return render_template('welcome.html')




# @app.route("/expense")from flask import Flask, render_template, redirect, url_for, request, flash, session

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'xyz'  # Change this to a random secret key

# Hardcoded username and password
USERNAME = 'admin'
PASSWORD = 'password123'

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']

    #     if username == USERNAME and password == PASSWORD:
    #         session['user_id'] = username  # Store the username in the session
    #         flash('Login successful!', 'success')
    #         return redirect(home.html('home'))
    #     else:
    #         flash('Invalid username or password.', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    # session.pop('user_id', None)  # Remove user from session
    # flash('You have been logged out.', 'info')
    return (login.html('home'))

@app.route('/home')
def home():
    return render_template('home.html')  # Create a simple home.html template
# def list_expense():
#     return jsonify(categories)

@app.route('/expenses')
def expenses():
    #its for retriving quieries from database
    # expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses)


# @app.route('/import', methods=['GET', 'POST'])
# def import_expenses():
#     if request.method == 'POST':
#         # Ensure the uploaded file is a CSV
#         if 'file' not in request.files:
#             return 'No file uploaded', 400
        
#         file = request.files['file']
        
#         if file.filename == '':
#             return 'No file selected', 400
        
#         if file and file.filename.endswith('.csv'):
#             # Read the CSV file
#             csv_file = csv.reader(file.stream.read().decode('utf-8').splitlines())
#             next(csv_file)  # Skip the header row
            
#             for row in csv_file:
#                 title = row[0]
#                 category = row[1]
#                 amount = float(row[2])
#                 date = datetime.strptime(row[3], '%Y-%m-%d')
                
#                 # Create a new expense record
#                 new_expense = Expense(title=title, category=category, amount=amount, date=date)
#                 db.session.add(new_expense)
            
#             db.session.commit()
#             return redirect(url_for('home'))

#     return render_template('import.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)