from django.contrib import admin
from crud_app.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'age', 'email', 'phone', 'address', 'created_at']
    search_fields = ['full_name', 'email', 'phone']
    list_filter = ['created_at']
    list_per_page = 5
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'age', 'email', 'phone', 'address', 'profile_pic')
        }),
        ('Important dates', {
            'fields': ('created_at', 'updated_at')
        })
    )
    filter_horizontal = ['full_name']
    raw_id_fields = ['full_name']
    ordering = ['created_at']
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    save_as = True
    save_on_top = True
    save_on_bottom = False
    show_full_result_count = True
    show_admin_actions = True

# Register your models here.
