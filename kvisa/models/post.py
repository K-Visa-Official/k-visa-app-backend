from django.db import models
from ..constants import VISA_CHOICES, LANGUAGE_CHOICES, POST_TYPE_CHOICES
from multiselectfield import MultiSelectField


class Post(models.Model):
    image1 = models.URLField(max_length=500, null=True, blank=True)
    image2 = models.URLField(max_length=500, null=True, blank=True)

    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES
    )
    visa_type = MultiSelectField(
        choices=VISA_CHOICES,
        max_length=100
    )
    post_type = models.CharField(
        max_length=10,
        choices=POST_TYPE_CHOICES
    )

    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    link = models.TextField(max_length=500, blank=True)

    view_count = models.IntegerField(default=0)

    show_start_date = models.DateField(null=True, blank=True)
    show_end_date = models.DateField(null=True, blank=True)
    show_main = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
