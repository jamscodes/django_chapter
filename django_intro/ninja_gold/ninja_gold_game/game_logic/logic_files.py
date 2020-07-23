from django.shortcuts import redirect
import random

def calculate_money(loc):
    randy = random.random()
    earnings = 0

    if loc == 'farm':
        earnings = round(randy * 10 + 10)
    elif loc == 'cave':
        earnings = round(randy * 5 + 5)
    elif loc == 'house':
        earnings = round(randy * 3 + 2)
    else:
        gain_loss = round(randy * 1)
        other_randy = random.random()
        if gain_loss == 1:
            earnings = round(other_randy * 50)
        else:
            earnings = round(other_randy * 50) * -1

    return [earnings, log_events(earnings, loc)]

def log_events(amt, loc):
    log = []
    
    if amt >= 0:
        log.append(f"You earned {amt} golds from the {loc}!")
    else:
        log.append(f"You lost {amt * -1} golds from the {loc}.")

    return log

def start_game(request):
    start_params = {
        'rounds': int(request.POST['num_rounds']),
        'gold_limit': int(request.POST['gold_limit'])
    }
    request.session['game_start'] = True
    request.session['logs'].insert(0, f"You have {start_params['rounds']} rounds to earn {start_params['gold_limit']} golds.")
    request.session['start_params'] = start_params
    return redirect('/')

def check_endgame(request, gold, round):
    start_params = request.session['start_params']
    
    if gold >= start_params['gold_limit']:
        request.session['game_won'] = True
        return True
    elif round >= start_params['rounds']:
        return True