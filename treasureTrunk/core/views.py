from django.http import HttpResponse
from django.shortcuts import render
from core.models import (
    Product,
    Category,
    Vendor,
    CartOrder,
    CartOrderItems,
    ProductImages,
    ProductReviews,
    wishlist,
    Address,
)


def index(request):
    products = Product.objects.filter(
        product_status="published", featured=True
    ).order_by("-date")
    context = {"products": products}
    return render(request, "core/index.html", context)


def product_list_view(request):
    products = Product.objects.filter(
        product_status="published", featured=True
    ).order_by("-date")
    context = {"products": products}
    return render(request, "core/product-list.html", context)


def category_list_view(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "core/category-list.html", context)


def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)
    context = {"category": category, "products": products}
    return render(request, "core/category-product-list.html", context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {"vendors": vendors}
    return render(request, "core/vendor-list.html", context)


def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(product_status="published", vendor=vendor)
    context = {"vendor": vendor, "products": products}
    return render(request, "core/vendor-detail.html", context)
