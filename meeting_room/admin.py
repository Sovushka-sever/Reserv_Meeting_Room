from django.contrib import admin
from .models import (
    MeetingRoom,
    Reservation,
)


@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'capacity',
        'description',
        'projector',
        'marker_board'
    )
    search_fields = ('title', 'capacity')
    list_filter = ('title', 'capacity',)
    empty_value_display = '-пусто-'


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'start_time',
        'end_time',
        'meeting_name',
        'meeting_room',
        'attendees',
        'status',
        'add_date',
    )
    search_fields = ('author', 'status')
    list_filter = ('start_time', 'end_time', 'meeting_name')
    empty_value_display = '-пусто-'
    fieldsets = (
        (None, {'fields': ('author', 'meeting_name', )}),
        (
            'Meeting room',
            {
                'fields': (
                    (
                        'meeting_room',
                    ),
                )
            },
        ),
        (
            'Meeting information',
            {
                'fields': (
                    'start_time',
                    'end_time',
                    'attendees',
                    'status',
                ),
            },
        ),
    )
