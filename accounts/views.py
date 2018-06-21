from datetime import timedelta
from json import dumps

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from django.utils import timezone

from . import user_verification


@login_required
def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)


@login_required
def profile(request, user):
    context = {
        'chosen_user': User.objects.get(username=user),
    }

    time_difference = timezone.now() - context['chosen_user'].profile.last_ping
    context['chosen_user_online'] = bool(time_difference < timedelta(0, 70))

    return render(request, 'accounts/profile.html', context)


@login_required
def user_status(request):
    data = request.body.decode('utf-8').split('@')

    if data[0] == 'U':
        session = Session.objects.get(session_key=data[1])
        user_id = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=user_id)

        user.profile.last_ping = timezone.now()
        user.save()

        payload = {'success': True}

    elif data[0] == 'R':
        user = User.objects.get(pk=data[1])

        time_difference = timezone.now() - user.profile.last_ping
        status = bool(time_difference < timedelta(0, 40))

        payload = {'success': True, 'status': status}

    else:
        payload = {'success': False}

    return HttpResponse(dumps(payload), content_type='application/json')


# Remove disable ASAP.
# pylint: disable-msg=too-many-branches
@login_required
def settings(request):
    context = {
        'errors': [],
        'successful_changes': [],
    }

    if request.method == 'POST':
        user = request.user

        user_first_name = request.POST['first_name']
        user_last_name = request.POST['last_name']
        user_profile_biography = request.POST['profile_biography']
        user_profile_url = request.POST['profile_url']

        profile_clean = user_verification.clean_profile_changes(
            user_first_name,
            user_last_name,
            user_profile_biography,
            user_profile_url,
            user
        )
        user = profile_clean[0]
        context['successful_changes'] += profile_clean[1]
        context['errors'] += profile_clean[2]

        # Profile Images
        file_system = FileSystemStorage()
        
        background = request.FILES.get('background', False)
        if background:
            fs = FileSystemStorage()
            extension = background.name[background.name.rfind("."):]
            filename = request.user.username + '_background' + extension
            if default_storage.exists(filename):
                default_storage.delete(filename)
            image = fs.save(filename, background)
            user.profile.background = image

        avatar = request.FILES.get('avatar', False)
        if avatar:
            fs = FileSystemStorage()
            extension = avatar.name[avatar.name.rfind("."):]
            filename = request.user.username + '_avatar' + extension
            if default_storage.exists(filename):
                default_storage.delete(filename)
            image = fs.save(filename, avatar)
            user.profile.avatar = image

        # Account
        user_username = request.POST['username']
        user.username = user_username
        # End of account

        user_old_pword = request.POST['old_pword']
        user_new_pword = request.POST['new_pword']
        user_new_pword_conf = request.POST['new_pword_conf']

        password_clean = user_verification.clean_password_changes(
            user_old_pword,
            user_new_pword,
            user_new_pword_conf,
            user,
            request
        )
        user = password_clean[0]
        context['successful_changes'] += password_clean[1]
        context['errors'] += password_clean[2]

        user.save()

    return render(request, 'accounts/settings.html', context)
