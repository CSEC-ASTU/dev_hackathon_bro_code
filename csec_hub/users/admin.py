from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import Excuitive, User, Division, Membership, Authority
from django.utils.translation import gettext_lazy as _


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
@admin.register(User)
class UserAdmin(UserAdmin):
	form = UserChangeForm

	fieldsets = (
	        (None, {'fields': ('email', 'phone', 'password',)}),
		(_('Personal info'), {'fields': ('first_name', 'last_name', )}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined', )}),
			
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide', ),
			'fields': ('email', 'phone', 'password1', 'password2', ),
		}),
	)
	list_display = ['email', 'first_name', 'last_name', 'is_staff', "phone", 'is_active']
	search_fields = ('email', 'first_name', 'last_name', )
	ordering = ('email', )
@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_filter = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    search_fields = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    list_editable = ('is_active',)
    ordering = ('-created_at',)

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('school_id','member_of', 'created_at', 'updated_at', 'is_active','is_accepted')
    list_filter = ('is_accepted', 'created_at', 'updated_at', 'is_active')
    search_fields = ('is_accepted', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    list_editable = ('is_accepted',)
    ordering = ('-created_at',)

@admin.register(Excuitive)
class ExcutiveAdmin(admin.ModelAdmin):
    list_display = ('user', 'authority', 'is_accepted', 'created_at', 'updated_at', 'is_active')
    list_filter = ('is_accepted', 'created_at', 'updated_at', 'is_active')
    search_fields = ('is_accepted', 'created_at', 'updated_at', 'is_active')
    
@admin.register(Authority)
class AuthorityAdmin(admin.ModelAdmin):
    list_display = ('position', 'description', 'created_at', 'updated_at', 'is_active')
    list_filter = ('position', 'description', 'created_at', 'updated_at', 'is_active')
    search_fields = ('position', 'description', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    ordering = ('-created_at',)

 



