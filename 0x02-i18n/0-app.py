#!/usr/bin/env python3
"""
Flask application Module
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Renders the index.html template.

    Returns:
        The rendered HTML content of index.html.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
