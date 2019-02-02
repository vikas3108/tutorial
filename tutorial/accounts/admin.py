from django.contrib import admin

# Register your models here.
from accounts.models import UserProfile,Friend


class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','gender','age','professional_status','company','website','location','skills','github_username','short_bio','image']


admin.site.register(UserProfile,UserProfileAdmin)

admin.site.register(Friend)
