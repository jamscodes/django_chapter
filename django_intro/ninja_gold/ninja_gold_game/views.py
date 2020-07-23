from django.shortcuts import render, HttpResponse, redirect
from ninja_gold_game.game_logic.logic_files import calculate_money, log_events, start_game, check_endgame

# Create your views here.

def index(request):
    if 'game_start' not in request.session:
        request.session['start_params'] = {}
        request.session['golds'] = 0
        request.session['round_num'] = 0
        request.session['logs'] = []
        request.session['game_start'] = False
        request.session['game_won'] = False
    return render(request, 'ninja_gold_game.html')

def process_money(request):
    golds_earned = calculate_money(request.GET['location'])
    request.session['golds'] += golds_earned[0]
    request.session['logs'].insert(0, golds_earned[1][0])
    request.session['round_num'] += 1
    
    if check_endgame(request, request.session['golds'], request.session['round_num']):
        return redirect('/end_screen/')
    else:
        return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')

def end_screen(request):
    return render(request, 'end_screen.html')