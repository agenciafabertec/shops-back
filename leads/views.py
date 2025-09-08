import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Lead

# Para ambiente local com front em outra porta, manter csrf_exempt.
# Em produção no mesmo domínio, remova o csrf_exempt e use o CSRF padrão.
@csrf_exempt
@require_POST
def submit_lead(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return JsonResponse({"ok": False, "error": "invalid_json"}, status=400)

    name  = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip().lower()
    phone = (data.get("phone") or "").strip()

    if not name or not email or not phone:
        return JsonResponse({"ok": False, "error": "missing_fields"}, status=400)

    if Lead.objects.filter(email=email).exists():
        return JsonResponse({"ok": True, "msg": "already_saved"})

    ua = request.META.get("HTTP_USER_AGENT", "")[:400]
    ip = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR", "")).split(",")[0].strip()

    Lead.objects.create(name=name, email=email, phone=phone, ua=ua, ip=ip)
    return JsonResponse({"ok": True})
