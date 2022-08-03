from django.urls import path
from . import views

# APP_NAME = "movies"
# URL configurations
urlpatterns = [
    path('', views.index, name="movies_index"),
    path('<int:movie_id>', views.detail, name='movies_detail')
]
