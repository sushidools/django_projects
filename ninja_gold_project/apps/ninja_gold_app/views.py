from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
import random
def index(request):
    if "myGold" not in request.session or "activity" not in request.session:
        request.session["myGold"] = 0
        request.session["activity"] = []
    elif "myGold" in request.session:
        pass
    return render(request,'ninja_gold_app/index.html')

def process_gold(request):
    date = strftime("%Y-%m-%d %H:%M %p", gmtime())
    #print(date)
    temp_list = request.session['activity']
    if request.POST['building'] == 'farm':
        gold = random.randint(10,20)
        request.session['myGold'] = int(request.session['myGold']) + gold
        temp_list.append("You found " + str(gold) + ". (" + date + ")")
    elif request.POST['building'] == 'cave':
        gold = random.randint(5,11)
        request.session['myGold'] = int(request.session['myGold']) + gold
        temp_list.append("You found " + str(gold) + ". (" + date + ")")
    elif request.POST['building'] == 'house':
        gold = random.randint(2, 6)
        request.session['myGold'] = int(request.session['myGold']) + gold
        temp_list.append("You found " + str(gold) + ". (" + date + ")")
    elif request.POST['building'] == 'casino':
        gold = random.randint(-50, 51)
        request.session['myGold'] = int(request.session['myGold']) + gold
        if gold < 0 :
            temp_list.append("You have lost " + str(gold) + "! (" + date + ")")
        else:
            temp_list.append("You got lucky and won " + str(gold) + ". (" + date + ")")
    return redirect("/")
    
def reset(request):
    del request.session['myGold']
    del request.session['activity']
    return redirect("/")