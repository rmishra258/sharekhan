from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [


    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello.views.index, name='home'),

    ##  lead weekdays theory

    url(r'^weekdays/$', hello.views.Weekdays.as_view(), name="weekdays-chart"),
    url(r'^weekdays/data/$', hello.views.WeekdaysData.as_view()),

    ##  conversion weekdays theory

    url(r'^conv-weekdays/$', hello.views.ConvWeekdays.as_view(), name="conv-weekdays-chart"),
    url(r'^conv-weekdays/data/$', hello.views.ConvWeekdaysData.as_view()),

    ##  lead wise time theory

    url(r'^time/$', hello.views.Time.as_view(), name="time-chart"),
    url(r'^time/data/$', hello.views.TimeData.as_view()),

    ##  conversion wise time theory

    url(r'^conv-time/$', hello.views.ConvTime.as_view(), name="conv-time-chart"),
    url(r'^conv-time/data/$', hello.views.ConvTimeData.as_view()),

    ##  Lead wise city theory

    url(r'^city/$', hello.views.City.as_view(), name="city-chart"),
    url(r'^city/data/$', hello.views.CityData.as_view()),

    ##  Lead wise city theory

    url(r'^conv-city/$', hello.views.ConvCity.as_view(), name="conv-city-chart"),
    url(r'^conv-city/data/$', hello.views.ConvCityData.as_view()),

    ##  Lead wise SOURCE city theory

    url(r'^source/$', hello.views.Source.as_view(), name="source-chart"),
    url(r'^api/source/data/$', hello.views.SourceData.as_view()),

    ##  Conversion wise SOURCE city theory

    url(r'^conv-source/$', hello.views.ConvSource.as_view(), name="conv-source-chart"),
    url(r'^conv-source/data/$', hello.views.ConvSourceData.as_view()),


    url(r'^circle/$', hello.views.test, name='circle'),

    url(r'^simple_chart/$', hello.views.simple_chart, name ='simple_chart'),

    ##converting keywords

    url(r'^keyword/$', hello.views.ConvKeyword.as_view(), name="keyword-chart"),
    url(r'^keyword/data/$', hello.views.ConvKeywordData.as_view()),
]