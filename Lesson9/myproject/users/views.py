from django.shortcuts import render, redirect               #After succesfully save the user, it needs to be redirect back to the post list
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
def register_view(request):
    if request.method == "POST":                 #if the request method is post, the form has been submitted   submitting it with a post request, the post method back to this same address
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", { "form": form })