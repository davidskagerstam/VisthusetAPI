from django.conf.urls import url
from Visthuset_web.views import MenyView, EventView
from VisthusetAPI.views import IndexView


app_name = "Visthuset_web"
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^meny/$', MenyView.as_view(), name="meny"),
    url(r'^evenemang/$', EventView, name="event"),
    ]