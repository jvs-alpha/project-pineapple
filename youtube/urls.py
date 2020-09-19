from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = "youtube"
urlpatterns = [
    path("",views.yindex,name="youtube index"),
    path("<int:qid>/",views.detail,name="detail"),
    path("<int:yid>/likes/",views.likes,name="video likes"),
    path("<int:yid>/comments/",views.comments,name="video comments"),
]

urlpatterns += staticfiles_urlpatterns()
