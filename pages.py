from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass

class Introduccion(Page):
    pass

class Instrucciones_verbal(Page):
    pass

class Intrucciones_conteo(Page):
    pass

class Prueba_verbal(Page):
    timer_text = 'Tiempo que le falta para completar la ronda: '
    timeout_seconds = Constants.task_time_v_p

class Prueba_conteo(Page):
    timer_text = 'Tiempo que le falta para completar la ronda: '
    timeout_seconds = Constants.task_time_c_p

class Tarea_verbal(Page):
    timer_text = 'Tiempo que le falta para completar la ronda: '
    #usar if para poner el tiempo dependiendo del grupo de tratamiento o control
    # timeout_seconds = Constants.task_time_v_s

    #def before_next_page(self):
    #   self.player.payoff = c(self.player.solved_tasks)

class Tarea_conteo(Page):
    timer_text = 'Tiempo que le falta para completar la ronda: '
    #timeout_seconds = Constants.task_time_c_s
    #def before_next_page(self):
    #   self.player.payoff = c(self.player.solved_tasks)

class Ranking_verbal(Page):
    pass

class Ranking_conteo(Page):
    pass

class Encuesta_final(Page):
    form_model='player'
    form_fields=['gender','age','career','ciclo','escala','exp']

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass


page_sequence = [
    MyPage,
    Introduccion,
    Instrucciones_verbal,
    Tarea_verbal,
    Ranking_verbal,
    Intrucciones_conteo,
    Tarea_conteo, 
    Ranking_conteo,
    Encuesta_final,
    ResultsWaitPage, 
    Results]
