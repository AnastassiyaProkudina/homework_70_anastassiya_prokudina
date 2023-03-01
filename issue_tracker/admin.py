from django.contrib import admin

from issue_tracker.models import Issue, Status, Type


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "summary",
        "description",
        "status",
        "get_type",
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
        "deleted_at",
    )
    search_fields = ("id", "summary", "status", "get_type")
    fields = ("summary", "description", "status", "get_type")
    readonly_fields = ("id", "created_at", "updated_at", "deleted_at", "is_deleted")

    def get_type(self, instance):
        return [type.name for type in instance.type.all()]


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
