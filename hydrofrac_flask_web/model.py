from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('model', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        e = request.form['inputE']
        mu = request.form['inputMu']
        k = request.form['inputK']
        q = request.form['inputQ']
        h = request.form['inputH']
        t = request.form['inputT']
        cp = request.form['inputCp']

    from . import plot

    top_right_chart = '''
    document.addEventListener('DOMContentLoaded', function() {
    Highcharts.chart('top_right_chart',
    {
    series: [{
    type: 'line'
    }]
    },
    );
    });
'''
    bottom_left_chart = '''
    document.addEventListener('DOMContentLoaded', function() {
    Highcharts.chart('bottom_left_chart',
    {
    series: [{
    type: 'line'
    }]
    },
    );
    });
'''
    return render_template('model/index.html',
                           top_right_chart=top_right_chart,
                           bottom_left_chart=bottom_left_chart)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        e = request.form['e']
        mu = request.form['mu']
        k = request.form['k']
        q = request.form['q']
        h = request.form['h']
        t = request.form['t']
        cp = request.form['cp']
        error = None

        if error is not None:
            flash(error)
        else:

            return redirect(url_for('blog.index'))

    return render_template('model/create.html')
