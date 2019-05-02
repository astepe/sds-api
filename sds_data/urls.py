from rest_framework.routers import SimpleRouter

from .views import SDSViewSet

router = SimpleRouter()
router.register('sds_data', SDSViewSet, base_name='sds_data')

urlpatterns = router.urls
