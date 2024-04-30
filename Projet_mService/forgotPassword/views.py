from django.shortcuts import render

# Create your views here.
def forgotPassword(request):
    return render(request, 'forgotPassword.html')


# def reset_password_send(request):
#   # Your custom logic for handling password reset requests
#   # (e.g., sending confirmation email)
#   return render(request, 'reset_password_send.html')

