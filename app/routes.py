"""Routes for parent Flask app."""
from flask import render_template
from flask import current_app as app


@app.route('/')
def home():
    """Landing page."""
    
    return render_template(
        'index.jinja2',
        title='MVP Dashboard',
        template='home-template',
    )