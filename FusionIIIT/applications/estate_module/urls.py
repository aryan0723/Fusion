from django.urls import path

from . import views

urlpatterns = [
    path('', views.estate, name="estate_module_home"),
    path('new/building', views.newBuilding, name="new_building"),
    path('edit/building/<building_id>', views.editBuilding, name="edit_building"),
    path('delete/<building_id>', views.deleteBuilding, name="delete_building"),
    path('new/work', views.newWork, name="new_work"),
    path('edit/work/<work_id>', views.editWork, name="edit_work"),
    path('delete/work/<work_id>', views.deleteWork, name="delete_work"),
]
