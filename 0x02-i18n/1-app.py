#!/usr/bin/env python3
"""
Flask application Module
with Babel for internationalization
"""
from flask import Flask, render_template
from flask_babel import Babel


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


@app.route('/')
def get_index() -> str:
    """
    Renders the index.html template.

    Returns:
        The rendered HTML content of index.html.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
