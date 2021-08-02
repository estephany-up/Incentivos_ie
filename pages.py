from otree.models import player
#from incentivos.models import Subsession
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player, Group, Subsession
import time, random


#class MyPage(Page):
#    pass

class Reglas_generales(Page):
    pass

class Introduccion(Page):
    def is_displayed(self):
        p1 = self.group.get_player_by_id(1)
        Group.treatment = p1.participant.vars['treatment']
        return self.round_number == 1
    def vars_for_template(self):
        code=self.player.id_code()       
        return dict(a=code)

class Instrucciones_verbal(Page):
    def before_next_page(self):
        self.session.vars['expiry'] = time.time() + Constants.task_time_v_p

class Prueba_verbal(Page):
    timer_text = 'Tiempo que le falta para completar la ronda: '
    timeout_seconds = Constants.task_time_v_p

    form_model='player'
    form_fields=['answer_1_p','answer_2_p','answer_3_p','answer_4_p','answer_5_p','answer_6_p','answer_7_p',
    'answer_8_p','answer_9_p','answer_10_p','answer_11_p','answer_12_p','answer_13_p','answer_14_p','answer_15_p',
    'answer_16_p','answer_17_p','answer_18_p','answer_19_p','answer_20_p','answer_21_p','answer_22_p','answer_23_p',
    'answer_24_p','answer_25_p']
    
    def before_next_page(self):
        self.player.puntaje_p()

class Wait_p(WaitPage):
    after_all_players_arrive='wp_p'

class Ranking_verbal_p(Page):
    def vars_for_template(self):
        pt_p, p_p = self.group.rank_p()
        p_p1=p_p[0]
        p_p2=p_p[1]
        p_p3=p_p[2]
        p_p4=p_p[3]
        pt_p1=pt_p[0]
        pt_p2=pt_p[1]
        pt_p3=pt_p[2]
        pt_p4=pt_p[3]
        return dict(p_p1=p_p1, p_p2=p_p2, p_p3=p_p3, p_p4=p_p4,
        pt_p1=pt_p1, pt_p2=pt_p2, pt_p3=pt_p3, pt_p4=pt_p4)

    def before_next_page(self):
        #p1 = self.group.get_player_by_id(1)
        #treatment = p1.participant.vars['treatment']
        if Group.treatment=='C' or Group.treatment=='T1':
            self.session.vars['expiry'] = time.time() + Constants.task_time_v_s
        else:
            self.session.vars['expiry'] = time.time() + Constants.task_time_v_t

class Tarea_verbal_R1(Page):   
    if Group.treatment=='C' or Group.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_v_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds=Constants.task_time_v_t            

    form_model='player'
    form_fields=['answer_1_R1','answer_2_R1','answer_3_R1','answer_4_R1','answer_5_R1','answer_6_R1','answer_7_R1',
    'answer_8_R1','answer_9_R1','answer_10_R1','answer_11_R1','answer_12_R1','answer_13_R1','answer_14_R1','answer_15_R1',
    'answer_16_R1','answer_17_R1','answer_18_R1','answer_19_R1','answer_20_R1','answer_21_R1','answer_22_R1','answer_23_R1',
    'answer_24_R1','answer_25_R1']

    def vars_for_template(self): 
        a=self.group.pato_1()
        return dict (a=a) 

    def before_next_page(self):
        self.player.puntaje_R1()


class Wait_1(WaitPage):
    after_all_players_arrive='wp_1'

class Ranking_verbal_R1(Page):
    def vars_for_template(self):
        pt_p, p_p = self.group.rank_R1()
        p_p1=p_p[0]
        p_p2=p_p[1]
        p_p3=p_p[2]
        p_p4=p_p[3]
        pt_p1=pt_p[0]
        pt_p2=pt_p[1]
        pt_p3=pt_p[2]
        pt_p4=pt_p[3]
        return dict(p_p1=p_p1, p_p2=p_p2, p_p3=p_p3, p_p4=p_p4,
        pt_p1=pt_p1, pt_p2=pt_p2, pt_p3=pt_p3, pt_p4=pt_p4)
    
    def before_next_page(self):
        #p1 = self.group.get_player_by_id(1)
        #treatment = p1.participant.vars['treatment']
        if Group.treatment=='C' or Group.treatment=='T1':
            self.session.vars['expiry'] = time.time() + Constants.task_time_v_s
        else:
            self.session.vars['expiry'] = time.time() + Constants.task_time_v_t

class pay_1(WaitPage):
    after_all_players_arrive='pp_1'

class Tarea_verbal_R2(Page):   
    if Group.treatment=='C' or Group.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_v_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds=Constants.task_time_v_t            

    form_model='player'
    form_fields=['answer_1_R2','answer_2_R2','answer_3_R2','answer_4_R2','answer_5_R2','answer_6_R2','answer_7_R2',
    'answer_8_R2','answer_9_R2','answer_10_R2','answer_11_R2','answer_12_R2','answer_13_R2','answer_14_R2','answer_15_R2',
    'answer_16_R2','answer_17_R2','answer_18_R2','answer_19_R2','answer_20_R2','answer_21_R2','answer_22_R2','answer_23_R2',
    'answer_24_R2','answer_25_R2']

    def vars_for_template(self): 
        a=self.group.pato_2()
        return dict (a=a) 

    def before_next_page(self):
        self.player.puntaje_R2()

class Wait_2(WaitPage):
    after_all_players_arrive='wp_2'

