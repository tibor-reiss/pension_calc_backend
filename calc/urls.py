"""
Define the calc specific urls.
"""

from django.urls import path

from calc import views


urlpatterns = [
    path("latest-calcs/", views.latest_calcs),
    path("generate-calc/", views.generate_calc),
]
