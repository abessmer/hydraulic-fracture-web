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

def generate_js_script(x, y, container: str):
    chart_options = HighchartsOptions(
        title = Title(text = 'Fracture',
                    align = 'left'),
        y_axis = YAxis(title = YAxisTitle(text = 'Fracture width, mm')),
        x_axis = XAxis(
            title = AxisTitle(text = 'Coordinate, m'),
        ),
        legend = Legend(layout = 'vertical',
                        align = 'right',
                        vertical_align = 'middle'),
        plot_options = PlotOptions(series = SeriesOptions(point_start = 2010,
                                                        label = SeriesLabel(connector_allowed = False)))
    )

    override_options = HighchartsOptions(legend = Legend(layout = 'horizontal',
                                                        align = 'center',
                                                        vertical_align = 'bottom'))
    responsive_config = Responsive(
        rules = [
            ResponsiveRules(chart_options = override_options,
                            condition = Condition(max_width = 500))
        ]
    )
    chart_options.responsive = responsive_config

    xy_array_stack = np.stack((x, y), axis=-1)
    line_series = LineSeries.from_array(xy_array_stack)
    line_series.name = 'Global solution'
    chart_options.add_series(line_series)
    chart = Chart.from_options(chart_options)

    chart.container = container

    as_js_literal = chart.to_js_literal()

    return as_js_literal