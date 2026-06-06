from django.shortcuts import render
from .models import Video
from .forms import VideoForm


def landing(request):
    return render(request, 'landing.html')


def video_list(request):
    videos = Video.objects.all().order_by('-created_at')
    return render(request, 'video_list.html', {'videos': videos})


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'form_video.html', {
                'form': VideoForm(),
                'success': True,
            })
        else:
            return render(request, 'form_video.html', {
                'form': form,
                'success': False,
            })
    else:
        form = VideoForm()
    return render(request, 'form_video.html', {'form': form})