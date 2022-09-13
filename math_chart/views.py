from django.shortcuts import render
from .forms import ChartsForm, SquareForm, TrigonometryForm
from django.forms import formset_factory
from plotly.offline import plot
from .die import Die
from .trigonometry import trigonometry_func, x_list
from plotly.graph_objs import Bar, Layout
import plotly.graph_objs as go
import numpy as np

def home(request):
    return render(request, 'math_chart/home.html')

def my_chart_10(request):
    ChartsFormSet = formset_factory(ChartsForm, extra=10)
    if request.method != 'POST':
        form = ChartsFormSet()
    else:
        form = ChartsFormSet(data=request.POST)
        if form.is_valid():
            points = form.cleaned_data
            x = [i['x'] for i in points]
            y = [i['y'] for i in points]
            print(form.errors)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name='y(x)'))
            fig.update_layout(legend_orientation="h",
                              margin=dict(l=0, r=0, t=0, b=0),
                              xaxis_title="Значение х",
                              yaxis_title="Значение y",
                              )
            plot_div = plot(fig, output_type='div', include_plotlyjs=False)

    try:
        context = {'form': form, 'plot_div': plot_div}
    except UnboundLocalError:
        plot_div = ''
        context = {'form': form, 'plot_div': plot_div}
    return render(request, 'math_chart/my_chart_10.html', context)

def my_chart_20(request):
    ChartsFormSet = formset_factory(ChartsForm, extra=20)
    if request.method != 'POST':
        form = ChartsFormSet()
    else:
        form = ChartsFormSet(data=request.POST)
        if form.is_valid():
            points = form.cleaned_data
            x_list = [i['x'] for i in points]
            y_list = [i['y'] for i in points]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_list, y=y_list, mode='lines+markers', name='y(x)'))
            fig.update_layout(legend_orientation="h",
                              margin=dict(l=0, r=0, t=0, b=0),
                              xaxis_title="Значение х",
                              yaxis_title="Значение y",
                              )
            plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    try:
        context = {'form': form, 'plot_div': plot_div}
    except UnboundLocalError:
        plot_div = ''
        context = {'form': form, 'plot_div': plot_div}
    return render(request, 'math_chart/my_chart_20.html', context)

def my_square(request):
    if request.method != 'POST':
        form = SquareForm()
    else:
        form = SquareForm(data=request.POST)
        if form.is_valid():
            coefficients = form.cleaned_data
            a = coefficients['a']
            b = coefficients['b']
            c = coefficients['c']
            h = -b/(2*a)                          #вершина параболы по оси х
            k = a*(h**2)+b*h+c                    #вершина параболы по оси y
            x = []
            for i in range(- 20, 21):
                x.append(i+h)
            func = [a*(i**2)+b*i+c for i in x]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=func, mode='lines', name='y=f(x)'))
            fig.update_layout(legend_orientation="h",
                              margin=dict(l=0, r=0, t=0, b=0),
                              xaxis_title="Значение х",
                              yaxis_title="Значение y",
                              )
            plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    try:
        context = {'form': form, 'plot_div': plot_div, 'h': h, 'k': k}
    except UnboundLocalError:
        plot_div = ''
        h = 0
        k = 0
        context = {'form': form, 'plot_div': plot_div, 'h': h, 'k': k}
    return render(request, 'math_chart/my_square.html', context)

def my_sin(request):
    if request.method != 'POST':
        form = TrigonometryForm()
    else:
        form = TrigonometryForm(data=request.POST)
        if form.is_valid():
            coefficients = form.cleaned_data
            a = coefficients['a']
            b = coefficients['b']
            c = coefficients['c']
            d = coefficients['d']
            x = x_list(b)
            sin_x = trigonometry_func(np.sin, a, b, c, d)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=sin_x, mode='lines', name='y=f(x)'))
            fig.update_layout(legend_orientation="h",
                              margin=dict(l=0, r=0, t=0, b=0),
                              xaxis_title="Значение х",
                              yaxis_title="Значение y",
                              )
            plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    try:
        context = {'form': form, 'plot_div': plot_div}
    except UnboundLocalError:
        plot_div = ''
        context = {'form': form, 'plot_div': plot_div}
    return render(request, 'math_chart/my_sin.html', context)

