# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from core.custom_models import *
import datetime
from django.utils.translation import ugettext_lazy as _


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
    POSITION = (
        (1, 1),
        (2, 2),
    )
    image = models.ImageField(_("Image"), max_length=1000, upload_to="banners")
    sub_url = models.CharField(_("Sub Url"), max_length=1000)
    is_show = models.BooleanField(_("Is Show"), default=False)
    position = models.IntegerField(_("Position"), choices=POSITION)

    def __str__(self):
        return '%s' % (self.sub_url)

    class Meta:
        verbose_name = _('Banner')


@python_2_unicode_compatible
class Rated(DateTimeModel):
    # using name as key mapping genre 18, populate ..etc
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), max_length=255)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = _('Rated')


@python_2_unicode_compatible
class Genre(DateTimeModel):
    name = models.CharField(_("Name Genre"), max_length=50)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')


@python_2_unicode_compatible
class MovieType(DateTimeModel):
    # using name as key mapping class css display in list film or film detail
    # (2d, 3d)
    TYPE = (
        ('', '----'),
        ('2d', '2D'),
        ('3d', '3D'),
        ('4dx', '4DX'),
        ('imax', 'IMAX'),
        ('screenx', 'SCREEN X'),
    )
    name = models.CharField(_("Type Name"), max_length=50, choices=TYPE)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = _('Movie Type')
        verbose_name_plural = _('Movie Types')


@python_2_unicode_compatible
class Movie(DateTimeModel):
    name = models.CharField(_("Movie Name"), max_length=255)
    poster = models.ImageField(
        _('Poster'), max_length=255, upload_to="poster_film")
    director = models.CharField(_("Director"), max_length=255)
    cast = models.CharField(_("Cast"), max_length=255)
    time_running = models.IntegerField(_('Time Running'))
    release_date = models.DateField(_("Release Date"))
    rated = models.ForeignKey("Rated", related_name='film_rated_rel')
    genre = models.ForeignKey("Genre", related_name='film_genre_rel')
    movie_type = models.ForeignKey("MovieType", related_name='film_type_rel')
    language = models.CharField(_("Language"), max_length=255)
    description = models.TextField(_("Description"))
    trailer = models.CharField(_("Trailer"), max_length=500)
    priority = models.IntegerField(_("Priority"), null=True, blank=True)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')


@python_2_unicode_compatible
class Comment(DateTimeModel):
    STAR = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    full_name = models.CharField(_("Full Name"), max_length=100)
    avatar = models.ImageField(_("Avatar"),
        max_length=500, upload_to="comment_avatar", null=True, blank=True)
    review = models.TextField(_("Review"))
    rating = models.IntegerField(_("Rating"), default=5, choices=STAR)
    date_post = models.DateField(_("Date Post"))
    movie = models.ForeignKey('Movie', related_name='movie_comment_rel')

    def __str__(self):
        return '%s' % (self.full_name)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


@python_2_unicode_compatible
class CenimaTechnology(DateTimeModel):
    # Post static pages : IMAX, GOLD_CARD, 4D ..etc..
    TECHNOLOGY = (
        ('4dx', '4DX'),
        ('sweetbox', 'SWEETBOX'),
        ('dolby-atmos', 'DOLBY ATMOS'),
        ('imax', 'IMAX'),
        ('gold-class', 'GOLD CLASS'),
        ('lamour', 'LAMOUR'),
        ('starium', 'STARIUM'),
        ('premium', 'PREMIUN CENIMA'),
        ('screenx', 'SCREEN X')
    )
    name = models.CharField(_("Name"), max_length=50, choices=TECHNOLOGY)
    content = models.TextField(_("Content"))

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = _('Cenima Technology')
        verbose_name_plural = _('Cenima Technologys')


@python_2_unicode_compatible
class NewOffer(DateTimeModel):
    GENDER = (
        ('all', 'ALL'),
        ('member', 'Member')
    )

    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), max_length=255, upload_to="new_offer")
    content = models.TextField(_("Content"), null=True, blank=True)
    condition = models.TextField(_("Condition"), null=True, blank=True)
    apply_for = models.CharField(_("Apply For"), max_length=50, default='all', choices=GENDER)
    priority = models.IntegerField(_("Priority"), null=True, blank=True)
    apply_date = models.DateField(_("Apply Date"), default=datetime.date.today, editable=True)
    movies = models.ManyToManyField('Movie', blank=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = _('New Offer')
        verbose_name_plural = _('New Offers')


@python_2_unicode_compatible
class Post(DateTimeModel):
    name = models.CharField(_("Name"), max_length=50)
    content = models.TextField(_("Content"))
    key_query = models.CharField(_("Key Query"), max_length=255, unique=True)
    is_draft = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.key_query = "kq_" + self.key_query.replace(" ", "_")
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


@python_2_unicode_compatible
class SlideShow(DateTimeModel):
    image = models.ImageField(_("Image"), max_length=255, upload_to="slide_home")
    priority = models.IntegerField(_("Priority"), null=True, blank=True)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.image)

    class Meta:
        verbose_name = _('Slide Show')
