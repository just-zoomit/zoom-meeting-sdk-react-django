import jwt #add this
import time #add this
from django.conf import settings #add this
from django.http import JsonResponse #add this

# Add to blog
from django.views.decorators.csrf import csrf_exempt #add this review
from json import loads #add this


# Create your views here.
@csrf_exempt #add this review
def ZoomJWTToken(request):

    if request.method == 'POST':
            
      get_body_data = loads(request.body)
      mn =  get_body_data['meetingNumber']
      role = get_body_data['role']
      # The current timestamp. Required.
      iat = int(time.time())
      exp = iat + 60 * 60 * 2
      token = jwt.encode({
            "sdkKey": settings.ZOOM_API_KEY, # Optional for Web.
            "appKey": settings.ZOOM_API_KEY,  # Optional for Web.
            "mn": mn , # Required for Web, optional for Native.
            "role": role, # Required for Web, optional for Native.
            "iat": iat, #  Required.
            "exp": exp, # Required for Web, optional for Native.
            "tokenExp": iat + 60 * 60 * 2 # Required for Native, optional for Web.
            }, settings.ZOOM_API_SECRET, algorithm="HS256", headers={ 'alg': 'HS256', 'typ': 'JWT' })
      
      return JsonResponse({'signature': token}) 
  