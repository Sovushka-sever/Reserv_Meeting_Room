from django.db import models
from django.utils import timezone
from users.models import User

STATUS_RESERVE_CHOICES = (
    ('rejected', 'Rejected'),
    ('approved', 'Approved'),
    ('initiate', 'Initiate')
)


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
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    add_date = models.DateTimeField(
        verbose_name='date of creation',
        auto_now_add=True
    )
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
        on_delete=models.CASCADE,
        related_name='reserve'
    )
    attendees = models.CharField(
        max_length=1000,
        default=' ',
        verbose_name='names of participants',
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_RESERVE_CHOICES,
        default='initiate'
    )

    def __str__(self):
        return f'{self.author} {self.meeting_name} {self.attendees}'

    class Meta:
        ordering = ('-start_time',)
