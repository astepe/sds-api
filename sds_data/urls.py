from rest_framework.routers import SimpleRouter

from .views import SDSViewSet, ManufacturerViewSet

router = SimpleRouter()
router.register('manufacturers', ManufacturerViewSet, base_name='manufacturers')
router.register('', SDSViewSet, base_name='sds_data')

urlpatterns = router.urls
