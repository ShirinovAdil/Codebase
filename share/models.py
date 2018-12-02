from django.db import models
from django.contrib import admin


class Code(models.Model):
    title = models.CharField(max_length=250, default=" ")
    date = models.DateTimeField(auto_now=True)
    number = models.IntegerField(help_text="Number of exercise on E-Olymp", default=0)

    def __str__(self):
        return self.title


class PersonalCode(models.Model):
    author = models.CharField(max_length=150, default=" ")
    author_code = models.TextField(default=" ", verbose_name="Solution")
    date = models.DateTimeField(auto_now=True)
    code_id = models.ForeignKey(Code, on_delete=models.CASCADE, verbose_name="Related exercise")

    # Could cause problems
    def __str__(self):
        return str(self.code_id) + " - " + str(self.author)

