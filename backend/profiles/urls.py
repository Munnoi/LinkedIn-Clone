from django.urls import path
from .views import ProfileView, ExperienceView, SkillView

urlpatterns = [
    path("api/profiles/me/", ProfileView.as_view()), # tested.
    path("api/experience/me/", ExperienceView.as_view()), # tested.
    path("api/skills/me/", SkillView.as_view()), # tested.
    # TODO: include the 'projects' and 'education' model urls.
]
