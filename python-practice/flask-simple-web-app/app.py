# # import Flask module 
from flask import Flask, render_template, request

# # Initialize Flask application 
app = Flask(__name__)

# # Define a route for homepage 
@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/form')
def form(): 
    return render_template('form.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f'Hello, {name}!'

@app.route('/gallery' )
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about(): 
    return render_template('about.html')



if __name__ == '__main__': 
    # run Flask app 
    app.run(debug=True)

