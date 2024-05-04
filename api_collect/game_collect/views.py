# from django.shortcuts import render
# import requests

# def index(request):
#     if request.method == 'POST':
#         reg_no = request.POST.get("Reg_No")
#         dob = request.POST.get("DOB")
#         api_url = f'http://127.0.0.1:8000/marks/{reg_no}/{dob}'  # Replace with your API endpoint URL
#         response = requests.get(api_url)
#         student_data = response.json()
#         if response.status_code == 200:
#             student_data = response.json()
#             return render(request, 'results.html', {'student_data': student_data})
#         else:
#             return render(request, 'index.html', {'message': 'Failed to fetch student results. Check Again!'})
    
        
#     return render(request, 'index.html')


#__________________________________ change 1

# from django.shortcuts import render
# import requests

# def index(request):
#     if request.method == 'POST':
#         title = request.POST.get("title")
#         api_url = f'http://127.0.0.1:8000/videogame/{title}/'  # Updated API endpoint URL
#         response = requests.get(api_url)
#         videogame_data = response.json()
#         if response.status_code == 200:
#             return render(request, 'videogame_details.html', {'videogame_data': videogame_data})
#         else:
#             return render(request, 'index.html', {'message': 'Failed to fetch video game details. Check Again!'})
    
#     return render(request, 'index.html')

#______________________________ change 2

# from django.shortcuts import render
# import requests

# def index(request):
#     if request.method == 'POST':
#         title = request.POST.get("title")
#         api_url = f'http://127.0.0.1:8000/videogame/{id}/'  # Updated API endpoint URL
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             videogame_data = response.json()
#             return render(request, 'videogame_details.html', {'videogame_data': videogame_data})
#         else:
#             return render(request, 'index.html', {'message': 'Failed to fetch video game details. Check Again!'})
    
#     return render(request, 'index.html')

#_____________________________________________ change 3

from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        api_url = f'http://127.0.0.1:8000/videogame/{title}'  

        response = requests.get(api_url)
        videogame_data = response.json()
        if response.status_code == 200:
            videogame_data = response.json()
            return render(request, 'videogame_details.html', {'videogame_data': videogame_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch video game details. Check Again!'})
    
    return render(request, 'index.html')

