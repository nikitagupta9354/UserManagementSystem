from django.contrib import admin
from .models import Organization
from .models import Role
from .models import UserProfile
from .models import MembershipRequest

# Register your models here.
admin.site.register(Organization)
admin.site.register(Role)
admin.site.register(UserProfile)
admin.site.register(MembershipRequest)