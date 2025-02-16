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
    params = {
        'youngs_modulus': '',
        'fluid_viscosity': '',
        'fracture_toughness': '',
        'fluid_injection_rate': '',
        'fracture_height': '',
        'time': '',
        'porosity': '',
    }
    mat_params = MaterialParameters.get_intermediate_regime()

    if request.method == 'GET':
        params = {
            'youngs_modulus': f'{mat_params.youngs_modulus:.4f}',
            'fluid_viscosity': f'{mat_params.fluid_viscosity:.4f}',
            'fracture_toughness': f'{mat_params.fracture_toughness:.4f}',
            'fluid_injection_rate': f'{mat_params.fluid_injection_rate}',
            'fracture_height': f'{mat_params.fracture_height}',
            'time': f'{mat_params.time}',
            'porosity': f'{mat_params.porosity:.4f}',
        }
        selected_params = MaterialParameters(
            float(params['youngs_modulus']),
            float(params['fluid_viscosity']),
            float(params['fracture_toughness']),
            float(params['fluid_injection_rate']),
            float(params['fracture_height']),
            float(params['time']),
            float(params['porosity']),
        )

    if request.method == 'POST':
        params = request.form
        selected_params = MaterialParameters(
            float(request.form['youngs_modulus']),
            float(request.form['fluid_viscosity']),
            float(request.form['fracture_toughness']),
            float(request.form['fluid_injection_rate']),
            float(request.form['fracture_height']),
            float(request.form['time']),
            float(request.form['porosity']),
        )

    frac = KgdFracture(selected_params)
    local_k_solution = frac.calculate_local_solution(100, 'K')
    local_m_solution = frac.calculate_local_solution(100, 'M')
    local_kt_solution = frac.calculate_local_solution(100, 'Kt')
    local_mt_solution = frac.calculate_local_solution(100, 'Mt')

    global_solution = frac.calculate_global_solution(100)

    top_right_chart = plot.generate_width_chart_js_script(
        global_solution,
        local_k_solution,
        local_m_solution,
        local_kt_solution,
        local_mt_solution,
        'top_right_chart')

    bottom_right_chart = plot.generate_pressure_chart_js_script(
        global_solution,
        local_k_solution,
        local_m_solution,
        local_kt_solution,
        local_mt_solution,
        'bottom_right_chart')

    return render_template('model/index.html',
                           **params,
                           top_right_chart=top_right_chart,
                           bottom_right_chart=bottom_right_chart)
