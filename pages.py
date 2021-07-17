import builtins
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player


class MyPage(Page):
    pass

class Introduccion(Page):
    pass

class Instrucciones_verbal(Page):
    pass

class Prueba_verbal(Page):
    timer_text = 'Tiempo que le falta para completar la ronda: '
    timeout_seconds = Constants.task_time_v_p

#class Prueba_conteo(Page):
#    timer_text = 'Tiempo que le falta para completar la ronda: '
#    timeout_seconds = Constants.task_time_c_p

class Tarea_verbal(Page):
    if Player.treatment=='C' or Player.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_v_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds=Constants.task_time_v_t

    #def before_next_page(self):
    #   self.player.payoff = c(self.player.solved_tasks)


class Ranking_verbal(Page):
    pass

class Encuesta_final(Page):
    form_model='player'
    form_fields=['num_ID','gender','age','career','ciclo','escala','exp',
    'q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
    'q11','q12','q13','q14','q15','q16','q17','q18','q19','q20',]

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass

#class count(Page):
#    pass

page_sequence = [
    #MyPage,
    Introduccion,
    Instrucciones_verbal,
    #Prueba_verbal.
    #Tarea_verbal,
    #Ranking_verbal,
    #Encuesta_final,
    #ResultsWaitPage, 
    #Results,
]
