from django.contrib import admin

from myapp.models import *


admin.site.register(Custom_user)
admin.site.register(viewersProfileModel) 
admin.site.register(BloggerProfileModel) 
admin.site.register(BlogPostModel)    
