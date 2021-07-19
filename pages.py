import builtins
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Group, Player,Subsession


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
    if Group.treatment=='C' or Group.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_v_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds=Constants.task_time_v_t            

    form_model='player'
    form_fields=['answer_1','answer_2','answer_3','answer_4','answer_5']


class Ranking_verbal(Page):
    pass


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
    Tarea_verbal,
    #Ranking_verbal,
    #ResultsWaitPage, 
    #Results,
]
