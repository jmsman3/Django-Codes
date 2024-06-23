from django.shortcuts import render

# Create your views here.
def index(request):

    data = [
  {
    "userId": 1,
    "it": 1,
    "title": "repels provide option",
    "body": "accepts consequences refusal"
  },
  {
    "userId": 1,
    "it": 2,
    "title": "being is time",
    "body": "follow life things"
  },
  {
    "userId": 1,
    "it": 3,
    "title": "she repels troubles",
    "body": "lust blinded pains"
  },
  {
    "userId": 1,
    "it": 4,
    "title": "blinded by pleasure",
    "body": "rejecting obtain pleasure"
  },
  {
    "userId": 1,
    "it": 5,
    "title": "they hate unknown",
    "body": "seek forgiveness flee"
  }
]

    return render(request , 'index.html' , {'data' : data})



def about(request):
    print(request.GET)
    return render(request , 'index.html' , {'id' : request.GET})