from flask import Blueprint, render_template

# Create a blueprint for main routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')   


