from django.contrib import admin

from issue_tracker.models import Issue, Status, Type


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "summary",
        "description",
        "status",
        "type_old",
        "created_at",
        "updated_at",
        "deleted_at",
        "is_deleted",
    )
    list_filter = (
        "id",
        "summary",
        "description",
        "status",
        "type_old",
        "created_at",
        "deleted_at",
    )
    search_fields = ("id", "summary", "status", "type_old")
    fields = ("summary", "description", "status", "type_old")
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
