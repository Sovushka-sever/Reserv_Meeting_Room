from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class MeetingRoom(models.Model):
    """
    Model for storing information about meeting rooms.
    """
    title = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='room name',
    )
    capacity = models.PositiveIntegerField(
        default=1,
        verbose_name='number of seats',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='additional information',
    )
    projector = models.BooleanField(
        default=False,
        null=False,
        blank=False)
    marker_board = models.BooleanField(
        default=False,
        null=False,
        blank=False)

    def __str__(self):
        return f'{self.title} {self.description}'


class Reservation(models.Model):
    """
    Model for booking meeting rooms.
    """
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='the author of the reservation',
    )
    meeting_name = models.CharField(
        unique=True,
        max_length=200,
        null=False,
    )
    meeting_room = models.ForeignKey(
        MeetingRoom,
        on_delete=models.CASCADE
    )
    attendees = models.CharField(
        max_length=1000,
        default=' ',
        verbose_name='names of participants',
    )

    def __str__(self):
        return f'{self.author} {self.meeting_name} {self.attendees}'

    class Meta:
        ordering = ('-start_time',)

