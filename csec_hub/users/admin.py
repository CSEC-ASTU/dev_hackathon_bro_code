from django.contrib import admin
from .models import Division, Membership, Authority


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_filter = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    search_fields = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    list_editable = ('is_active',)
    ordering = ('-created_at',)

<<<<<<< Updated upstream
@admin.register(Membership)
=======
<<<<<<< Updated upstream
@admin.register(Memebership)
>>>>>>> Stashed changes
class MemebershipAdmin(admin.ModelAdmin):
    list_display = ('school_id','member_of','member_authority', 'created_at', 'updated_at', 'is_active','is_accepted')
    list_filter = ('is_accepted', 'created_at', 'updated_at', 'is_active')
=======
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('school_id','member_authority', 'created_at', 'updated_at','is_accepted')
    list_filter = ('is_accepted', 'created_at', 'updated_at')
>>>>>>> Stashed changes
    search_fields = ('is_accepted', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    list_editable = ('is_accepted',)
    ordering = ('-created_at',)

@admin.register(Authority)
class AuthorityAdmin(admin.ModelAdmin):
    list_display = ('position', 'description', 'created_at', 'updated_at', 'is_active')
    list_filter = ('position', 'description', 'created_at', 'updated_at', 'is_active')
    search_fields = ('position', 'description', 'created_at', 'updated_at', 'is_active')
    list_per_page = 10
    ordering = ('-created_at',)



 



