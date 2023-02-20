from flask import render_template
from ._gallery import gallery


@gallery.get('/')
def index():
    return render_template('gallery/home.html')
