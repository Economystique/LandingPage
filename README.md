# Flask Landing Page

A modern, responsive landing page built with Flask, featuring user authentication, contact forms, and newsletter subscription.

## Features

- **Modern Design**: Clean, responsive design using Bootstrap 5
- **User Authentication**: Login and registration system with Flask-Login
- **Contact Form**: Functional contact form with database storage
- **Newsletter Subscription**: Email subscription functionality
- **Database Integration**: SQLAlchemy with SQLite (easily configurable for other databases)
- **Security**: Password hashing, CSRF protection, and secure session management
- **Mobile Responsive**: Optimized for all device sizes

## Project Structure

```
your_project/
│
├── app/                    # Main application package
│   ├── __init__.py         # Initializes the Flask app
│   ├── routes.py           # Route definitions
│   ├── models.py           # Database models
│   ├── static/             # CSS, JS, images
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   └── templates/          # HTML templates
│       ├── base.html       # Base template
│       ├── index.html      # Home page
│       ├── about.html      # About page
│       ├── contact.html    # Contact page
│       └── auth/           # Authentication templates
│           ├── login.html
│           └── register.html
│
├── venv/                   # Virtual environment
│
├── run.py                  # Entry point to run the app
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd landing-page
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables** (optional)
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///site.db
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-email-password
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

7. **Access the application**
   Open your browser and go to `http://localhost:5000`

## Configuration

The application uses different configuration classes for different environments:

- **Development**: `config.py` - DevelopmentConfig
- **Testing**: `config.py` - TestingConfig  
- **Production**: `config.py` - ProductionConfig

To use a specific configuration, set the `FLASK_ENV` environment variable:
```bash
export FLASK_ENV=production
```

## Database

The application uses SQLAlchemy with SQLite by default. The database will be automatically created when you first run the application.

To use a different database (PostgreSQL, MySQL, etc.), update the `SQLALCHEMY_DATABASE_URI` in your configuration.

## Features in Detail

### User Authentication
- User registration with email validation
- Secure login/logout functionality
- Password hashing with Werkzeug
- Session management with Flask-Login

### Contact Form
- Collects name, email, subject, and message
- Stores submissions in the database
- Form validation and error handling
- Flash messages for user feedback

### Newsletter Subscription
- Email collection for newsletter
- Duplicate email prevention
- Database storage of subscriptions

### Responsive Design
- Bootstrap 5 for responsive layout
- Custom CSS for enhanced styling
- Mobile-first approach
- Modern UI components

## Customization

### Styling
- Modify `app/static/css/style.css` for custom styling
- Update Bootstrap classes in templates
- Add custom JavaScript in `app/static/js/main.js`

### Content
- Edit templates in `app/templates/` to change content
- Update company information in templates
- Modify contact details and social links

### Functionality
- Add new routes in `app/routes.py`
- Create new models in `app/models.py`
- Extend the application with additional features

## Deployment

### Using Gunicorn (Recommended for Production)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

### Using Heroku
1. Create a `Procfile`:
   ```
   web: gunicorn run:app
   ```
2. Deploy to Heroku using their CLI or GitHub integration

### Using Docker
1. Create a `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 5000
   CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue on GitHub or contact the development team.

## Changelog

### Version 1.0.0
- Initial release
- Basic Flask application structure
- User authentication system
- Contact form functionality
- Newsletter subscription
- Responsive design with Bootstrap 5 