from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema
from drf_yasg       import openapi

from api.models import User


class ApiTestView(APIView):
    
    permission_classes = [AllowAny]
    
    post_params = openapi.Schema(
        type       = openapi.TYPE_OBJECT,
        required   = ['nickname'],
        properties = {
            'nickname': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    )
    
    @swagger_auto_schema(request_body=post_params, responses={201: '유저 닉네임이 생성되었습니다.'})
    def post(self, request):
        nickname = request.data.get('nickname')
        if not nickname:
            return Response({'message': '유저 닉네임은 필수값입니다.'}, status=400)
        
        if User.objects.filter(nickname=nickname).exists():
            return Response({'message': f'유저 닉네임 {nickname}은/는 이미 존재합니다.'}, status=400)
        
        user = User.objects.create(nickname=nickname)
        
        return Response({'message': f'유저 닉네임 {user.nickname}이/가 생성되었습니다.'}, status=201)