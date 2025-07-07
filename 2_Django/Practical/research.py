def device_view(request):
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    if "Mobile" in user_agent:
        message = "You're on a mobile device"
    else:
        message = "You're on desktop"
    return HttpResponse(message)
