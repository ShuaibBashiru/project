from django.urls import path
from . import views, testfile, pso


urlpatterns = [
    path('', views.index, name="home"),
    path('test/', testfile.testing, name="home"),
    path('f1/', pso.func1, name="function_one"),
    path('f2/', pso.func2, name="function_two"),
    path('f3/', pso.func3, name="function_three"),
    path('f4/', pso.func4, name="function_four"),
    path('f5/', pso.func5, name="function_five"),
    path('f6/', pso.func6, name="function_six"),
    path('f7/', pso.func7, name="function_seven"),
    path('f8/', pso.func8, name="function_eight"),
    # path('f9/', pso.func9, name="function_nine"),

]
