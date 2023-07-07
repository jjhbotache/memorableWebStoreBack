from rest_framework import routers
from app_crud.api import App_crudViewSet,WineKindsViewSet

router = routers.DefaultRouter()

router.register('api/Posts',App_crudViewSet)
router.register('api/WineKinds',WineKindsViewSet)

urlpatterns = router.urls
 