class Ranking_verbal_R2(Page):
    def vars_for_template(self):
        pt_p, p_p = self.group.rank_R2()
        p_p1=p_p[0]
        p_p2=p_p[1]
        p_p3=p_p[2]
        p_p4=p_p[3]
        pt_p1=pt_p[0]
        pt_p2=pt_p[1]
        pt_p3=pt_p[2]
        pt_p4=pt_p[3]
        return dict(p_p1=p_p1, p_p2=p_p2, p_p3=p_p3, p_p4=p_p4,
        pt_p1=pt_p1, pt_p2=pt_p2, pt_p3=pt_p3, pt_p4=pt_p4)
    
    def before_next_page(self):
        p1 = self.group.get_player_by_id(1)
        treatment = p1.participant.vars['treatment']
        if treatment=='C' or treatment=='T1':
            self.session.vars['expiry'] = time.time() + Constants.task_time_v_s
        else:
            self.session.vars['expiry'] = time.time() + Constants.task_time_v_t

class pay_2(WaitPage):
    after_all_players_arrive='pp_2'

class Tarea_verbal_R3(Page):   
    if Group.treatment=='C' or Group.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_v_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds=Constants.task_time_v_t            

    form_model='player'
    form_fields=['answer_1_R3','answer_2_R3','answer_3_R3','answer_4_R3','answer_5_R3','answer_6_R3','answer_7_R3',
    'answer_8_R3','answer_9_R3','answer_10_R3','answer_11_R3','answer_12_R3','answer_13_R3','answer_14_R3','answer_15_R3',
    'answer_16_R3','answer_17_R3','answer_18_R3','answer_19_R3','answer_20_R3','answer_21_R3','answer_22_R3','answer_23_R3',
    'answer_24_R3','answer_25_R3']

    def vars_for_template(self): 
        a=self.group.pato_3()
        return dict (a=a) 

    def before_next_page(self):
        self.player.puntaje_R3() 

class Wait_3(WaitPage):
    after_all_players_arrive='wp_3'

class Ranking_verbal_R3(Page):
    def vars_for_template(self):
        pt_p, p_p = self.group.rank_R3()
        p_p1=p_p[0]
        p_p2=p_p[1]
        p_p3=p_p[2]
        p_p4=p_p[3]
        pt_p1=pt_p[0]
        pt_p2=pt_p[1]
        pt_p3=pt_p[2]
        pt_p4=pt_p[3]
        return dict(p_p1=p_p1, p_p2=p_p2, p_p3=p_p3, p_p4=p_p4,
        pt_p1=pt_p1, pt_p2=pt_p2, pt_p3=pt_p3, pt_p4=pt_p4)
    
    def before_next_page(self):
        p1 = self.group.get_player_by_id(1)
        treatment = p1.participant.vars['treatment']
        if treatment=='C' or treatment=='T1':
            self.session.vars['expiry'] = time.time() + Constants.task_time_v_s
        else:
            self.session.vars['expiry'] = time.time() + Constants.task_time_v_t

class pay_3(WaitPage):
    after_all_players_arrive='pp_3'

class Tarea_verbal_R4(Page):   
    if Group.treatment=='C' or Group.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_v_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds=Constants.task_time_v_t            

    form_model='player'
    form_fields=['answer_1_R4','answer_2_R4','answer_3_R4','answer_4_R4','answer_5_R4','answer_6_R4','answer_7_R4',
    'answer_8_R4','answer_9_R4','answer_10_R4','answer_11_R4','answer_12_R4','answer_13_R4','answer_14_R4','answer_15_R4',
    'answer_16_R4','answer_17_R4','answer_18_R4','answer_19_R4','answer_20_R4','answer_21_R4','answer_22_R4','answer_23_R4',
    'answer_24_R4','answer_25_R4']

    def vars_for_template(self): 
        a=self.group.pato_4()
        return dict (a=a) 

    def before_next_page(self):
        self.player.puntaje_R4()

class Wait_4(WaitPage):
    after_all_players_arrive='wp_4'

class Ranking_verbal_R4(Page):
    def vars_for_template(self):
        pt_p, p_p = self.group.rank_R4()
        p_p1=p_p[0]
        p_p2=p_p[1]
        p_p3=p_p[2]
        p_p4=p_p[3]
        pt_p1=pt_p[0]
        pt_p2=pt_p[1]
        pt_p3=pt_p[2]
        pt_p4=pt_p[3]
        return dict(p_p1=p_p1, p_p2=p_p2, p_p3=p_p3, p_p4=p_p4,
        pt_p1=pt_p1, pt_p2=pt_p2, pt_p3=pt_p3, pt_p4=pt_p4)

class pay_4(WaitPage):
    after_all_players_arrive='pp_4'
    
class Cambio_app(Page):
    def before_next_page(self):
        a=self.player.pay_1
        b=self.player.pay_2
        c=self.player.pay_3
        d=self.player.pay_4
        self.player.payoff=a+b+c+d
        return self.player.payoff


page_sequence = [
    #MyPage,
    Reglas_generales,
    Introduccion,
    Instrucciones_verbal,
    Prueba_verbal,
    Wait_p,
    Ranking_verbal_p,
    Tarea_verbal_R1,
    Wait_1,
    Ranking_verbal_R1,
    pay_1,
    #Tarea_verbal_R2,
    #Wait_2,
    #Ranking_verbal_R2,
    #pay_2,
    #Tarea_verbal_R3,
    #Wait_3,
    #Ranking_verbal_R3,
    #pay_3,
    #Tarea_verbal_R4,
    #Wait_4,
    #Ranking_verbal_R4,
    #pay_4, 
    Cambio_app,
]
