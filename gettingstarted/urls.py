from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import resume_builder.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume_builder.urls')),
]

admin.site.site_header = "Resume Site Admin"
admin.site.site_title = "Resume Builder by D. Paul Barden 2019"
admin.site.index_title = "Resume Site Admin"