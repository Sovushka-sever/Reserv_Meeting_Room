from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from .models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from .forms import CreationForm


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    @action(
        methods=('get', 'patch'),
        detail=False,
        permission_classes=(IsAuthenticated,)
    )
    def me(self, request):
        user_profile = get_object_or_404(
            User,
            id=request.user.id
        )
        if request.method == 'GET':
            serializer = UserSerializer(user_profile)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        serializer = UserSerializer(
            user_profile,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(
            role=user_profile.role,
            avatar=user_profile.avatar,
            bio=user_profile.bio,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class SignUp(CreateView):
    form_class = CreationForm
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if not form.is_valid():
            return render(request, 'signup.html', {'form': form})

        user = form.save()
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )
        login(request, user)
        return redirect('index')


