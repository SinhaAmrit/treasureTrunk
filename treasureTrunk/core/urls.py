from django.urls import path
from core.views import category_list_view, index, product_list_view

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("categories/", category_list_view, name="category-list"),
]
