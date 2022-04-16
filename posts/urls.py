from rest_framework.routers import SimpleRouter

from posts.views import (
    CategoryViewSet,
    SubcategoryViewSet,
    ProductViewSet,
    ImageViewSet,
)

router = SimpleRouter()

router.register("category",CategoryViewSet,"category")
router.register("subcategory",SubcategoryViewSet,"subcategory")
router.register("product",ProductViewSet,"product")
router.register("images",ImageViewSet,"images")

urlpatterns = []
urlpatterns += router.urls
