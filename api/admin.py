from django.contrib import admin

# Register your models here.
# モデルの読み込み
from .models import Task
# アドミんで指定
admin.site.register(Task)