from django.urls import path
from api import views


urlpatterns = [
    path('task_lists/', views.ListOfTaskLists.as_view()),
    path('task_lists/<int:pk>/', views.TaskListDetail.as_view()),
    # path('task_lists/<int:pk>/tasks/', views.category_product)
]


# urlpatterns = [
#     path('task_lists/', views.task_list),
#     path('task_lists/<int:pk>/', views.task_list_detail),
#     path('task_lists/<int:pk>/tasks/', views.category_product)
# ]