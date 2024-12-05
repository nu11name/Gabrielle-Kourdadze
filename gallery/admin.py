from django.contrib import admin
from .models import (
    Painting,
    WorkOnPaper,
    ExhibitionCategory,
    Exhibition,
    ExhibitionImage,
    Education,
    Residency,
    Fair,
    GroupExhibition,
    PersonalExhibition,
    TextsPublications
)

# Inline for Exhibition Images
class ExhibitionImageInline(admin.TabularInline):
    model = ExhibitionImage
    extra = 1

# Admin for Painting
@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# Admin for Works on Paper
@admin.register(WorkOnPaper)
class WorkOnPaperAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# Admin for Exhibition Categories
@admin.register(ExhibitionCategory)
class ExhibitionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Admin for Exhibitions
@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'location',)
    list_filter = ('location',)
    search_fields = ('title', 'location__name')
    inlines = [ExhibitionImageInline]

# Admin for Education
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('education',)
    search_fields = ('education',)

# Admin for Residencies
@admin.register(Residency)
class ResidencyAdmin(admin.ModelAdmin):
    list_display = ('location',)
    search_fields = ('location',)

# Admin for Fairs
@admin.register(Fair)
class FairAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)

# Admin for Group Exhibitions
@admin.register(GroupExhibition)
class GroupExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)

# Admin for Personal Exhibitions
@admin.register(PersonalExhibition)
class PersonalExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)

# Admin for Texts and Publications
@admin.register(TextsPublications)
class TextsPublicationsAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'subtitle_en')
    search_fields = ('title_en', 'subtitle_en')
