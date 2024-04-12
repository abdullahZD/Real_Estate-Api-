from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"add_estate", views.BuldingViewset, basename="add_estate")

urlpatterns = [
    path("contact_form/", views.ContactUsView.as_view(), name="contact_form"),
    path("request_bulding/", views.RequestBuldingView.as_view(), name="request_bulding"),
    path("", include(router.urls)),
    path("get_estates/", views.GetAllEstatesView.as_view(), name="get_estates"),
    path("get_estate/<int:pk>/", views.GetEstateView.as_view(), name="get_estate"),
]
