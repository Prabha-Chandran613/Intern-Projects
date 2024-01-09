# views.py

from django.http import JsonResponse
from .auth_utils import api_view_wrapper
# from django.shortcuts import redirect

# from django.contrib.auth.decorators import login_required
# def keycloak_login(request):
#     return redirect("account/social/login/keycloak/")

@api_view_wrapper
def simple_api_view(request):
    data = {
        'message': 'Hello, this is a protected API response!'
    }
    return JsonResponse(data)






























# from django.http import JsonResponse
# from .auth_utils import token_required

# @token_required
# def simple_api_view(request):
#     data = {
#         'message': 'Hello, this is a simple API response!'
#     }
#     return JsonResponse(data)

































# from django.http import JsonResponse
# # from keycloak import KeycloakOpenID

# from keycloak.keycloak_openid import KeycloakOpenID


# def simple_api_view(request):
#     keycloak_openid = KeycloakOpenID(
#         server_url='http://0.0.0.0:8080/auth',
#         client_id='keycloak_admin',
#         realm_name='keycloak_auth',
#         client_secret_key='ZbdJYNKAu198AqOdmJubQEy8KgRhbsYw',
#     )

#     try:
#         print("trial")
#         token = request.headers['Authorization']
#         print(token,"test")
#         if token:
#             abc = token.split()

#             token_info = keycloak_openid.introspect(abc[1])
#             print(token_info)
#             # Check token_info to validate the token and get user information
#             data = {
#                 'message': 'Hello, this is a simple API response!'
#             }
#             return JsonResponse(data)
#         else:
#             return JsonResponse({'error': 'Unauthorized'}, status=401)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)






# # views.py

# from django.http import JsonResponse
# from keycloak import KeycloakOpenID

# # Assuming you have the keycloak.json file in your project directory

# def simple_api_view(request):
#     keycloak_openid = KeycloakOpenID(keycloak_json_path='keycloakAuth/keycloak.json')

#     try:
#         token = request.COOKIES.get('access_token')
#         if token:
#             token_info = keycloak_openid.introspect(token)
#             # Check token_info to validate the token and get user information
#             data = {
#                 'message': 'Hello, this is a simple API response!'
#             }
#             return JsonResponse(data)
#         else:
#             return JsonResponse({'error': 'Unauthorized'}, status=401)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)










# # from django.shortcuts import render

# # Create your views here.
# from django.http import JsonResponse

# def simple_api_view(request):
#     data = {
#         'message': 'Hello, this is a simple API response!'
#     }
#     return JsonResponse(data)