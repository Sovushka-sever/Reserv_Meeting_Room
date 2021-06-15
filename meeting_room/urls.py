from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.new_meting_room, name='new_meting_room'),
    path('reserve/', views.new_reserve, name='new_reserve'),
    path('', views.index, name='index'),
    path('<int:room_id>/', views.meting_room_view, name='meeting_room'),
    path('<int:room_id>/delete/', views.meeting_room_delete,
         name='meeting_room_delete'),
    path(
        '<int:room_id>/edit/',
        views.meting_room_edit,
        name='meting_room_edit'
        ),
]
