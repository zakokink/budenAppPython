from django.urls import path
from . import views
from .views import LatestTrainingFuerUebungAndUser, LatestGewichtForUebungAndUser, Uebungen

urlpatterns = [
    path('', views.home, name='home'),
    path('uebungen/', views.UebungenListCreate.as_view(), name="uebungen-view-create"),
    path('uebungen/<int:pk>', views.UebungenListUpdateDestroy.as_view(), name="uebungen-update"),
    path('uebung', Uebungen.as_view()),
    path('letztesTraining/<int:userId>/<int:uebungId>', views.LatestTrainingFuerUebungAndUser.as_view(), name="latest-training-view-create"),
    path('letztesGewicht/<int:userId>/<int:uebungId>', views.LatestGewichtForUebungAndUser.as_view(), name="latest-gewicht-view-create"),

]

