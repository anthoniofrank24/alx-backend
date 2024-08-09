#!/usr/bin/env python3
"""
Flask application Module
with Babel for internationalization
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """
    Configuration class for the Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel: Babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Get a user by ID from the users dictionary.

    Returns:
        A user dictionary if found, otherwise None.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """
    Function to be executed before all other functions.
    Sets the user as a global variable.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with our supported languages
    """
    # checks if the request contains a locale argument
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Renders the index.html template.

    Returns:
        The rendered HTML content of index.html.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
