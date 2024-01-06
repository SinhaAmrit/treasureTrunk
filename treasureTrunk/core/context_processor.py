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


def default(request):
    categories = Category.objects.all()
    return {
        "categories": categories,
    }
