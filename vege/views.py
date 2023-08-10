from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def recipes(request):
    if request.method == "POST":

        data =request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image=request.FILES.get("recipe_image")

        print(recipe_name)
        print(recipe_description)
        print(recipe_image)

        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_description=recipe_description,
            recipe_name=recipe_name
        )
        return redirect('recipes')
    
    queryset=Recipe.objects.all()
    context={'recipes':queryset}

    return render(request,"recipes.html",context)

def delete_recipe(request,id):
    queryset=Recipe.objects.all().get(id=id)
    queryset.delete()
    return redirect('recipes')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        queryset.recipe_description = recipe_description
        queryset.recipe_name = recipe_name
        
        if recipe_image:  
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('recipes')

    context = {"recipes": queryset}
    return render(request, "update_recipe.html", context)
