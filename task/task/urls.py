from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', include('apps.users.urls'))
]
