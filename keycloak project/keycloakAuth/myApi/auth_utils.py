

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

def token_authentication_middleware(get_response):
    def auth_middleware(request):
        auth = TokenAuthentication()
        try:
            token = request.headers.get('Authorization')

            if token:
                token_parts = token.split()
                if len(token_parts) == 2 and token_parts[0].lower() == 'bearer':
                    access_token = token_parts[1]
                    user, _ = auth.authenticate_credentials(access_token)  # Token not used here

                    if user is not None:
                        request.user = user
                        return get_response(request)
                    else:
                        return JsonResponse({'error': 'Invalid token'}, status=401)
                else:
                    return JsonResponse({'error': 'Invalid authorization header format'}, status=401)
            else:
                return JsonResponse({'error': 'Authorization header not provided'}, status=401)
        except exceptions.AuthenticationFailed as e:
            return JsonResponse({'error': str(e)}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return auth_middleware

def api_view_wrapper(view_func):
    def wrapped_view(request, *args, **kwargs):
        permission = IsAuthenticated()
        if not permission.has_permission(request, view_func):
            return JsonResponse({'error': 'Permission Denied'}, status=403)
        
        return view_func(request, *args, **kwargs)
    return wrapped_view













# # from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
# from rest_framework import exceptions
# from rest_framework.permissions import IsAuthenticated
# from django.http import JsonResponse

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





#  try:
#             token = request.headers.get('Authorization')

#             if token:
#                 token_parts = token.split()
#                 if len(token_parts) == 2 and token_parts[0].lower() == 'bearer':
#                     access_token = token_parts[1]
#                     user, _ = auth.authenticate_credentials(access_token)  # Token not used here

#                     if user is not None:
#                         request.user = user
#                         return get_response(request)
#                     else:
#                         return JsonResponse({'error': 'Invalid token'}, status=401)
#                 else:
#                     return JsonResponse({'error': 'Invalid authorization header format'}, status=401)
#             else:
#                 return JsonResponse({'error': 'Authorization header not provided'}, status=401)
#         except exceptions.AuthenticationFailed as e:
#             return JsonResponse({'error': str(e)}, status=401)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     return auth_middleware

# def api_view_wrapper(view_func):
#     def wrapped_view(request, *args, **kwargs):
#         permission = IsAuthenticated()
#         if not permission.has_permission(request, view_func):
#             return JsonResponse({'error': 'Permission Denied'}, status=403)
        
#         return view_func(request, *args, **kwargs)
#     return wrapped_view
