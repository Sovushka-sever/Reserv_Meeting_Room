from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from meeting_room.forms import MeetingRoomForm, ReservationForm
from meeting_room.models import Reservation, MeetingRoom
from users.models import User


@login_required
def index(request):
    meeting_rooms = MeetingRoom.objects.filter()
    reservations = Reservation.objects.filter()
    return render(request, 'index.html', {
        'meeting_rooms': meeting_rooms,
        'reservations': reservations,
    })


def role_check(user):
    return True if user.is_office_manager else False


@user_passes_test(role_check, login_url='/')
def new_meting_room(request):
    """New meting room."""
    form = MeetingRoomForm(
        request.POST or None,
        files=request.FILES or None
    )
    if form.is_valid():
        room = form.save(commit=False)
        room.save()
        return redirect('index')
    return render(
        request,
        'new_meting_room.html',
        {'is_edit': False,
         'form': form}
    )


@user_passes_test(role_check, login_url='/')
def meting_room_edit(request, room_id):
    """Edit meting room."""
    room = get_object_or_404(MeetingRoom, pk=room_id)
    if User.role == User.is_employee:
        return redirect('meeting_room', room_id=room_id)
    form = MeetingRoomForm(
        request.POST or None,
        instance=room)
    if form.is_valid():
        form.save()
        return redirect('meeting_room', room_id=room_id)
    return render(
        request,
        'new_meting_room.html',
        {'is_edit': True, 'room': room, 'form': form}
    )


@user_passes_test(role_check, login_url='/')
def meting_room_view(request, room_id):
    """Info meting room."""
    meeting_room = get_object_or_404(MeetingRoom, pk=room_id)
    reservations = Reservation.objects.filter(meeting_room=meeting_room)
    return render(
        request,
        'room.html',
        {'meeting_room': meeting_room,
         'reservations': reservations}
    )


@user_passes_test(role_check, login_url='/')
def meeting_room_delete(request, room_id):
    """Delete meting room."""
    meeting_room = get_object_or_404(MeetingRoom, pk=room_id)
    meeting_room.delete()
    return redirect('index')


@login_required
def new_reserve(request):
    """New reservation."""
    form = ReservationForm(
        request.POST or None,
        files=request.FILES or None
    )
    if form.is_valid():
        reservation = form.save(commit=False)
        reservation.save()
        return redirect('index')
    return render(
        request,
        'new_reserve.html',
        {'is_edit': False,
         'form': form}
    )


@login_required
def reserve_edit(request, room_id, reserve_id):
    """Edit reservation."""
    meeting_room = get_object_or_404(MeetingRoom, room_id=room_id)
    reservation = get_object_or_404(
        ReservationForm,
        pk=reserve_id,
        meeting_room=meeting_room
    )
    form = ReservationForm(
        request.POST or None,
        instance=reservation)
    if form.is_valid():
        form.save()
        return redirect('new_reserve', reserve_id=reserve_id)
    return render(
        request,
        'new_reserve.html',
        {'is_edit': True, 'reservation': reservation, 'form': form}
    )


@login_required
def reserve_delete(request, reserve_id):
    """Delete reservation."""
    meeting_room = get_object_or_404(MeetingRoom, reserve_id=reserve_id)
    meeting_room.delete()
    return redirect('index')
