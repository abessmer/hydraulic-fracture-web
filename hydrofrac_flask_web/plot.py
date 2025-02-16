from highcharts_core.chart import Chart
from highcharts_core.options import HighchartsOptions
from highcharts_core.options.plot_options import PlotOptions
from highcharts_core.options.axes.x_axis import XAxis
from highcharts_core.options.axes.y_axis import YAxis
from highcharts_core.options.axes.accessibility import AxisAccessibility
from highcharts_core.options.axes.title import YAxisTitle, AxisTitle
from highcharts_core.options.title import Title
from highcharts_core.options.subtitle import Subtitle
from highcharts_core.options.legend import Legend
from highcharts_core.options.plot_options.series import SeriesOptions
from highcharts_core.options.series.area import LineSeries
from highcharts_core.options.series.labels import SeriesLabel
from highcharts_core.options.responsive import Responsive, ResponsiveRules, Condition
from highcharts_core.constants import EnforcedNull
import numpy as np


def generate_width_chart_js_script(global_solution,
                                   local_k_solution,
                                   local_m_solution,
                                   local_kt_solution,
                                   local_mt_solution,
                                   container: str):
    chart_options = HighchartsOptions(
        title=Title(text='Fracture width distribution',
                    align='left'),
        y_axis=YAxis(title=YAxisTitle(text='Fracture width, mm')),
        x_axis=XAxis(
            title=AxisTitle(text='Coordinate, m'),
        ),
        legend=Legend(layout='vertical',
                      align='right',
                      vertical_align='middle'),
        plot_options=PlotOptions(series=SeriesOptions(point_start=2010,
                                                      label=SeriesLabel(connector_allowed=False)))
    )

    override_options = HighchartsOptions(legend=Legend(layout='horizontal',
                                                       align='center',
                                                       vertical_align='bottom'))
    responsive_config = Responsive(
        rules=[
            ResponsiveRules(chart_options=override_options,
                            condition=Condition(max_width=500))
        ]
    )
    chart_options.responsive = responsive_config

    global_line_series = LineSeries.from_array(np.stack(
        (global_solution.normalized_coordinate, global_solution.normalized_width), axis=-1))
    global_line_series.name = 'Global solution'
    chart_options.add_series(global_line_series)

    local_k_line_series = LineSeries.from_array(np.stack(
        (local_k_solution.normalized_coordinate, local_k_solution.normalized_width), axis=-1))
    local_k_line_series.name = 'Local K solution'
    chart_options.add_series(local_k_line_series)

    local_m_line_series = LineSeries.from_array(np.stack(
        (local_m_solution.normalized_coordinate, local_m_solution.normalized_width), axis=-1))
    local_m_line_series.name = 'Local M solution'
    chart_options.add_series(local_m_line_series)

    local_kt_line_series = LineSeries.from_array(np.stack(
        (local_kt_solution.normalized_coordinate, local_kt_solution.normalized_width), axis=-1))
    local_kt_line_series.name = 'Local Kt solution'
    chart_options.add_series(local_kt_line_series)

    local_mt_line_series = LineSeries.from_array(np.stack(
        (local_mt_solution.normalized_coordinate, local_mt_solution.normalized_width), axis=-1))
    local_mt_line_series.name = 'Local Mt solution'
    chart_options.add_series(local_mt_line_series)

    chart = Chart.from_options(chart_options)

    chart.container = container

    as_js_literal = chart.to_js_literal()

    return as_js_literal


def generate_pressure_chart_js_script(global_solution,
                                      local_k_solution,
                                      local_m_solution,
                                      local_kt_solution,
                                      local_mt_solution,
                                      container: str):
    chart_options = HighchartsOptions(
        title=Title(text='Fluid pressure distribution',
                    align='left'),
        y_axis=YAxis(title=YAxisTitle(text='Fluid pressure, Pa')),
        x_axis=XAxis(
            title=AxisTitle(text='Coordinate, m'),
        ),
        legend=Legend(layout='vertical',
                      align='right',
                      vertical_align='middle'),
        plot_options=PlotOptions(series=SeriesOptions(point_start=2010,
                                                      label=SeriesLabel(connector_allowed=False)))
    )

    override_options = HighchartsOptions(legend=Legend(layout='horizontal',
                                                       align='center',
                                                       vertical_align='bottom'))
    responsive_config = Responsive(
        rules=[
            ResponsiveRules(chart_options=override_options,
                            condition=Condition(max_width=500))
        ]
    )
    chart_options.responsive = responsive_config

    global_line_series = LineSeries.from_array(np.stack(
        (global_solution.normalized_coordinate, global_solution.normalized_pressure), axis=-1))
    global_line_series.name = 'Global solution'
    chart_options.add_series(global_line_series)

    local_k_line_series = LineSeries.from_array(np.stack(
        (local_k_solution.normalized_coordinate, local_k_solution.normalized_pressure), axis=-1))
    local_k_line_series.name = 'Local K solution'
    chart_options.add_series(local_k_line_series)

    local_m_line_series = LineSeries.from_array(np.stack(
        (local_m_solution.normalized_coordinate, local_m_solution.normalized_pressure), axis=-1))
    local_m_line_series.name = 'Local M solution'
    chart_options.add_series(local_m_line_series)

    local_kt_line_series = LineSeries.from_array(np.stack(
        (local_kt_solution.normalized_coordinate, local_kt_solution.normalized_pressure), axis=-1))
    local_kt_line_series.name = 'Local Kt solution'
    chart_options.add_series(local_kt_line_series)

    local_mt_line_series = LineSeries.from_array(np.stack(
        (local_mt_solution.normalized_coordinate, local_mt_solution.normalized_pressure), axis=-1))
    local_mt_line_series.name = 'Local Mt solution'
    chart_options.add_series(local_mt_line_series)

    chart = Chart.from_options(chart_options)

    chart.container = container

    as_js_literal = chart.to_js_literal()

    return as_js_literal
