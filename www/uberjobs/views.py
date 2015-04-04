from django.shortcuts import render
from django.http import HttpResponse
from uberjobs.models import EconCategory, EconSeries

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime

from scipy import stats
import json

# Create your views here.
def index(request):
    return render(request, 'uberjobs/index.html')

def serieslist(request):
    series_list = EconSeries.objects.all()
    category_list = EconCategory.objects.all()

    context = {
            'series_list' : series_list,
            'category_list' : category_list
        }
        
    return render(request, 'uberjobs/serieslist.html', context)


def seriesdetail(request, series_id):

    series_data = []
    series_json = ''
    error_msg = ''

    try:
        if len(EconSeries.objects.filter(series_id=series_id)) > 0:
            series = EconSeries.objects.filter(series_id=series_id)[0]
            series_data = series.get_data()
        else:
            error_msg = "Sorry, we couldn't find your series!"
    except:
        raise Http404("Series does not exist.")

    context = {
        'series_id' : series_id,
        'series_data' : series_data,
        'series_json' : json.dumps(series_data),
        'error_msg' : error_msg
    }

    return render(request, 'uberjobs/seriesdetail.html', context)

def seriesmodel(request, series_id):

    series_data = []
    series_json = ''
    error_msg = ''
    slope = 0
    intercept = 0
    r_value = 0
    p_value = 0
    std_err = 0

    try:
        if len(EconSeries.objects.filter(series_id=series_id)) > 0:
            series = EconSeries.objects.filter(series_id=series_id)[0]
            job_series = EconSeries.objects.get(pk=1)

            series_data = series.get_data()
            job_series_data = job_series.get_data()
        else:
            error_msg = "An error happened!"

        X = job_series_data.values()
        Y = series_data.values()
    
        # Create linear regression object
        slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)

    except:
        error_msg = 'An error happened!'

    

    context = {
        'series_id' : series_id,
        'series_data' : series_data,
        'job_series_data' : job_series_data,
        'slope' : round(slope,3),
        'intercept' : round(intercept,6),
        'r_value' : round(r_value,3),
        'p_value' : round(p_value,6),
        'std_err' : round(std_err,3),
        'r_squared' : round(r_value**2,3),
        'error_msg' : error_msg
    }

    return render(request, 'uberjobs/seriesmodel.html', context)

def serieschart(request, series_id):

    try:
        series = EconSeries.objects.filter(series_id=series_id)[0]
        series_data = series.get_raw_data()
        series_name = series.series_name
    except EconSeries.DoesNotExist:
        raise Http404("Series does not exist.")

    x_labels = [datetime.strptime(n, '%Y-%m') for n in series_data.keys()]

    fig = Figure(facecolor="white")
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ax.plot(x_labels, series_data.values())
    ax.set_title(series_name)
    ax.grid(True)
    ax.set_xlabel('Time')
    response = HttpResponse(content_type = 'image/png')
    canvas.print_png(response)
    return response

def serieschartcompare(request, series_id, lag=0):

    try:
        user_series = EconSeries.objects.filter(series_id=series_id)[0]
        job_series = EconSeries.objects.get(pk=1)

        user_series_data = user_series.get_data()
        user_series_name = user_series.series_name

        job_series_data = job_series.get_data()
        job_series_name = job_series.series_name

    except EconSeries.DoesNotExist:
        raise Http404("Series does not exist.")

    x_labels = [datetime.strptime(n, '%Y-%m') for n in user_series_data.keys()]

    fig = Figure(facecolor="white")
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ax.plot(x_labels, user_series_data.values(), label=user_series.series_id)
    ax.plot(x_labels, job_series_data.values(), label=job_series.series_id, color='r')
    ax.set_title(user_series_name + " vs. " + job_series_name)
    ax.grid(True)
    ax.set_xlabel('Time')
    ax.legend([user_series.series_id, job_series.series_id], loc='upper right')
    response = HttpResponse(content_type = 'image/png')
    canvas.print_png(response)
    return response

def serieschartscatter(request, series_id, lag=0):

    try:
        user_series = EconSeries.objects.filter(series_id=series_id)[0]
        job_series = EconSeries.objects.get(pk=1)

        user_series_data = user_series.get_data()
        user_series_name = user_series.series_name

        job_series_data = job_series.get_data()
        job_series_name = job_series.series_name

    except EconSeries.DoesNotExist:
        raise Http404("Series does not exist.")

    fig = Figure(facecolor="white")
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ax.scatter(job_series_data.values(), user_series_data.values())
    ax.set_title("Scatter Plotting")
    ax.grid(True)
    ax.set_xlabel(job_series_name)
    ax.set_ylabel(user_series_name)
    response = HttpResponse(content_type = 'image/png')
    canvas.print_png(response)
    return response
