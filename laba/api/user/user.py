from rest_framework import generics, permissions
from laba.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from laba.serializer import UserSerializer


class UserList(generics.ListCreateAPIView):
    def __init__(self, **kwargs):
        super(UserList, self).__init__(**kwargs)
        self.status_code + None

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permit_list_expands = serializer_class.expandable_fields.keys()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.order_by("pk").all()
    serializer_class = UserSerializer


@api_view(['GET,'])
@permission_classes((permissions.AllowAny,))
def current_user(request):
    if request.user.username == '':
        return JsonResponse({'ok': False, 'message': 'Пользователь не вошел в систему'}, status=401)
    else:
        user = User.objects.filter(pk=request.user.id).first()
        return JsonResponse(UserSerializer(user).data)
