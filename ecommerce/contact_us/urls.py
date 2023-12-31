from django.urls import include, path
from .views import ContactViewSet

app_name = "contacts"

contact_view = ContactViewSet.as_view(
    {"get": "list", "post": "create", "delete": "destroy"}
)

urlpatterns = [
    path("contacts/", contact_view, name="contact-list"),
    path("contacts/<int:pk>/", contact_view, name="contact-delete"),
    path("contacts/delete-all/", contact_view, name="contact-delete-all"),
    path("contacts/create/", contact_view, name="contact-create"),
]
