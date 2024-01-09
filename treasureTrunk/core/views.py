from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from taggit.models import Tag
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


def product_detail_view(request, pid):
    product = get_object_or_404(Product, pid=pid)
    related_products = Product.objects.filter(category=product.category).exclude(
        pid=pid
    )
    reviews = ProductReviews.objects.filter(product=product).order_by("-date")
    avg_rating = ProductReviews.objects.filter(product=product).aggregate(
        rating=Avg("rating")
    )
    p_image = product.p_images.all()
    context = {
        "p_image": p_image,
        "product": product,
        "reviews": reviews,
        "avg_rating": avg_rating,
        "related_products": related_products,
    }
    return render(request, "core/product-detail.html", context)


def category_list_view(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "core/category-list.html", context)


def category_product_list_view(request, cid):
    category = get_object_or_404(Category, cid=cid)
    products = Product.objects.filter(product_status="published", category=category)
    context = {"category": category, "products": products}
    return render(request, "core/category-product-list.html", context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {"vendors": vendors}
    return render(request, "core/vendor-list.html", context)


def vendor_detail_view(request, vid):
    # vendor = Vendor.objects.get(vid=vid)
    vendor = get_object_or_404(Vendor, vid=vid)
    products = Product.objects.filter(product_status="published", vendor=vendor)
    context = {"vendor": vendor, "products": products}
    return render(request, "core/vendor-detail.html", context)


def tag_list_view(request, tag_slug):
    products = Product.objects.filter(product_status="published").order_by("-id")
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])
    context = {"products": products, "tag": tag}
    return render(request, "core/tag-list.html", context)
