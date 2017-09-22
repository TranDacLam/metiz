# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class DateTimeModel(models.Model):
    """
    Abstract model that is used for the model using created and modified fields
    """
    created = models.DateTimeField(_('Created Date'), auto_now_add=True,
                                   editable=False)
    modified = models.DateTimeField(
        _('Modified Date'), auto_now=True, editable=False)

    def __init__(self, *args, **kwargs):
        super(DateTimeModel, self).__init__(*args, **kwargs)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Banner(DateTimeModel):
    image = models.ImageField(max_length=1000, upload_to="banners")
    sub_url = models.CharField(max_length=1000)
    is_show = models.BooleanField(default=False)
    position = models.IntegerField()

    def __str__(self):
        return '%s' % (self.sub_url)


@python_2_unicode_compatible
class Rated(DateTimeModel):
    name = models.CharField(max_length=255)
    icon = models.ImageField(max_length=255, upload_to="rated_icon")

    def __str__(self):
        return '%s' % (self.name)


@python_2_unicode_compatible
class Genre(DateTimeModel):
    # using name as key mapping genre 18, populate ..etc
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)

    def __str__(self):
        return '%s' % (self.name)


@python_2_unicode_compatible
class MovieType(DateTimeModel):
    # using name as key mapping class css display in list film or film detail (2d, 3d)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)

    def __str__(self):
        return '%s' % (self.name)


@python_2_unicode_compatible
class Movie(DateTimeModel):
    name = models.CharField(max_length=255)
    poster = models.ImageField(
        _('Poster'), max_length=255, upload_to="poster_film")
    director = models.CharField(max_length=255)
    cast = models.CharField(max_length=255)
    time_running = models.IntegerField(_('Time Running'))
    release_date = models.DateField()
    rated = models.ForeignKey('Rated', related_name='film_rated_rel')
    genre = models.ForeignKey('Genre', related_name='film_genre_rel')
    movie_type = models.ForeignKey('MovieType', related_name='film_type_rel')
    language = models.CharField(max_length=255)
    description = models.TextField()
    trailer = models.CharField(max_length=500)
    priority = models.IntegerField()
    is_draff = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.name)


@python_2_unicode_compatible
class CenimaTechnology(DateTimeModel):
    # Post static pages : IMAX, GOLD_CARD, 4D ..etc..
    name = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return '%s' % (self.name)


@python_2_unicode_compatible
class NewOffer(DateTimeModel):
    GENDER =(
        ('all', 'ALL'),
        ('member', 'Member')
    )
    name = models.CharField(max_length=50)
    image = models.ImageField(max_length=255, upload_to="new_offer")
    content = models.TextField()
    condition = models.TextField()
    apply_for = models.CharField(max_length=50, choices=GENDER)
    priority = models.IntegerField()
    apply_date = models.DateField(auto_now=True)
    movies = models.ManyToManyField('Movie')

    def __str__(self):
        return '%s' % (self.name)


