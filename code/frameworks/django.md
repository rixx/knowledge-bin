# Django

## Setup

 - mkvirtualenv project
 - pip install django psycopg2
 - django-admin startproject project

 - edit manage.py database settings
 - ./manage.py migrate
 - ./manage.py runserver [[0.0.0.0:]8080]

 - ./manage.py startapp app
 - ./manage.py createsuperuser

## Models

 - app/models.py:

    from django.db import models
    class AppClass(models.Model):
        textfield = models.CharField(max_length=200)
        datefield = models.DateTimeField('date published')
        inttfield = models.IntegerField(default=0)
        def somemethod(self):
            return self.intfield > 5
        somemethod.admin_order_field = 'datefield'
        somemethod.boolean = True
        somemethod.short_description = 'Is intfield greater than five?'

 - settings.py:

    INSTALLED_APPS = (
        'app',
    )

 - ./manage.py makemigrations app
 - ./manage.py sqlmigrate app
 - ./manage.py migrate

 - models can have normal functions etc

## Admin

 - admin.site.register(AppClass) in admin.py
 - **oder**: admin.site.register(AppClass, AppClassAdmin)

    from django.contrib import admin
    class AppClassAdmin(admin.ModelAdmin):
        fields = ['datefield', 'intfield', 'textfield'] # order
        list_display = ['textfield', 'somemethod'] # fields in admin overview
        list_filter = ['datefield'] # filters to provide
        search_fields = ['text_field']
        fieldsets = [ # categories
                    (None, {'fields': ['textfield']}),
                    ('Fields with numbers', {'fields': ['datefield, intfield'],
                                             'classes': ['collapse']}) # initially collapsed
                ]
        inlines = [OtherClassInline]
    class OtherClassInline(admin.StackedInline): # or TabularInline
        model = OtherClass
        extra = 3
    admin.site.register(AppClassAdmin)


## Shell

 - ./manage.py shell
 - from app import AppClass
 - AppClass.objects.all()
