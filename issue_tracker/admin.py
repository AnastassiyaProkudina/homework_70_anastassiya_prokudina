from django.contrib import admin

from issue_tracker.models import Issue, Status, Type


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "created_at", "updated_at", "deleted_at", "is_deleted")


class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "title")
    list_filter = ("id", "name", "title")
    search_fields = ("id", "name", "title")
    fields = ("name", "title")


class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "title")
    list_filter = ("id", "name", "title")
    search_fields = ("id", "name", "title")
    fields = ("name", "title")


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
