# Entry point to run the app
from app import create_app
# Testing Auto Deploy
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)