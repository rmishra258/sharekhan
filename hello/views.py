from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Greeting
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import numpy as np

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN




# Create your views here.


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def index(request):

    return render(request,'index.html')


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)




### LEAD-WISE WEEKDAYS DATA

class Weekdays(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'weekdays.html')


class WeekdaysData(APIView):
    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):

        ## data visulaization starts here


        data = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/1FfHdYFfzYaYAMfby5MZaOCli8ePMA_3hfZp3HI_X-Ks/pub?output=csv')



        data = data['Day'].value_counts()

        days = list(data.keys())
        daysdata = list(data.values)

        labels = days
        default_items = daysdata
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)

##CONVERSION-WISE WEEKDAYS DATA


class ConvWeekdays(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'conv-weekdays.html')


class ConvWeekdaysData(APIView):
    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):

        ## data visulaization starts here



        data = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/1FfHdYFfzYaYAMfby5MZaOCli8ePMA_3hfZp3HI_X-Ks/pub?output=csv')

        data = data[data['Status'] == 'Sale']

        data = data['Day'].value_counts()

        days = list(data.keys())
        daysdata = list(data.values)

        labels = days
        default_items = daysdata
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)

##LEAD-WISE TIME DATA


class Time(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'time.html')


class TimeData(APIView):
    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):

        ## data visulaization starts here

        data = data = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/1FfHdYFfzYaYAMfby5MZaOCli8ePMA_3hfZp3HI_X-Ks/pub?output=csv')


        time = (data['Hour'].value_counts()).sort_index(ascending=True)

        timelabel = list(time.keys())
        timedata = list(time.values)


        labels = timelabel
        default_items = timedata
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


##CONVERSION-WISE TIME DATA


class ConvTime(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'conv-time.html')


class ConvTimeData(APIView):
    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):

        ## data visulaization starts here

        data = data = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/1FfHdYFfzYaYAMfby5MZaOCli8ePMA_3hfZp3HI_X-Ks/pub?output=csv')

        data = data[data['Status'] == 'Sale']

        time = (data['Hour'].value_counts()).sort_index(ascending=True)

        timelabel = list(time.keys())
        timedata = list(time.values)


        labels = timelabel
        default_items = timedata
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)

##LEAD-WISE CITY DATA


class City(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'city.html')


class CityData(APIView):
    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):

        ## data visulaization starts here


        data = data = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/1FfHdYFfzYaYAMfby5MZaOCli8ePMA_3hfZp3HI_X-Ks/pub?output=csv')

        city = (data['City'].value_counts()).head(10)

        cityname = list(city.keys())
        citydata = list(city.values)



        labels = cityname
        default_items = citydata
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


##CONVERSION-WISE CITY DATA


class ConvCity(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'conv-city.html')


class ConvCityData(APIView):
    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):

        ## data visulaization starts here


        data = data = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/1FfHdYFfzYaYAMfby5MZaOCli8ePMA_3hfZp3HI_X-Ks/pub?output=csv')

        data = data[data['Status'] == 'Sale']

        city = (data['City'].value_counts()).head(10)

        cityname = list(city.keys())
        citydata = list(city.values)


        labels = cityname
        default_items = citydata
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


##LEAD-WISE SOURCE DATA


class Source(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'source.html')


class SourceData(APIView):
    authentication_classes = []
    permission_classes = []




    def get(self, request, format=None):

        ## data visulaization starts here



        data = data = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/1FfHdYFfzYaYAMfby5MZaOCli8ePMA_3hfZp3HI_X-Ks/pub?output=csv')

        data = data.fillna('Unknown')

        source = data['utm_source'].value_counts()

        sourcename = list(source.keys())
        sourcedata = list(source.values)


        labels = sourcename
        default_items = sourcedata
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


##CONVERSION-WISE SOURCE DATA

class ConvSource(View):
    def get(self, request):


        return render(request, 'conv-source.html')

class ConvSourceData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        ## data visulaization starts here


        data = data = pd.read_csv('https://docs.google.com/spreadsheets/d/1FfHdYFfzYaYAMfby5MZaOCli8ePMA_3hfZp3HI_X-Ks/pub?output=csv')

        data = data[data['Status'] == 'Sale']

        data = data.fillna('Unknown')

        source = data['utm_source'].value_counts()

        sourcename = list(source.keys())
        sourcedata = list(source.values)

        lst1 = [1,2,3,4,5,6]



        labels = sourcename
        default_items = sourcedata
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


##test bokeh implementation

def test(request):

    plot = figure(plot_width=400 , tools='pan, box_zoom')
    plot.circle([12,3,4,5],[8,6,5,2,3])
    output_file('test.html')
    show(plot)

    return render(request, plot)


def simple_chart(request):
    plot = figure()
    plot.circle([1, 2], [3, 4])

    show(plot)

    script, div = components(plot, CDN)

    return render(request, "test.html", {"script": script, "div": div , 'name' : 'rahul'})


def converting_keyword(request):
    data = pd.read_csv('https://docs.google.com/spreadsheets/d/1h8xQtq-t-_bLk2VrXO-v26exeG5FkgrCF7mRrQQnDbA/pub?output=csv')

    data = data[data['Conversions'] >= 1]

    data = data[data['Keyword'].str.contains('khan')]

    data = data.loc[:, ['Keyword', 'Conversions']]

    name = np.array(data['Keyword'])
    conv = np.array(data['Conversions'])

    return render(request, 'keyword.html')


class ConvKeyword(View):
    def get(self, request):


        return render(request, 'keyword.html')

class ConvKeywordData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        ## data visulaization starts here


        data = pd.read_csv('https://docs.google.com/spreadsheets/d/1gS2x5wz8e5CCcySLBWSDt92LmkDY2N6_XOWyjIFFAEw/pub?output=csv')

        data = data[data['Conversions'] >= 1]

        data = data[data['Keyword'].str.contains('khan')].head(10)

        data = data.loc[:, ['Keyword', 'Conversions']]

        name = np.array(data['Keyword'])
        conv = np.array(data['Conversions'])




        labels = list(name)
        default_items = list(conv)


        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)