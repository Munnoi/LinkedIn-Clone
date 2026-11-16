from django.urls import path
from .views import ProfileView, ExperienceView, SkillView, EducationView, ProjectView

urlpatterns = [
    path("api/profile/me/", ProfileView.as_view()), # tested.
    path("api/experience/me/", ExperienceView.as_view()), # tested.
    path("api/skill/me/", SkillView.as_view()), # tested.
    path("api/education/me/", EducationView.as_view()), # tested.
    path("api/project/me/", ProjectView.as_view()), # tested.
]
