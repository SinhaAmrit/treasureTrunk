from django.urls import path
from core.views import (
    category_list_view,
    category_product_list_view,
    index,
    product_detail_view,
    product_list_view,
    search_view,
    tag_list_view,
    vendor_detail_view,
    vendor_list_view,
)

app_name = "core"

urlpatterns = [
    # Home
    path("", index, name="index"),
    # Tags
    path("products/tags/<slug:tag_slug>", tag_list_view, name="tag-list"),
    # Search
    path("search/", search_view, name="search"),
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
