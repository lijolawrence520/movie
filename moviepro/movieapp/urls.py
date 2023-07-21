from django.urls import path
from.import views
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('det/<int:movie_id>/',views.det,name='det'),
    path('add',views.addm,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.dell,name='delete'),

]