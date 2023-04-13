from django.urls import path
from .views import Class1, Class2, Class3, Home, Thankyou, Class4, Class5, Class6, Class7, Class8

app_name = 'app1'
urlpatterns = [
    path('class1/', Class1.as_view(), name='class1'),
    path('class2/', Class2.as_view(), name='class2'),
    path('class3/', Class3.as_view(), name='class3'),
    path('Home/', Home.as_view(), name='Home'),
    path('Thankyou/', Thankyou.as_view(), name= 'Thankyou'),
    path('class4/', Class4.as_view(), name='class4'),
    path('class5/', Class5.as_view(), name='class5'),
    path('class6/<int:pk>', Class6.as_view(), name='class6'),
    path('class7/<int:pk>', Class7.as_view(), name = 'class7'),
    path('class8/<int:pk>', Class8.as_view(), name='class8'),
]
#app_name:url_name
#app1/class4/{{id}}