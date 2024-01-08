from django.urls import path
from core.views import (
    category_list_view,
    category_product_list_view,
    index,
    product_detail_view,
    product_list_view,
    vendor_detail_view,
    vendor_list_view,
)

app_name = "core"

urlpatterns = [
    # Home
    path("", index, name="index"),
    # Products
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),
    # Categories
    path("categories/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),
    # Vendors
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>/", vendor_detail_view, name="vendor-detail"),
]
