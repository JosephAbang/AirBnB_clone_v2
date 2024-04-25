#!/usr/bin/python3
"""
    Start a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """render list of states templates"""
    states = storage.all(states)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', sorted_states=sorted_states)


@app.teardown_appcontext
def teardown_app(arg=None):
    """Teardown running session"""
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
