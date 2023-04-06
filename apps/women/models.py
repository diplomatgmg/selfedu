from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, db_index=True, null=True
    )

    def __str__(self):
        return f"id: {self.id}, {self.title}"
