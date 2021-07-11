from django.db.models.base import Model
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
from . import ret_fun
from django.db.models import F

author = 'Estephany y Yadira'

doc = """
Tareas de conteo y verbal - 4 rondas cada una
"""

class Constants(BaseConstants):
    name_in_url = 'incentivos'
    players_per_group = None
    num_rounds = 1
    task_time_v_p=60  #prueba verbal
    task_time_v_s=180 #verbal sin presión
    task_time_v_t=120 #verbal con presión
    task_time_c_p=60  #prueba conteo
    task_time_c_s=300 #conteo sin presión
    task_time_c_t=180 #conteo con presión

class Subsession(BaseSubsession):
    ##por ahora sólo se ha asignado tratamiento por participante
    ##cambiar más adelante a grupos
    def creating_session(self):
     #randomize to treatments
        for player in self.get_players():
            player.treatment = random.choice(['C', 'T1', 'T2', 'T3'])
            print('Treatment:', player.treatment)
    
    # we look for a corresponding Task Generator in our library (ret_functions.py) that contain all task-generating
    # functions. So the name of the generator in 'task_fun' parameter from settings.py should coincide with an
    # actual task-generating class from ret_functions.
        self.session.vars['task_fun'] = getattr(ret_fun, self.session.config['task'])
    # If a task generator gets some parameters (like a level of difficulty, or number of rows in a matrix etc.)
    # these parameters should be set in 'task_params' settings of an app, in a form of dictionary. For instance:
    # 'task_params': {'difficulty': 5}
        self.session.vars['task_params'] = self.session.config.get('task_params', {})
    # for each player we call a function (defined in Player's model) called get_or_create_task
    # this is done so that when a RET page is shown to a player for the first time they would already have a task
    # to work on

class Group(BaseGroup):
    pass

def make_field(label):
    return models.IntegerField(
        choices=[[1,''],[2,''],[3,''],[4,'']],
        label=label,
        widget=widgets.RadioSelect,
    )

class Player(BasePlayer):
    num_ID = models.StringField(label='1. ¿Cuál es tu número ID')
    age = models.IntegerField(label='3. ¿Cuál es tu edad?', min=13, max=40)
    gender = models.StringField(
        choices=[[0, 'Masculino'], [1, 'Femenino']],
        label='2. ¿Cuál es tu género?',
        widget=widgets.RadioSelect,
    )
    career = models.StringField(
        choices=[['Derecho', 'Derecho'], ['Finanzas', 'Finanzas'],['Marketing','Marketing'],
        ['Economía','Economía'],['Contabilidad','Contabilidad'],['Administración','Administración'],
        ['Ingeniería informática','Ingeniería informática'],['Ingeniería empresarial','Ingeniería empresarial'],
        ['Negocios internacionales','Negocios internacionales']],
        label='4. ¿Cuál es la carrera que estudias? Seleccione su carrera',
        widget=widgets.RadioSelect,
    )
    ciclo = models.IntegerField(label='5. ¿Qué ciclo estás cursando actualmente? (Ej:5to)')
    escala = models.StringField(label='6. ¿En qué escala de pensión te encuentras?')
    exp = models.StringField(
        choices=[[0,'No'],[1,'Sí, una vez'],[2,'Sí, más de una vez']],
        label='7. ¿Has participado en un experimento anteriormente?',
    )
    ##enunciados de competencia
    q1 = make_field('Me gusta competir')
    q2 = make_field('Me gusta competir individualmente')
    q3 = make_field('Disfruto competir contra un oponente')
    q4 = make_field('No me gusta competir contra otras personas')
    q5 = make_field('Competir contra otros me da satisfacción')
    q6 = make_field('La situaciones de competencia me parecen incómodas')
    q7 = make_field('Temo competir contra otras personas')
    q8 = make_field('Intento evitar competir contra otras personas')
    q9 = make_field('Trato de superar a los demás a menudo')
    q10 = make_field('No me gustan los juegos en los que el ganador se lleva todo el premio')
    q11 = make_field('La competencia destruye la amistad')
    q12 = make_field('Los juegos sin un solo ganador son aburridos')
    q13 = make_field('Usualmente no es importante para mí ser el mejor')
    q14 = make_field('Cuando juego, me gusta llevar el conteo de la puntuación')
    ##enunciados de incentivos para todos
    q15 = make_field('Le doy importancia a los incentivos monetarios')
    q16 = make_field('Los incentivos monetarios no tienen ningún valor para mí')
    q17 = make_field('Los incentivos monetarios tienen efectos positivos en mi performance')
    q18 = make_field('Un incentivo monetario atractivo aumentará mi motivación para trabajar más duro')
    ##enunciados adicionales para tratameinto 1 y 3
    q19 = make_field('Los incentivos monetarios ofrecidos coinciden con mi esfuerzo en las tareas realizadas')
    q20 = make_field('El incentivo monetario ofrecido no está a la altura de mis expectativas')
    

    treatment = models.StringField()

    # this method returns number of correct tasks solved in this round
    @property
    def num_tasks_correct(self):
        return self.tasks.filter(correct_answer=F('answer')).count()

    # this method returns total number of tasks to which a player provided an answer
    @property
    def num_tasks_total(self):
        return self.tasks.filter(answer__isnull=False).count()

    solved_tasks = num_tasks_correct