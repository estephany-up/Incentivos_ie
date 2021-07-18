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

from otree.models import player

author = 'Estephany y Yadira'

doc = """
Experimento de incentivos (Hasta tarea verbal)
"""

class Constants(BaseConstants):
    name_in_url = 'exp_incentivos'
    players_per_group = 4
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
            for g in self.get_groups():
                p1=g.get_player_by_id(1)
                p1.participant.vars['group_treatment']=random.choice(['C', 'T1', 'T2', 'T3'])
                Group.treatment=p1.participant.vars['group_treatment']
                #Group.treatment = random.choice(['C', 'T1', 'T2', 'T3'])
                print('Treatment:', p1.participant.vars['group_treatment'])

    
class Group(BaseGroup):
    treatment=models.StringField


class Player(BasePlayer):  
    pass

 