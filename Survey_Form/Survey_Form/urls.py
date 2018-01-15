from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.SF_app.urls')),
    url(r'^SF_app/', include('apps.SF_app.urls'))

]
