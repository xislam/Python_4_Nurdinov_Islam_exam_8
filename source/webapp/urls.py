from django.urls import path

from webapp.views import IndexView, ProductCreateView, ReviewCreateView, ProductView, ProductUpdateView, \
    ProductDeleteView

app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),

    path('review/add/', ReviewCreateView.as_view(), name='review_add'),


]
