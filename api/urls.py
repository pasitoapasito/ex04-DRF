from django.urls import path
from api.views   import ApiTestView


urlpatterns = [
    path('/test', ApiTestView.as_view()),
]
