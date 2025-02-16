from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from hydrofrac_models.material_parameters import MaterialParameters
from hydrofrac_models.kgd_fracture import KgdFracture
from . import plot


bp = Blueprint('model', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    top_right_chart = ''
    bottom_right_chart = ''

    if request.method == 'POST':
        e = request.form['inputE']
        mu = request.form['inputMu']
        k = request.form['inputK']
        q = request.form['inputQ']
        h = request.form['inputH']
        t = request.form['inputT']
        cp = request.form['inputCp']


        params = MaterialParameters.get_k_regime()

        frac = KgdFracture(params)
        frac_solution = frac.calculate_local_solution(100, 'K')

        top_right_chart = plot.generate_js_script(
            frac_solution.normalized_coordinate, 
            frac_solution.normalized_width, 
            'top_right_chart')



    return render_template('model/index.html',
                           top_right_chart=top_right_chart,
                           bottom_right_chart=bottom_right_chart)


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