def my_cos(request):
    if request.method != 'POST':
        form = TrigonometryForm()
    else:
        form = TrigonometryForm(data=request.POST)
        if form.is_valid():
            coefficients = form.cleaned_data
            a = coefficients['a']
            b = coefficients['b']
            c = coefficients['c']
            d = coefficients['d']
            x = x_list(b)
            cos_x = trigonometry_func(np.cos, a, b, c, d)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=cos_x, mode='lines', name='y=f(x)'))
            fig.update_layout(legend_orientation="h",
                              margin=dict(l=0, r=0, t=0, b=0),
                              xaxis_title="Значение х",
                              yaxis_title="Значение y",
                              )
            plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    try:
        context = {'form': form, 'plot_div': plot_div}
    except UnboundLocalError:
        plot_div = ''
        context = {'form': form, 'plot_div': plot_div}
    return render(request, 'math_chart/my_cos.html', context)

def my_tan(request):
    if request.method != 'POST':
        form = TrigonometryForm()
    else:
        form = TrigonometryForm(data=request.POST)
        if form.is_valid():
            coefficients = form.cleaned_data
            a = coefficients['a']
            b = coefficients['b']
            c = coefficients['c']
            d = coefficients['d']
            x = x_list(b)
            tan_x = trigonometry_func(np.tan, a, b, c, d)
            fig = go.Figure()
            fig.update_yaxes(range=[-8*abs(a)+d, 8*abs(a)+d])
            fig.update_xaxes(range=[-8/abs(b), 8/abs(b)])
            fig.add_trace(go.Scatter(x=x, y=tan_x, mode='lines', name='y=f(x)'))
            fig.update_layout(legend_orientation="h",
                              margin=dict(l=0, r=0, t=0, b=0),
                              xaxis_title="Значение х",
                              yaxis_title="Значение y",
                              )
            plot_div = plot(fig, output_type='div', include_plotlyjs=False)

            ctg_x = trigonometry_func(np.tan, -a, b, c+1.57, d)
            fig_ctg = go.Figure()
            fig_ctg.update_yaxes(range=[-8 * abs(a) + d, 8 * abs(a) + d])
            fig_ctg.update_xaxes(range=[-8 / abs(b), 8 / abs(b)])
            fig_ctg.add_trace(go.Scatter(x=x, y=ctg_x, mode='lines', name='y=f(x)'))
            fig_ctg.update_layout(legend_orientation="h",
                              margin=dict(l=0, r=0, t=0, b=0),
                              xaxis_title="Значение х",
                              yaxis_title="Значение y",
                              )
            plot_div_ctg = plot(fig_ctg, output_type='div', include_plotlyjs=False)
    try:
        context = {'form': form, 'plot_div': plot_div, 'plot_div_ctg': plot_div_ctg}
    except UnboundLocalError:
        plot_div = ''
        plot_div_ctg = ''
        context = {'form': form, 'plot_div': plot_div, 'plot_div_ctg': plot_div_ctg}
    return render(request, 'math_chart/my_tan.html', context)

def trigonometry(request):
    return render(request, 'math_chart/trigonometry.html')


def b6_b6(request):
    die_1 = Die()
    die_2 = Die()

    results = []
    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    freqs = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result + 1):
        freq = results.count(value)
        freqs.append(freq)

    x_values = list(range(2, max_result + 1))
    data = [Bar(x=x_values, y=freqs)]

    x_axis_config = {'title': 'Результат', 'dtick': 1}
    y_axis_config = {'title': 'Частота результата'}

    my_layout = Layout(xaxis=x_axis_config, yaxis=y_axis_config)
    fig = go.Figure(data=data, layout=my_layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)

    fig_d = go.Figure()
    fig_d.add_trace(go.Pie(values=freqs, labels=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], sort=False, hole=0.6))
    plot_d = plot(fig_d, output_type='div', include_plotlyjs=False)

    return render(request, 'math_chart/b6_b6.html', {'plot_div': plot_div, 'plot_d': plot_d})


