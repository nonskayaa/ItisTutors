from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView
)
from .models import TutorInfo


def home(request):
    context = {
        'TutorInfos': TutorInfo.objects.all()
    }
    return render(request, 'tutors/list.html', context)


class TutorInfoListView(ListView):
    model = TutorInfo
    template_name = 'tutors/list.html'
    context_object_name = 'TutorInfos'
    paginate_by = 3

class TutorDetailView(ListView):
    model = TutorInfo
    template_name = 'tutorinfo_detail.html'
    context_object_name = 'TutorInfo'
    #paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return TutorInfo.user


class TutorInfoDetailView(DetailView):
    model = TutorInfo


#def about(request):
#    return render(request, 'tutors/about.html', {'title': 'О Тьюторах'})