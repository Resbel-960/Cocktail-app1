from django.contrib import admin
from .models import *

# Register your models here.


class Tip_categoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tip_category, Tip_categoryAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)

# class TagAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Tag, TagAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class CocktailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cocktail, CocktailAdmin)

class Ingridient_cocktailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ingridient_cocktail, Ingridient_cocktailAdmin)


class TipAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tip, TipAdmin)

class IngridientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ingridient, IngridientAdmin)

class LikeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Like, LikeAdmin)