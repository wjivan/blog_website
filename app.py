import sys, os
import json

# Imports
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flaskext.markdown import Markdown
from flask_bootstrap import Bootstrap

# Configuration
DEBUG = True

# Some configurations for markdown flatpages
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)  # contains links to all pages ending with .md

# Define the markdown style
markdown_manager = Markdown(app, extensions=['fenced_code', 'mdx_math'], output_format='html5')

# Frozen App
# Currently the Flask app is still serving the rendering the flat pages
# Using Freezer, we create a static set of files and assets that removes
# Flask as the middleman
freezer = Freezer(app)  
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = PROJECT_ROOT
# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "http://localhost/wjivan.github.io"
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                    # will be deleted when you run the freezer

# Find all tags
tags = sorted(set([tag for page in pages for tag in page.meta['tags']]))
tech = ['R', 'Python', 'SQL', 'Flask']
tags_topical = set(tags) - set(tech)
tags_tech = set(tags).intersection(tech)

# Functionalities
# @app.context_processor
# def clever_function(u):
#     return 'hello'

# Routes
# Note: templates default to 'templates' folder 
@app.route('/')
def index():
    return render_template('about.html', tags_topical=tags_topical, tags_tech=tags_tech)

@app.route('/blogs/')
def blogs():
    return render_template('blogs.html', tags_topical=tags_topical, tags_tech=tags_tech, pages=pages, tags=tags)

@app.route('/tag/<string:tag>/')
def tag(tag):
    # Get pages objects for specific tags
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag, tags=tags, tags_topical=tags_topical, tags_tech=tags_tech)

@app.route('/<path:path>/')
def page(path):
    return render_template('page.html', page=pages.get_or_404(path), tags_topical=tags_topical, tags_tech=tags_tech)

@app.route('/projects/')
def projects():
    with open('data/projects.json') as projects_json:
        projects_data = json.load(projects_json)
        return render_template('projects.html', projects=projects_data)

@app.errorhandler(404)
def page_not_found(path):
    # set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)

# app.jinja_env.globals.update(clever_function=clever_function)
# app.add_template_global(clever_function, name='clever_function')
