from flask import Flask, request, render_template
import pickle
import mysql.connector as sql

app = Flask(__name__)

# Load the ML model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Connect to MySQL database
mydb = sql.connect(
    host="localhost",
    user="root",
    password="Anir@100"
    , database="cia2"
)
@app.route('/')
def main():
    print("------abc-----")
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_check():
    username = request.form['username']
    password = request.form['password']
    mydb = sql.connect(host="localhost",
    user="root",
    password="Anir@100"
    , database="cia2"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from login")
    data = mycursor.fetchall()
    username_list=[]
    password_list=[]

    for i in data:
        username_list.append(i[0])
        password_list.append(i[-1])

    if username not in username_list:
        return render_template('login.html',msg="Invalid username or password")
    else:
        if password not in password_list:
            return render_template('login.html',msg="Invalid username or password")
        else:
            return render_template("predict.html")
        
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = (request.form.get('age'))
        tenure = (request.form.get('tenure'))
        balance = (request.form.get('balance'))
        num_of_products = (request.form.get('numofproducts'))
        estimated_salary = (request.form.get('estimatedsalary'))
        prediction = model.predict([[age, tenure, balance, num_of_products, estimated_salary]])[0]
        if prediction == 1:
            return render_template("result.html", value = 1)
        else:
            return render_template("result.html", value = 0)
    else:
        return render_template('predict.html')

if __name__ == '__main__':
    print("----start-----")
    app.run(host = 'localhost' , port=5000)
