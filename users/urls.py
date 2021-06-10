from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users import views
from users.views import RegisterView, UserViewSet

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet)

api_urlpatterns = [
    path('register/',
         RegisterView.as_view(),
         name='auth_register'),
]

dj_urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]

urlpatterns = [
    path('v1/', include(api_urlpatterns)),
    path('v1/', include(router_v1.urls)),
    path('', include(dj_urlpatterns))
]
