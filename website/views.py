from django.shortcuts import render
from django.http import JsonResponse
import requests
import os 
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests




def home(request):
    return render(request, "home.html")

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os

from django.conf import settings
GOOGLE_SHEET_URL = settings.GOOGLE_SHEET_URL


@csrf_exempt
def submit_form(request):
    if request.method == "POST":

        if not GOOGLE_SHEET_URL:
            return JsonResponse(
                {"error": "GOOGLE_SHEET_URL not set"},
                status=500
            )

        data = {
            "name": request.POST.get("name", ""),
            "phone": request.POST.get("phone", ""),
            "message": request.POST.get("message", ""),
            "page": "Home Page"
        }

        try:
            response = requests.post(
                GOOGLE_SHEET_URL,
                json=data,
                timeout=10
            )

            if response.status_code == 200:
                return JsonResponse({"status": "success"})

            return JsonResponse(
                {"error": "Google API failed"},
                status=500
            )

        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=500
            )

    return JsonResponse({"error": "Invalid request"}, status=405)
