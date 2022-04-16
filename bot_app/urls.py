from rest_framework.routers import SimpleRouter

from bot_app.views import AnswerViewSet,UserViewSet,TestViewSet,QuectionViewSet

router = SimpleRouter()
router.register('answer',AnswerViewSet,'answer')
router.register('user',UserViewSet,'user')
router.register('test',TestViewSet,'test')
router.register('quection',QuectionViewSet,'quection')

urlpatterns = []
urlpatterns +=router.urls