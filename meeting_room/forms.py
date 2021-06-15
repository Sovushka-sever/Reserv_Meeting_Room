from django import forms
from meeting_room.models import Reservation, MeetingRoom


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = (
            'author',
            'meeting_name',
            'meeting_room',
            'attendees',
            'status',
            'start_time',
            'end_time',
        )


class MeetingRoomForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        fields = (
            'title',
            'capacity',
            'description',
            'projector',
            'marker_board',
        )
