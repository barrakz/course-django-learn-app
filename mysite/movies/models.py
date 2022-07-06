from django.db import models

# Create your models here.


class Actor(models.Model):
    GENDERS = [
        ("W", "Woman"),
        ("M", "Man")
    ]

    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(choices=GENDERS, max_length=1)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Movie(models.Model):
    GENRES = [
        ("A", "Action"),
        ("F", "Fantasy"),
        ("SF", "Science Fiction"),
        ("R", "Romance")
    ]

    title = models.CharField(max_length=128)
    genre = models.CharField(choices=GENRES, max_length=2)
    year = models.IntegerField()
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name="movies", blank=True, null=True
    )
    country = models.ForeignKey(
        "Country", on_delete=models.CASCADE, related_name="movies", blank=True, null=True
    )

    def __str__(self):
        return f"{self.title}"


class Country(models.Model):
    name = models.CharField(max_length=128)
    iso_code = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.name}"


class Oscar(models.Model):
    CATEGORIES = [
        ("BAT", "Best Actor"),
        ("BAS", "Best Actress"),
        ("BPC", "Best Picture")
    ]
    category = models.CharField(choices=CATEGORIES, max_length=3)
    year = models.IntegerField()
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name="oscars", blank=True, null=True
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="oscars", blank=True, null=True
    )

    def __str__(self):
        return f"{self.get_category_display()} {self.year}"


