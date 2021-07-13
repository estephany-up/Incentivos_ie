from otree.api import Currency as c, currency_range
from otree.db.models import StringField
from ._builtin import Page, WaitPage
from .models import Constants, Player

import random

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
    if Player.treatment=='C' or Player.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_v_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds=Constants.task_time_v_t

    #def before_next_page(self):
    #   self.player.payoff = c(self.player.solved_tasks)

class Tarea_conteo(Page):
    if Player.treatment=='C' or Player.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_c_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds=Constants.task_time_c_t
    
    form_model='player'
    form_fields=['rpta_c']
    
    def vars_for_template(self):
#        lst = [1,2,3,4,5,6,7,8,9,10]
#        for i in range (1,10):
        a_1 = str(random.choice([0,1]))
        a_2 = str(random.choice([0,1]))
        a_3 = str(random.choice([0,1]))
        a_4 = str(random.choice([0,1]))
        a_5 = str(random.choice([0,1]))
        a_6 = str(random.choice([0,1]))
        a_7 = str(random.choice([0,1]))
        a_8 = str(random.choice([0,1]))
        a_9 = str(random.choice([0,1]))
        a_10 = str(random.choice([0,1]))
        a_11 = str(random.choice([0,1]))
        a_12 = str(random.choice([0,1]))
        a_13 = str(random.choice([0,1]))
        a_14 = str(random.choice([0,1]))
        a_15 = str(random.choice([0,1]))
        a_16 = str(random.choice([0,1]))
        a_17 = str(random.choice([0,1]))
        a_18 = str(random.choice([0,1]))
        a_19 = str(random.choice([0,1]))
        a_20 = str(random.choice([0,1]))
        a_21 = str(random.choice([0,1]))
        a_22 = str(random.choice([0,1]))
        a_23 = str(random.choice([0,1]))
        a_24 = str(random.choice([0,1]))
        a_25 = str(random.choice([0,1]))
        a_26 = str(random.choice([0,1]))
        a_27 = str(random.choice([0,1]))
        a_28 = str(random.choice([0,1]))
        a_29 = str(random.choice([0,1]))
        a_30 = str(random.choice([0,1]))
        a_31 = str(random.choice([0,1]))
        a_32 = str(random.choice([0,1]))
        a_33 = str(random.choice([0,1]))
        a_34 = str(random.choice([0,1]))
        a_35 = str(random.choice([0,1]))
        a_36 = str(random.choice([0,1]))
        a_37 = str(random.choice([0,1]))
        a_38 = str(random.choice([0,1]))
        a_39 = str(random.choice([0,1]))
        a_40 = str(random.choice([0,1]))
        a_41 = str(random.choice([0,1]))
        a_42 = str(random.choice([0,1]))
        a_43 = str(random.choice([0,1]))
        a_44 = str(random.choice([0,1]))
        a_45 = str(random.choice([0,1]))
        a_46 = str(random.choice([0,1]))
        a_47 = str(random.choice([0,1]))
        a_48 = str(random.choice([0,1]))
        a_49 = str(random.choice([0,1]))
        a_50 = str(random.choice([0,1]))
        a_51 = str(random.choice([0,1]))
        a_52 = str(random.choice([0,1]))
        a_53 = str(random.choice([0,1]))
        a_54 = str(random.choice([0,1]))
        a_55 = str(random.choice([0,1]))
        a_56 = str(random.choice([0,1]))
        a_57 = str(random.choice([0,1]))
        a_58 = str(random.choice([0,1]))
        a_59 = str(random.choice([0,1]))
        a_60 = str(random.choice([0,1]))
        a_61 = str(random.choice([0,1]))
        a_62 = str(random.choice([0,1]))
        a_63 = str(random.choice([0,1]))
        a_64 = str(random.choice([0,1]))
        a_65 = str(random.choice([0,1]))
        a_66 = str(random.choice([0,1]))
        a_67 = str(random.choice([0,1]))
        a_68 = str(random.choice([0,1]))
        a_69 = str(random.choice([0,1]))
        a_70 = str(random.choice([0,1]))
        a_71 = str(random.choice([0,1]))
        a_72 = str(random.choice([0,1]))
        a_73 = str(random.choice([0,1]))
        a_74 = str(random.choice([0,1]))
        a_75 = str(random.choice([0,1]))
        a_76 = str(random.choice([0,1]))
        a_77 = str(random.choice([0,1]))
        a_78 = str(random.choice([0,1]))
        a_79 = str(random.choice([0,1]))
        a_80 = str(random.choice([0,1]))
        a_81 = str(random.choice([0,1]))
        a_82 = str(random.choice([0,1]))
        a_83 = str(random.choice([0,1]))
        a_84 = str(random.choice([0,1]))
        a_85 = str(random.choice([0,1]))
        a_86 = str(random.choice([0,1]))
        a_87 = str(random.choice([0,1]))
        a_88 = str(random.choice([0,1]))
        a_89 = str(random.choice([0,1]))
        a_90 = str(random.choice([0,1]))
        a_91 = str(random.choice([0,1]))
        a_92 = str(random.choice([0,1]))
        a_93 = str(random.choice([0,1]))
        a_94 = str(random.choice([0,1]))
        a_95 = str(random.choice([0,1]))
        a_96 = str(random.choice([0,1]))
        a_97 = str(random.choice([0,1]))
        a_98 = str(random.choice([0,1]))
        a_99 = str(random.choice([0,1]))
        a_100 = str(random.choice([0,1]))

        return dict (
            a_1=a_1, a_2=a_2, a_3=a_3, a_4=a_4, a_5=a_5, a_6=a_6, a_7=a_7, a_8=a_8, a_9=a_9, a_10=a_10,
            a_11=a_11, a_12=a_12, a_13=a_13, a_14=a_14, a_15=a_15, a_16=a_16, a_17=a_17, a_18=a_18, a_19=a_19, a_20=a_20,
            a_21=a_21, a_22=a_22, a_23=a_23, a_24=a_24, a_25=a_25, a_26=a_26, a_27=a_27, a_28=a_28, a_29=a_29, a_30=a_30,
            a_31=a_31, a_32=a_32, a_33=a_33, a_34=a_34, a_35=a_35, a_36=a_36, a_37=a_37, a_38=a_38, a_39=a_39, a_40=a_40,
            a_41=a_41, a_42=a_42, a_43=a_43, a_44=a_44, a_45=a_45, a_46=a_46, a_47=a_47, a_48=a_48, a_49=a_49, a_50=a_50,
            a_51=a_51, a_52=a_52, a_53=a_53, a_54=a_54, a_55=a_55, a_56=a_56, a_57=a_57, a_58=a_58, a_59=a_59, a_60=a_60,
            a_61=a_61, a_62=a_62, a_63=a_63, a_64=a_64, a_65=a_65, a_66=a_66, a_67=a_67, a_68=a_68, a_69=a_69, a_70=a_70,
            a_71=a_71, a_72=a_72, a_73=a_73, a_74=a_74, a_75=a_75, a_76=a_76, a_77=a_77, a_78=a_78, a_79=a_79, a_80=a_80,
            a_81=a_81, a_82=a_82, a_83=a_83, a_84=a_84, a_85=a_85, a_86=a_86, a_87=a_87, a_88=a_88, a_89=a_89, a_90=a_90,
            a_91=a_91, a_92=a_92, a_93=a_93, a_94=a_94, a_95=a_95, a_96=a_96, a_97=a_97, a_98=a_98, a_99=a_99, a_100=a_100,
            )
    
    #def before_next_page(self):
    #   self.player.payoff = c(self.player.solved_tasks)

class Ranking_verbal(Page):
    pass

class Ranking_conteo(Page):
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

class count(Page):
    pass

page_sequence = [
    #MyPage,
    #Introduccion,
    #Instrucciones_verbal,
    #Prueba_verbal.
    #Tarea_verbal,
    #Ranking_verbal,
    #Intrucciones_conteo,
    #Prueba_conteo
    Tarea_conteo, 
    #Ranking_conteo,
    Encuesta_final,
    #ResultsWaitPage, 
    #Results,
]
