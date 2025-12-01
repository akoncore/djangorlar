from django.db.models import (
    CharField,
    TextField,
    IntegerField,
    BooleanField,
    ForeignKey,
    CASCADE,
    DecimalField,
    PositiveSmallIntegerField
) 
from apps.abstracts.models import AbstractBaseModel
from django.conf import settings

class Course(AbstractBaseModel):
    title = CharField(max_length=40)
    description = TextField()
    is_active = BooleanField(blank=True,null=True,default=True)
    owner = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name="owned_courses"
    )
    
    def __str__(self):
        return self.title


class Lesson(AbstractBaseModel):
    course = ForeignKey(
        Course,
        on_delete=CASCADE,
        related_name="lessons"
    )

    title = CharField(max_length=255)
    content = TextField()

    order = DecimalField(max_digits=5, decimal_places=2, default=0)
    indentation = PositiveSmallIntegerField(default=0)
    is_published = BooleanField(default=False)


    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
