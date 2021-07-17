from typing import List
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

author = 'Estephany y Yadira'

doc = """
Experimento de incentivos (Hasta tarea verbal)
"""

class Constants(BaseConstants):
    name_in_url = 'exp_incentivos'
    players_per_group = None
    num_rounds = 1
    task_time_v_p=60  #prueba verbal
    task_time_v_s=180 #verbal sin presión
    task_time_v_t=120 #verbal con presión

class Subsession(BaseSubsession):
    ##por ahora sólo se ha asignado tratamiento por participante
    ##cambiar más adelante a grupos
    def creating_session(self):
     #randomize to treatments
        if self.round_number==1:
            for player in self.get_players():
                player.treatment = random.choice(['C', 'T1', 'T2', 'T3'])
                print('Treatment:', player.treatment)

    
class Group(BaseGroup):
    pass


class Player(BasePlayer):  
    treatment = models.StringField()

 