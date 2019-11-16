from django.urls import path

from webapp.views import IndexView, ProductCreateView, ReviewCreateView, ProductView, ProductUpdateView
app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='update'),

    path('review/add/', ReviewCreateView.as_view(), name='review_add'),


]
