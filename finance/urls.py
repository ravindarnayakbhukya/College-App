from django.urls import path
from finance.views import *

urlpatterns = [

    path('feecollection/', feeCollection),
    path('duereport/', feeDueReport),
    path('collectionreport/', feeCollectionReport),

]
