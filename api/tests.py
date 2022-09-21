import json

from rest_framework.test import APITestCase

from api.models import User


class ApiTestViewTest(APITestCase):
    
    maxDiff = None
    
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            nickname = 'superuser'
        )
    
    def test_success_api_test(self):
        data = {
            'nickname': 'user'
        }
        
        response = self.client\
                       .post('/api/test', data=json.dumps(data), content_type='application/json')
                       
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            {
                'message': '유저 닉네임 user이/가 생성되었습니다.'
            }  
        )
        
    def test_fail_api_test_due_to_nickname_required(self):
        data = {}
        
        response = self.client\
                       .post('/api/test', data=json.dumps(data), content_type='application/json')
                       
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.json(),
            {
                'message': '유저 닉네임은 필수값입니다.'
            }  
        )
    
    def test_fail_api_test_due_to_already_existed_nickname(self):
        data = {
            'nickname': 'superuser'
        }
        
        response = self.client\
                       .post('/api/test', data=json.dumps(data), content_type='application/json')
                       
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {
                'message': '유저 닉네임 superuser은/는 이미 존재합니다.'
            }  
        )