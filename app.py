
# Importing  necessary modules from the Flask framework
from flask import Flask, render_template, request


## Creating a Flask web application instance
app = Flask(__name__)


# Defining a route '/calculate' that accepts both GET and POST requests
@app.route('/calculate', methods=["GET", "POST"])
def calculate():

    # Check if the request method is GET
    if request.method == "GET":
        # Render the calculator.html template for the initial form display
        return render_template('calculator.html')
    
    # Retrieve user input from the submitted form
    else:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']



       # Performing calculations based on the selected operator
        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
             # Checking for division by zero before performing the operation
            if num2 != 0:
                result = num1 / num2
            else:
                return "Cannot divide by zero!"
            
        # Rendering the calculator_result.html template with the calculated result
        return render_template('calculator_result.html', result=result)
    

# Run the Flask app if this script is executed directly
if __name__ == "__main__":

    # Enable debug mode for development to automatically reload the server on code changes
    app.run(debug=True, port=8080)