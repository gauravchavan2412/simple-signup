from flask import Flask, render_template, request, redirect
import boto3
import os

app = Flask(__name__)

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Change to your region
table = dynamodb.Table('signup_table')

# Route to display signup form
@app.route('/')
def index():
    return render_template('signup.html')

# Route to handle form submission
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']

    # Insert user information into DynamoDB
    table.put_item(
        Item={
            'email': email,
            'name': name
        }
    )
    return redirect('/users')

# Route to display user information from DynamoDB
@app.route('/users')
def users():
    response = table.scan()
    users = response.get('Items', [])
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7447)
