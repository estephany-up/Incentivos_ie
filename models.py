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
    Word_list_preguntas = ['EXPERIMENTO', 'ARGENTINA', 'CABALLITO', 'CASCABELES', 'HOLOCAUSTO',
     'MANDARINA', 'ELEFANTES', 'COBARDÍA', 'TELEPATÍA', 'COMUNICACIÓN']

    Word_list_ALEATORIO = ['aerolito', 'lotearía', 'aletría', 'atolero', 'atolera', 'latería', 
    'laterío', 'latiera', 'loteara', 'lotería', 'oleario', 'olearia', 'realito', 'alerta', 'alerto', 
    'aliaré', 'alotar', 'alrota', 'altear', 'altera', 'altero', 'altiro', 'areito', 'areola', 'arieta', 
    'arieto', 'arlota', 'arlote', 'ataire', 'atairo', 'atareo', 'atería', 'aterío', 'atoaré', 'élitro', 
    'eolito', 'etaria', 'etario', 'etolio', 'etolia', 'latear', 'latera', 'latero', 'latirá', 'latiré', 
    'latría', 'litará', 'litaré', 'litera', 'loaría', 'lotear', 'lotero', 'lotera', 'oleará', 'olería', 
    'oliera', 'otario', 'otaria', 'oteará', 'otilar', 'relata', 'relato', 'talare', 'talaré', 'talero', 
    'teoría', 'tirela', 'toaría', 'tolera', 'tolero', 'aireo', 'airea', 'alear', 'alero', 'aleta','aliar', 
    'alier', 'alora', 'alota', 'aloté', 'aloto', 'altar', 'alteo', 'altea', 'altor', 'aorta', 'arela','arelo', 
    'arilo', 'artal', 'ataré', 'atear', 'aterí', 'atoar', 'atole', 'atora', 'atoré', 'atoro', 'atoró', 'atrae', 
    'atril', 'atrio', 'elato', 'elata', 'eolia', 'eolio', 'erala', 'erial', 'etilo', 'etola', 'etolo', 'ilota', 
    'italo', 'itero', 'itera', 'latea', 'lateo', 'latía', 'latió', 'latir', 'letra', 'liará', 'liaré', 'litar', 
    'litre', 'litro', 'loará', 'loaré', 'lorea', 'loreo', 'loteo', 'loteo', 'olear', 'olerá', 'olote', 'orate', 
    'oriol', 'otear', 'otero', 'otila', 'otilé', 'otilo', 'raleo', 'ralea', 'rateo', 'ratea', 'ratio', 'reala', 
    'reata', 'reato', 'retal', 'riata', 'riela', 'rielo', 'rolea', 'roleo', 'rotal', 'taira', 'taire', 'talar', 
    'talea', 'talio', 'tarea', 'telar', 'tiara', 'toará', 'oaré', 'toral', 'torea', 'toreo', 'toril', 'torio', 
    'traía', 'trial', 'trile', 'trola', 'trole', 'aeta', 'aíra', 'aire', 'aíro', 'alar', 'alea', 'aleo', 'alía', 
    'alié', 'alío', 'aloe', 'alta', 'alto', 'área', 'arel', 'ario', 'aria', 'arla', 'arlé', 'arlo', 'arta', 'arte', 
    'arto', 'atal', 'atar', 'ateo', 'atea', 'atoa', 'atoé', 'atol', 'atoo', 'eirá', 'eral', 'ería', 'erío', 'íleo', 
    'iota', 'lata', 'late', 'latí', 'lato', 'leía', 'lera', 'lero', 'liar', 'lira', 'lita', 'lité', 'lito', 'loar', 
    'loor', 'loro', 'lora', 'lota', 'lote', 'loto', 'oirá', 'oiré', 'olea', 'óreo', 'oler', 'olía', 'olió', 'olor', 
    'oral', 'orea', 'óreo', 'orla', 'orlé', 'orlo', 'orto', 'otar', 'otea', 'oteo', 'otra', 'otro', 'raía', 'raíl', 
    'ralo', 'rala', 'rata', 'rato', 'real', 'reía', 'reta', 'reto', 'rial', 'riel', 'rila', 'rilé', 'rilo', 'rite', 
    'rito', 'roel', 'roía', 'rola', 'rolo', 'rolé', 'rota', 'roto', 'rote', 'roté', 'tael', 'tala', 'talé', 'talo', 
    'tara', 'tare', 'taro', 'tela', 'tila', 'tile', 'tilo', 'tira', 'tiré', 'tiro', 'toar', 'tola', 'tole', 'tora', 
    'toro', 'trae', 'treo', 'tría', 'trié', 'trío', 'trol']

    Word_list_EXPERIMENTO = ['exterminé', 'extermine', 'extermino','exterminó', 'inexperto', 'pimentero', 'rompiente', 
    'peinetero', 'exprimen', 'eximente', 'exporten', 'extirpen', 'extremen', 'emétrope', 'empeoren', 'empitone', 'empotren', 
    'epitomen', 'impetren', 'importen', 'permiten', 'prometen', 'temperen', 'temperie', 'trompeen', 'menorete', 'metieren', 
    'metieron', 'moreteen', 'temieren', 'temieron', 'exprime', 'exprimo', 'experto', 'expiren', 'exponer', 'exporte', 
    'extirpe', 'extirpo', 'extremo', 'exonere', 'externe', 'externo', 'extorne', 'empeine', 'empente', 'empento', 'empeore', 
    'emperne', 'emperno', 'empetro', 'empíreo', 'emporen', 'empoten', 'empotre', 'epímone', 'epítome', 'imperen', 'impetre', 
    'impetro', 'imponer', 'importe', 'menipeo', 'oprimen', 'optimen', 'perimen', 'permeen', 'permite', 'permito', 'premien', 
    'primeen', 'promete', 'prometí', 'tempere', 'tempero', 'trompee', 'trompen', 'emérito', 'entripe', 'entripo', 'mentiré', 
    'meriten', 'metiere', 'moretee', 'peinero', 'penetre', 'penetro', 'pereion', 'perineo', 'periten', 'pernote', 'porteen', 
    'potreen', 'prenote', 'remeneo', 'remeten', 'remetió', 'remiten', 'remonte', 'repeine', 'repeine', 'repeino', 'repente', 
    'repinte', 'repinto', 'repito', 'retomen', 'temiere', 'termine', 'termino', 'terpeno', 'timonee', 'entreoí', 'oriente', 
    'retiene', 'tironee', 'eximen', 'expíen', 'expire', 'expiro', 'expone', 'pixtón', 'exente', 'exento', 'exoren', 'exorne', 
    'empero', 'empine', 'empino', 'empore', 'empote', 'impere', 'impero', 'ímpeto', 'impone', 'oprime', 'optimé', 'perime', 
    'perimo', 'permee', 'permeo', 'premié', 'premio', 'primee', 'primen', 'primeo', 'rompe', 'tiempo', 'trompe', 'emiten', 
    'enmote', 'enorme', 'enrome', 'etíope', 'inepto', 'inerme', 'mentir', 'mentor', 'merino', 'merito', 'meteré', 'miente', 
    'miento', 'minero', 'minore', 'mitren', 'monteé', 'morete', 'moteen', 'nepote', 'omiten', 'operen', 'perene', 'pereto', 
    'periné', 'perite', 'perito', 'pernee', 'perneo', 'pernio', 'peroné', 'perote', 'pétreo', 'pinero', 'pintee', 'pinteo', 
    'pintor', 'piteen', 'pitero', 'pitreo', 'ponteé', 'porteé', 'porten', 'potreé', 'prieto', 'remete', 'remtí', 'remeto', 
    'remite', 'remito', 'repetí', 'repine', 'repino', 'repite', 'repito', 'repone', 'repten', 'retome', 'riepto', 'ritmen', 
    'temeré', 'topeen', 'tremen', 'tremió', 'trepen', 'tripón', 'enteré', 'entero', 'entore', 'etéreo', 'eterno', 'inerte', 
    'iteren', 'norteé', 'retiné', 'retino', 'tierno', 'toreen', 'torneé', 'trineo', 'epoxi', 'exime', 'eximo', 'expíe', 
    'expío', 'expón', 'mixto', 'éxit', 'exoré', 'nixte', 'oxeen', 'impón', 'miope', 'pemón', 'primé', 'primo', 'rompe', 'rompí', 
    'tiempo', 'emite', 'emito', 'étimo', 'inope', 'meneé', 'meneo', 'menor', 'mente', 'mentí', 'mento', 'meren', 'meten', 
    'meter', 'metió', 'metro', 'miren', 'mirón', 'mirto', 'mitón', 'mitré', 'mitró', 'moneé', 'monte', 'moren', 'moteé', 
    'motín', 'nemeo', 'normé', 'ominé', 'omite', 'opere', 'opine', 'opten', 'peeré', 'peine', 'peino', 'perno', 'peten', 
    'pinté', 'pinto', 'piren', 'pirón', 'piteo', 'pitón', 'poner', 'porte', 'poten', 'prion', 'remen', 'repón', 'repte', 
    'repto', 'rimen', 'ritmo', 'romín', 'temen', 'temer', 'temió', 'temor', 'termo', 'timen', 'timón', 'tomen', 'tomín', 
    'topeé', 'topen', 'torpe', 'treme', 'tremí', 'tremó', 'trepé', 'trepo', 'tripe', 'enero', 'enríe', 'enrío', 'enteo', 
    'entré', 'entro', 'etneo', 'itere', 'itero', 'nieto', 'nitor', 'nitré', 'nitro', 'norte', 'oreen', 'orine', 'oteen', 
    'reine', 'reino', 'renio', 'rente', 'rento', 'retén', 'retín', 'ritón', 'roete', 'roten', 'tener', 'tenío', 'tenor', 
    'terne', 'terno', 'tiene', 'tiren', 'tirón', 'tóner', 'toreé', 'torne', 'treno', 'tríen', 'triné', 'trino', 'trone', 
    'exir', 'nexo', 'ónix', 'oxeé', 'oxte', 'emir', 'ítem', 'meen', 'mene', 'meno', 'mero', 'mete', 'metí', 'meto', 'míen', 
    'miné', 'mino', 'miré', 'miro', 'mito', 'moer', 'moré', 'morí', 'mote', 'neme', 'nepe', 'nome', 'opté', 'peer', 'peen', 
    'pene', 'peni', 'peno', 'peón', 'peor', 'peri', 'pero', 'peté', 'peto', 'píen', 'pino', 'pion', 'piré', 'piro', 'pite', 
    'pito', 'pone', 'poni', 'pote', 'reme', 'remo', 'repo', 'rimé', 'rimo', 'romí', 'teme', 'temí', 'temo', 'tepe', 'timé', 
    'timo', 'tipo', 'tomé', 'topé', 'éneo', 'ente', 'eren', 'éter', 'neto', 'nito', 'noté', 'oiré', 'oreé', 'oren', 'orín', 
    'orné', 'oteé', 'otre', 'rene', 'reno', 'reté', 'retó', 'ríen', 'rite', 'rito', 'roen', 'rote', 'tené', 'tino', 'tiré', 
    'tiro', 'toen', 'toné', 'tren', 'treo', 'trié', 'trío']

    Word_list_ARGENTINA = ['engaritan', 'tangerina', 'tangieran', 'agitanen', 'agitaren', 'agrietan', 'argentan', 'engaitan', 
    'engaitar', 'engarita', 'garanten', 'gitanean', 'gitanear', 'granatín', 'gratinan', 'gratinen', 'integran', 'negarían', 
    'tangaren', 'tangiera', 'tangiran', 'atinaren', 'entinará', 'atinaren', 'entinara', 'intránea', 'agitané', 'agitaré', 
    'agrieta' 'arengan', 'argenta', 'artigan', 'atengan', 'atingen', 'engaita', 'engatan', 'engatar', 'engrana', 'engrían', 
    'gaitera', 'ganaren', 'garante', 'garieta', 'gatería', 'girante', 'gitanea', 'granate', 'granean', 'gratina', 'gratiné', 
    'grietan', 'ingrata', 'integra', 'negarán', 'negaría', 'negrita', 'ratigan', 'tangaré', 'tangían', 'tangirá', 'tangiré', 
    'traigan', 'aretina', 'arietan', 'atairen', 'atenían', 'aterían', 'atinaré', 'entinar', 'interna', 'ratinan', 'ratinen', 
    'reatina', 'retinan', 'aganen', 'agitan', 'agitar', 'agiten', 'agrían', 'agríen', 'anegar', 'angina', 'arenga', 'artiga', 
    'atenga', 'atinge', 'engata', 'engina', 'engría', 'ganaré', 'gareta', 'garita', 'gatean', 'gatear', 'gatera', 'gineta', 
    'gitana', 'granan', 'granea', 'granen', 'gratan', 'graten', 'gratín', 'grieta', 'gritan', 'griten', 'ignara', 'negará', 
    'niegan', 'raigan', 'ratiga', 'regata', 'regían', 'rengan', 'riegan', 'ringan', 'tangan', 'tangar', 'tangen', 'tangía', 
    'tangir', 'tengan', 'tigana', 'tragan', 'traiga', 'airean', 'antena', 'antera', 'arenan', 'artina', 'ataire', 'ataren', 
    'atenía', 'atería', 'atinan', 'atinar', 'atinen', 'atraen', 'enatía', 'enrían', 'entina', 'entran', 'etaria', 'innata', 
    'iteran', 'nantar', 'narina', 'nitran', 'nitren', 'ranita', 'ratean', 'ratina', 'ratine', 'reatan', 'reinan', 'renana', 
    'rentan', 'retina', 'tarina', 'tenían', 'tierna', 'tirana', 'traían', 'trinan', 'trinen', 'agita', 'agite', 'agria', 
    'agríe', 'anega', 'angra', 'argán', 'argén', 'gaita', 'ganan', 'ganar', 'ganen', 'ganta', 'gante', 'gatea', 'ginea', 
    'giren', 'giran', 'grana', 'grané', 'grata', 'graté', 'grita', 'grité', 'ígnea', 'irgan', 'negar', 'negra', 'niega', 
    'raiga', 'regia', 'renga', 'riega', 'rigen', 'ringa', 'taiga', 'tanga', 'tange', 'tangí', 'tenga', 'tigre', 'tinge', 
    'traga', 'airan', 'airea', 'airen', 'anear', 'arena', 'ataré', 'atear', 'aterí', 'atina', 'atiné', 'atrae', 'enana', 
    'enría', 'entra', 'erina', 'étnia', 'inane', 'itera', 'naire', 'nanea', 'nanta', 'natía', 'natri', 'nenia', 'niara', 
    'nieta', 'nitra', 'nitré', 'raían', 'ratea', 'reata', 'reían', 'reina', 'renta', 'retan', 'retín', 'riata', 'taina', 
    'taran', 'tarea', 'taren', 'tarín', 'teína', 'tenía', 'terna', 'tiara', 'tínea', 'tiran', 'tiren', 'traen', 'traía', 
    'trena', 'trían', 'tríen', 'trina', 'triné', 'agre', 'gana', 'gané', 'gata', 'geta', 'gira', 'gire', 'gran', 'inga', 
    'irga', 'nega', 'regí', 'rige', 'ring', 'aeta', 'aína', 'aíra', 'aire', 'anea', 'anta', 'aran', 'área', 'aren', 'aria', 
    'arna', 'arte', 'atan', 'atar', 'atea', 'aten', 'eirá', 'enta', 'eran', 'ería', 'irán', 'nana', 'nata', 'nena', 'neta', 
    'raen', 'raía', 'rain', 'rana', 'rata', 'reía', 'reta', 'rian', 'rien', 'rita', 'rite', 'tara', 'taré', 'tena', 'tina', 
    'tira', 'tiré', 'trae', 'tren', 'tría', 'trie']

    Word_list_CABALLITO = ['baticola', 'báltica', 'báltico', 'coitaba', 'acolita', 'alicato', 'argentan', 'altaico', 'alcoba', 
    'bacilo', 'biloca', 'bocata', 'botica', 'cabalo', 'cabila', 'cálibo', 'citaba', 'colaba', 'cotaba', 'ociaba', 'tabaco', 
    'tabica', 'tabico', 'tocaba', 'abatió', 'abolía', 'alacio', 'albita', 'álcali', 'atablo', 'balita', 'balito', 'balota', 
    'batial', 'batola', 'bolita', 'calato', 'coaita', 'coital', 'colita', 'cotila', 'labial', 'laical', 'litaba', 'locata', 
    'oblata', 'tablao', 'ábaco', 'aboca', 'acabo', 'bacía', 'bical', 'bloca', 'bocal', 'cabal', 'cabía', 'cabió', 'caoba', 
    'ciaba', 'cibal', 'cobil', 'cobla', 'abatí', 'abato', 'abita', 'abito', 'abolí', 'acato', 'acial', 'acilo', 'acola', 
    'acota', 'alabo', 'álica', 'aloca', 'atacó', 'atiba', 'atibó', 'ática', 'ático', 'atoba', 'baila', 'bailo', 'balta', 
    'balto', 'batía', 'batió', 'bilao', 'biota', 'cálao', 'calta', 'ciato', 'clota', 'coita', 'coatí', 'labia', 'lábil', 
    'labio', 'lacia', 'lacio', 'lacta', 'lacto', 'laica', 'laico', 'liaba', 'loaba', 'local', 'loica', 'tabal', 'tabla', 
    'talco', 'tiaca', 'tlaco', 'toaba', 'tocia', 'alola', 'alota', 'ilota', 'latía', 'latió', 'lilao', 'otila', 'talio', 'baca', 
    'bloc', 'boca', 'cabo', 'cibo', 'coba', 'acal', 'acta', 'acto', 'alba', 'albo', 'alca', 'bala', 'balo', 'bata', 'batí', 'bato', 
    'bita', 'bito', 'bola', 'bota', 'caía', 'cala', 'calo', 'cata', 'cato', 'cita', 'cito', 'cola', 'cota', 'cotí', 'laca', 'laco', 
    'liba', 'libo', 'loba', 'loca', 'ocal', 'ocia', 'taba', 'tabí', 'tabo', 'taca', 'taco', 'tico', 'toba', 'toca', 'alía', 'alío', 
    'alta', 'alto', 'atoa', 'atol', 'iota', 'lata', 'latí', 'lato', 'lila', 'lita', 'lito', 'lota', 'olía', 'tala', 'talo', 'taló', 
    'tilo', 'tola']

    Word_list_CASCABELES = ['cableases', 'cabeceas', 'cascabel', 'ceceabas', 'balacees', 'cablease', 'caseases', 'calacees', 
    'calcases', 'calceses', 'sebáceas', 'albeases', 'baleases', 'balsease', 'escalase', 'laceases', 'leseabas', 'sablease', 
    'cabecea', 'ceceaba', 'balacee', 'becases', 'cabales', 'cabases', 'cableas', 'cablees', 'cacease', 'calaceé', 'calcase', 
    'casabes', 'cascace', 'cebases', 'cacales', 'celabas', 'cesabas', 'escabel', 'sebácea', 'secabas', 'abalees', 'alabees', 
    'albease', 'balases', 'balease', 'balseas', 'balsees', 'basales', 'belesas', 'calases', 'caleses', 'casales', 'celases', 
    'escalas', 'escales', 'escasea', 'lacases', 'lacease', 'lascase', 'leseaba', 'sabelas', 'sableas', 'sablees', 'salaces', 
    'seseaba', 'aleases', 'aselase', 'salease', 'acabes', 'acaece', 'acebal', 'aceces', 'bascas', 'becase', 'cabale', 'cablea', 
    'cableé', 'cables', 'caceas', 'cacees', 'cacles', 'calcas', 'calces', 'casabe', 'cascas', 'cebase', 'ceceas', 'celaba', 
    'cesaba', 'secaba', 'abaleé', 'alabeé', 'alabes', 'albeas', 'albees', 'alceas', 'aleces', 'asaces', 'balase', 'baleas', 
    'balees', 'balsas', 'balsea', 'balseé', 'basase', 'belesa', 'besase', 'calase', 'calesa', 'casase', 'caseas', 'celase', 'cesase', 
    'clases', 'escala', 'escale', 'escasa', 'lacase', 'laceas', 'lacees', 'lascas', 'sabeas', 'sabela', 'sablea', 'sableé', 'sables', 
    'sacase', 'salces', 'secase', 'alease', 'asease', 'aselas', 'aseles', 'leseas', 'salase', 'saleas', 'salees', 'salesa', 'salsea', 
    'salseé', 'abecé', 'acabé', 'acece', 'bacas', 'basca', 'becas', 'cabal', 'cabas', 'cabes', 'cable', 'cacas', 'cacea', 'caceé', 
    'caces', 'cacle', 'calca', 'calce', 'casca', 'cebas', 'cebes', 'cecal', 'cecas', 'cecea', 'abalé', 'acles', 'alabé', 'albas', 
    'albea', 'albeé', 'alcas', 'alcea', 'alces', 'alece', 'ascas', 'balas', 'balea', 'baleé', 'bales', 'balsa', 'basal', 'basas', 
    'bases', 'beles', 'besas', 'beses', 'calas', 'cales', 'casal', 'casas', 'cásea', 'cases', 'celas', 'celes', 'cesas', 'ceses', 
    'clase', 'lacas', 'lacea', 'laceé', 'laces', 'lasca', 'sabea', 'sabes', 'sable', 'sacas', 'sebes', 'aleas', 'alees', 'asase', 
    'aseas', 'asees', 'asela', 'aselé', 'asesa', 'asesé', 'lasas', 'lesas', 'lesea', 'salas', 'salea', 'saleé', 'sales', 'salsa', 
    'sasal', 'seles', 'sesea', 'baca', 'beca', 'cabe', 'caca', 'cacé', 'ceba', 'cebe', 'ceca', 'acal', 'acle', 'alba', 'alca', 'alce', 
    'asca', 'bala', 'balé', 'basa', 'base', 'besa', 'besé', 'caes', 'cala', 'calé', 'casa', 'casé', 'ceas', 'cela', 'celé', 'cesa', 
    'cese', 'esca', 'labe', 'laca', 'lacé', 'sabe', 'saca', 'sebe', 'seca', 'alas', 'alea', 'aleé', 'asas', 'asea', 'ases', 'eles', 
    'esas', 'eses', 'lasa', 'leas', 'lees', 'lesa', 'sala', 'sale']

    Word_list_HOLOCAUSTO = ['actuoso', 'costalo', 'cultosa', 'cultoso', 'locatos', 'locutas', 'ocotosa', 'ocultas', 'ocultos', 
    'talcoso', 'holcos', 'huacos', 'hostal', 'acostó', 'acuoso', 'asulcó', 'caloso', 'castúo', 'cautos', 'clotas', 'coloso', 'costal', 
    'cotúas', 'cultas', 'cultos', 'cuotas', 'locato', 'locuta', 'locuto', 'ocluso', 'ocotal', 'oculta', 'oculto', 'ósculo', 'socola', 
    'socoló', 'talcos', 'tlacos', 'tuscal', 'latoso', 'lautos', 'lutosa', 'lutoso', 'soluto', 'holco', 'hosca', 'hosco', 'huaco', 'ahúso', 
    'halos', 'hatos', 'hotos', 'huaos', 'hulas', 'hutas', 'acoló', 'acoso', 'acotó', 'actos', 'actúo', 'aculo', 'acusó', 'acuto', 'alocó', 
    'catos', 'causo', 'cauto', 'clota', 'colas', 'costa', 'costó', 'cotas', 'cotos', 'cotúa', 'culos', 'culta', 'culto', 'cuota', 'cutas', 
    'cutos', 'lactó', 'lascó', 'locas', 'locos', 'lucas', 'lusco', 'lusca', 'ocaso', 'sauco', 'socol', 'sulco', 'tacos', 'talco', 'tasco', 
    'taucó', 'tlaco', 'tocas', 'tocos', 'tosco', 'tosca', 'tusca', 'tusco', 'alotó', 'altos', 'asoló', 'atusó', 'ausol', 'autos', 'lasto', 
    'latos', 'lauto', 'lotos', 'lutos', 'salto', 'soltá', 'soltó', 'sotol', 'suato', 'talos', 'tolas', 'halo', 'hato', 'hola', 'hoto', 
    'huao', 'hula', 'huló', 'huso', 'huta', 'acto', 'asco', 'caló', 'caos', 'caso', 'cató', 'coas', 'cola', 'coló', 'cosa', 'coso', 'cota', 
    'coto', 'cuál', 'culo', 'cusa', 'cusó', 'cuto', 'cuta', 'lacó', 'loca', 'loco', 'luca', 'luco', 'ocal', 'ocas', 'osca', 'osco', 'saco', 
    'soca', 'suco', 'taco', 'toca', 'tocó', 'tuca', 'tuco', 'alto', 'atol', 'atoó', 'auto', 'laso', 'lato', 'loas', 'losa', 'losó', 'lota', 
    'loto', 'lúas', 'luso', 'lusa', 'luto', 'olas', 'osta', 'otos', 'saló', 'sato', 'sola', 'solo', 'sota', 'soto', 'sula', 'taló', 'talo', 
    'taos', 'tasó', 'toas', 'tola', 'tosa', 'toso', 'tusa', 'tuso']

    Word_list_ELEFANTES = ['fleteasen', 'elefante', 'fletanes', 'fletasen', 'fletease', 'entelase', 'estafen', 'falseen', 'falsete', 'falseen', 
    'fenales', 'festean', 'festeen', 'fetales', 'fetenes', 'fletase', 'fletean', 'fleteas', 'fleteen', 'fletees', 'aleteen', 'aletees', 'anteles', 
    'eneales', 'enlates', 'entelas', 'enteles', 'saeteen', 'salteen', 'éfetas', 'estafé', 'faenes', 'falseé', 'falsen', 'falten', 'faltes', 'flanes', 
    'fletan', 'fletas', 'fletea', 'fleteé', 'fleten', 'fletes', 'alenté', 'aleteé', 'alteen', 'altees', 'antele', 'antelé', 'aselen', 'asente', 
    'asenté', 'atenes', 'atesen', 'enaste', 'atesen', 'enlate', 'entela', 'entele', 'entesa', 'entese', 'estela', 'etneas', 'lasten', 'latees', 
    'lateen', 'leneas', 'lentas', 'lentes', 'lesean', 'leseen', 'saeteé', 'saeten', 'saleen', 'salteé', 'salten', 'setena', 'setene', 'setené', 
    'taeles', 'tesela', 'afeen', 'afees', 'alfen', 'alfes', 'éfeta', 'faene', 'falsé', 'falté', 'fanes', 'fenal', 'fetal', 'fetas', 'fetén', 'fleta', 
    'flete', 'aleen', 'alees', 'alteé', 'antes', 'aseen', 'asele', 'atese', 'eleta', 'eneal', 'eneas', 'entes', 'están', 'estén', 'etnea', 'lasté', 
    'lateé', 'laten', 'lates', 'lenas', 'lenes', 'lenta', 'lente', 'lesea', 'lesee', 'leste', 'letea', 'neles', 'saete', 'salee', 'salen', 'salté', 
    'saneé', 'satén', 'senté', 'setal', 'talen', 'tales', 'tasen', 'telas', 'tenas', 'tenés', 'tensa', 'tensé', 'tesan', 'tesen', 'tesla', 'afee', 
    'álef', 'alfé', 'efes', 'fase', 'feas', 'feta', 'flan', 'aleé', 'aseé', 'asen', 'aten', 'ates', 'eles', 'enea', 'enes', 'enta', 'ente', 'esta', 
    'este', 'etas', 'late', 'lean', 'leas', 'leen', 'lees', 'lena', 'lene', 'lesa', 'neas', 'neta', 'sale', 'sane', 'sean', 'sena', 'sete', 'seta', 
    'tael', 'talé', 'tasé', 'teas', 'tela', 'telé', 'tena', 'tesa', 'tesé']

    Word_list_COBARDÍA = ['acribado', 'boricada', 'carábido', 'abdicar', 'acribad', 'bocarda', 'brocada', 'cribada', 'cribado', 'acibaró', 'acibaro', 
    'arábico', 'rociaba', 'acárido', 'arcadio', 'aricado', 'cariado', 'rabiado', 'rociada', 'abdica', 'abdicó', 'abocad', 'bocada', 'cabida', 'cabido', 
    'cobrad', 'cribad', 'abarcó', 'abarco', 'abocar', 'abraco', 'acíbar', 'acriba', 'acribó', 'barcia', 'bárico', 'bárica', 'cabría', 'cabrío', 'cárabo', 
    'caroba', 'criaba', 'croaba', 'ociaba', 'rábico', 'rábica', 'aborda', 'acadio', 'acodar', 'acordá', 'adobar', 'arcado', 'aricad', 'cadira', 'carado', 
    'cariad', 'corada', 'criada', 'criado', 'darico', 'doraba', 'dórica', 'obrada', 'odiaba', 'rabiad', 'rábida', 'rábido', 'radica', 'radico', 'robada', 
    'rocada', 'rociad', 'rodaba', 'arabio', 'ociara', 'airado', 'odiará', 'ábaco', 'aboca', 'acabo', 'acabó', 'bacía', 'barca', 'barco', 'braca', 'braco', 
    'broca', 'cabía', 'cabió', 'cabra', 'cabro', 'caoba', 'carba', 'ciaba', 'cobra', 'criba', 'cribó', 'abadí', 'abrid', 'ácida', 'ácido', 'acoda', 'arcad', 
    'baída', 'barda', 'bardo', 'borda', 'brida', 'caída', 'caído', 'carda', 'cardo', 'ciado', 'cidra', 'cidro', 'corda', 'criad', 'crida', 'croad', 'dacia', 
    'dacio', 'draba', 'obrad', 'ociad', 'robad', 'robda', 'abiar', 'abría', 'abrió', 'ácaro', 'acora', 'aocar', 'arabí', 'arabo', 'arica', 'arico', 'aroca', 
    'baria', 'bario', 'boira', 'boria', 'carao', 'caria', 'cario', 'ciara', 'ciará', 'ociar', 'oraba', 'rabia', 'rabió', 'rocía', 'adiar', 'adora', 'airad', 
    'arado', 'ardía', 'ardió', 'árida', 'árido', 'daria', 'dario', 'irado', 'irada', 'odiar', 'orada', 'radía', 'radio', 'raído', 'riada', 'rodia', 'roída', 
    'baca', 'boca', 'cabo', 'cibo', 'coba', 'abad', 'bada', 'boda', 'cada', 'cadi', 'cado', 'ciad', 'coda', 'daba', 'daca', 'doca', 'abar', 'abia', 'abra', 
    'abrí', 'abro', 'arca', 'arco', 'barí', 'baro', 'biro', 'bira', 'brío', 'broa', 'caía', 'cara', 'cari', 'caro', 'ciar', 'cora', 'cori', 'cría', 'crió', 
    'croa', 'icor', 'obra', 'ocia', 'ocra', 'orca', 'raba', 'rabí', 'rabo', 'raco', 'riba', 'rica', 'rico', 'roca', 'roba', 'adía', 'adío', 'adir', 'ador', 
    'adra', 'adro', 'arad', 'arda', 'ardí', 'ardo', 'dará', 'dirá', 'dora', 'dría', 'odia', 'oída', 'orad', 'rada', 'roda', 'aira', 'airo', 'aria', 'ario', 
    'oirá', 'raía', 'roía']

    Word_list_MANDARINA = ['amadrinan', 'dimanarán', 'mandarian', 'amadrina', 'amrinad', 'dimanará', 'mandarán', 'mandaría', 'mandarín', 'marinada', 'amarinan', 
    'aminaran', 'animarán', 'imanarán', 'manarían', 'andarían', 'andarina', 'anidaran', 'anidarán', 'arandina', 'nadarían', 'admiran', 'amainad', 'animada', 
    'armadía', 'damiana', 'dimanan', 'dimanar', 'imanada', 'madrina', 'mandará', 'mandria', 'maridan', 'marinad', 'ramadán', 'amainan', 'amainar', 'amarían', 
    'amarina', 'aminara', 'animará', 'animara', 'imanara', 'imanará', 'manaran', 'manarán', 'manaría', 'manirán', 'marinan', 'minaran', 'minarán', 'adiaran', 
    'anadina', 'andarán', 'andaría', 'andarín', 'andrina', 'anidara', 'anidará', 'nadaran', 'nadarán', 'nadaría', 'nardina', 'adaman', 'adamar', 'admira', 
    'amanad', 'amarad', 'aminad', 'animad', 'armada', 'dimana', 'imanad', 'manada', 'mandan', 'mandar', 'mandra', 'manida', 'marida', 'minada', 'mirada', 
    'ramada', 'rimada', 'aimara', 'amaina', 'amanan', 'amanar', 'amaran', 'amaría', 'aminan', 'aminar', 'imanan', 'imanar', 'manará', 'manían', 'marina', 
    'miarán', 'minará', 'ramina', 'adiana', 'adiará', 'airada', 'andana', 'andará', 'andina', 'anidan', 'anidar', 'ardían', 'arnadí', 'darían', 'nadara', 
    'nadará', 'radían', 'rindan', 'narina', 'ranina', 'adama', 'amada', 'amida', 'armad', 'drama', 'imada', 'manad', 'manda', 'mandí', 'manid', 'minad', 
    'mirad', 'rimad', 'amana', 'amará', 'anima', 'arman', 'imana', 'manan', 'manar', 'manía', 'manir', 'miara', 'miará', 'minan', 'minar', 'miran', 'riman', 
    'adían', 'adiar', 'adran', 'airad', 'andan', 'andar', 'anida', 'arada', 'ardan', 'ardía', 'árida', 'darán', 'daría', 'dinar', 'dirán', 'irada', 'nadan', 
    'nadar', 'nadir', 'radia', 'raída', 'randa', 'riada', 'rinda', 'airan', 'ananá', 'arana', 'niara', 'raían', 'amad', 'dama', 'miad', 'mida', 'aman', 'amar', 
    'amia', 'amín', 'amir', 'arma', 'imán', 'maná', 'maní', 'mara', 'miar', 'mina', 'mira', 'rama', 'rima', 'adir', 'adra', 'anda', 'arad', 'arda', 'ardí', 'dará', 
    'dirá', 'dría', 'inda', 'nada', 'nadi', 'rada', 'rand', 'aína', 'aira', 'aran', 'aria', 'arna', 'irán', 'nana', 'raía', 'rain', 'rana', 'rían']

    Word_list_TELEPATÍA = ['talepate', 'apetite', 'paletea', 'patalee', 'pataleé', 'petatea', 'pleitea', 'tepetal', 'apalee', 'apaleé', 'apeale', 'apealé', 
    'atipla', 'atiplé', 'atiple', 'lapita', 'paleta', 'pateta', 'petate', 'pileta', 'platea', 'platee', 'plateé', 'pleita', 'tápate', 'tapete', 'tapial', 'aletea', 
    'atleta', 'talete', 'teleta', 'apela', 'apele', 'apelé', 'apila', 'apile', 'apilé', 'apita', 'apite', 'apité', 'atipa', 'atipe', 'atipé', 'épale', 'epata', 
    'epate', 'epaté', 'etapa', 'paila', 'palea', 'palee', 'paleé', 'palia', 'palie', 'palié', 'palta', 'patea', 'patee', 'pateé', 'peala', 'peale', 'pealé', 'pelea', 
    'pelta', 'piala', 'piale', 'pialé', 'pital', 'pitea', 'pitee', 'piteé', 'plata', 'taipa', 'talpa', 'tapea', 'tapee', 'tapeé', 'tapia', 'tapie', 'tapié', 'tiple', 
    'aleta', 'altea', 'altee', 'alteé', 'ateta', 'atete', 'ateté', 'elata', 'eleta', 'élite', 'ítala', 'latea', 'latee', 'lateé', 'latía', 'letea', 'taita', 'tálea', 
    'titea', 'titee', 'titeé', 'apea', 'apeé', 'apta', 'lapa', 'lipa', 'pala', 'palé', 'pali', 'pata', 'paté', 'patí', 'peal', 'peía', 'pela', 'pelé', 'pele', 'peta', 
    'pete', 'peté', 'pial', 'piel', 'pila', 'pile', 'pilé', 'pita', 'pite', 'pité', 'tapa', 'tapé', 'tape', 'tepe', 'tipa', 'aeta', 'alea', 'alee', 'aleé', 'alía', 
    'alié', 'alíe', 'alta', 'atal', 'atea', 'lata', 'late', 'latí', 'leía', 'lita', 'lité', 'tael', 'tala', 'talé', 'tata', 'tate', 'tela', 'tele', 'teta', 'tete', 
    'tila', 'tile', 'tita']

    Word_list_COMUNICACIÓN = ['incomunica', 'incomunico', 'incomunicó', 'amunicionó', 'amuniciono', 'comunican', 'concomían', 'miccionan', 'inoacción', 
    'municiona', 'municiono', 'municionó', 'cinámico', 'coacción', 'comunica', 'comunico', 'comunicó', 'concoman', 'concomía', 'micciona', 'micciono', 
    'miccionó', 'monicaco', 'canónico', 'cauciono', 'caucionó', 'comunión', 'conocían', 'inacción', 'mocionan', 'monición', 'munición', 'nomónica', 
    'aniónico', 'cimacio', 'cocción', 'concoma', 'concomí', 'micción', 'acciono', 'accionó', 'amínico', 'amónico', 'anímico', 'aucción', 'canción', 'caución', 
    'ciánico', 'cocinan', 'coición', 'concina', 'concino', 'conción', 'concoma', 'conmina', 'conmino', 'conminó', 'conocía', 'icónica', 'icónico', 'incaico', 
    'minción', 'minoica', 'minoico', 'minucia', 'mociona', 'monoica', 'anónimo', 'anuncio', 'innocuo', 'innocua', 'minuano', 'cómica', 'cómico', 'macuco', 'acción', 
    'acucio', 'acució', 'ancuco', 'caminí', 'camino', 'camión', 'cancín', 'cancón', 'cición', 'cínica', 'cínico', 'cocían', 'cocina', 'cocino', 'cocinó', 'comuna', 
    'concia', 'concón', 'cónica', 'cónico', 'conocí', 'conuco', 'cumano', 'mocano', 'moción', 'nómica', 'nómico', 'amonio', 'amuino', 'amuinó', 'canino', 'incoan', 
    'incona', 'incono', 'inconó', 'inicua', 'inicuo', 'inocua', 'inocuo', 'iónica', 'iónico', 'minian', 'minina', 'minino', 'monona', 'nación', 'noción', 'nomina', 
    'nomino', 'nominó', 'nuncio', 'ominan', 'uncían', 'unción', 'cómic', 'ácimo', 'acoco', 'acocó', 'caico', 'camón', 'cinca', 'cinco', 'cocan', 'cocía', 'coció', 'coima', 
    'coman', 'comía', 'comió', 'común', 'conca', 'cuaco', 'cucan', 'cuica', 'cuico', 'icaco', 'macío', 'macón', 'manco', 'mocan', 'ocumo', 'ación', 'acuno', 'acunó', 
    'amino', 'amono', 'amonó', 'ancón', 'ánimo', 'canon', 'cianí', 'cinia', 'cuina', 'cuino', 'ícono', 'incoa', 'incoo', 'incoó', 'minan', 'minia', 'minió', 'minio', 
    'miona', 'nació', 'nimio', 'nimia', 'nomon', 'nunca', 'uncía', 'unció', 'única', 'único', 'aonio', 'nonio', 'unían', 'unión', 'caco', 'cica', 'cima', 'coca', 'cocí', 
    'coco', 'coma', 'comí', 'como', 'cuca', 'cuco', 'cuma', 'mica', 'moca', 'moco', 'muca', 'muco', 'cano', 'cian', 'cono', 'cuan', 'cuán', 'cuin', 'cuna', 'imán', 'inca', 
    'maní', 'mano', 'miau', 'mina', 'mona', 'mono', 'muna', 'muon', 'nací', 'naco', 'noca', 'noma', 'nomo', 'nuca', 'nuco', 'numo', 'ocio', 'uncí', 'anuo', 'nona', 'nono', 
    'oían', 'unan', 'unía', 'unió']

    lista =[Word_list_EXPERIMENTO, Word_list_ARGENTINA, Word_list_CABALLITO, Word_list_CASCABELES, Word_list_HOLOCAUSTO,
    Word_list_ELEFANTES, Word_list_COBARDÍA, Word_list_MANDARINA, Word_list_TELEPATÍA, Word_list_COMUNICACIÓN ]

    s_inc=0
    c_inc=0.2

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number==1:
            import itertools
            treat = itertools.cycle(['C','T1','T2','T3'])
            for g in self.get_groups():
                p1=g.get_player_by_id(1)
                p1.participant.vars['treatment']=next(treat)
                g.treatment=p1.participant.vars['treatment']
                print('Treatment:', p1.participant.vars['treatment']) 

        #import itertools
        #colors = itertools.cycle(['blue', 'red'])
        #for player in self.get_players():
        #    player.color = next(colors)
        self.mariposa_1=hola_1()
        self.mariposa_2=hola_2(self)
        self.mariposa_3=hola_3(self)
        self.mariposa_4=hola_4(self)
    
    mariposa_1=models.CharField()
    mariposa_2=models.CharField()
    mariposa_3=models.CharField()
    mariposa_4=models.CharField()

def hola_1(): 
    palabra_aleatoria = models.CharField(initial='')
    palabra_aleatoria= random.choice(Constants.Word_list_preguntas)
    return palabra_aleatoria
#mariposa_1 = hola_1()

def hola_2(subsession:Subsession): 
    palabra_aleatoria = models.CharField(initial='')
    palabra_aleatoria= random.choice(Constants.Word_list_preguntas)
    while subsession.mariposa_1 == palabra_aleatoria:
        palabra_aleatoria=random.choice(Constants.Word_list_preguntas)
        if subsession.mariposa_1 != palabra_aleatoria:
            break
    return palabra_aleatoria
#mariposa_2 = hola_2()

###revisar el None, si sale la misma palabra -->while --> revisar para uno y si es que va, replicar 
##cambiar ID por label
##que no pase si es que está vacío -->correr esa parte (aun falta)
##mostrar el pago --> revisar si es que funciona para ambas apps
##RECORDAR QUE NO A TODOS LOS PARTICIOANTES SE LES PAGAN, SÓLO A LOS DEL TRATAMIENTO 1 Y 3
######es decir, sólo a esos grupos se les paga 0.20 por pregunta, o sino 0
def hola_3(subsession:Subsession): 
    palabra_aleatoria = models.CharField(initial='')
    palabra_aleatoria= random.choice(Constants.Word_list_preguntas)
    while palabra_aleatoria == subsession.mariposa_1 or palabra_aleatoria == subsession.mariposa_2:
        palabra_aleatoria=random.choice(Constants.Word_list_preguntas)
        if palabra_aleatoria != subsession.mariposa_1 and palabra_aleatoria != subsession.mariposa_2:
            break
    return palabra_aleatoria
#mariposa_3 = hola_3()

def hola_4(subsession:Subsession): 
    palabra_aleatoria = models.CharField(initial='')
    palabra_aleatoria= random.choice(Constants.Word_list_preguntas)
    while palabra_aleatoria == subsession.mariposa_1 or palabra_aleatoria == subsession.mariposa_2 or palabra_aleatoria == subsession.mariposa_3:
        palabra_aleatoria=random.choice(Constants.Word_list_preguntas)
        if palabra_aleatoria != subsession.mariposa_1 and palabra_aleatoria != subsession.mariposa_2 and palabra_aleatoria != subsession.mariposa_3:
            break
    return palabra_aleatoria
#mariposa_4 = hola_4()

  
class Group(BaseGroup):
    treatment=models.CharField()

    arrive_p=models.StringField()

    def wp_p(self):   
        self.arrive_p='Listo'

    def rank_p(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        r_1=0 ##id player
        r_2=0
        r_3=0
        r_4=0

        for p in self.get_players(): 
            if p.total_score_p >= i_4:
                i_4=p.total_score_p
                r_4=p.id_in_group
            if i_4 >= i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=r_3
                r_3=r_4
                r_4=tee
            if i_3 >= i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=r_2
                r_2=r_3
                r_3=tee
            if i_2 >= i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=r_1
                r_1=r_2
                r_2=tee
        return [i_1, i_2, i_3, i_4], [r_1, r_2, r_3, r_4]

    ##para R1
    def pato_1(self):    
        players = self.get_players()
        for p in players: 
            p.palabra_pregunta_R1=self.subsession.mariposa_1
        return p.palabra_pregunta_R1    

    arrive_1=models.StringField()

    def wp_1(self):   
        self.arrive_1='Listo'

    puesto1_R1=models.IntegerField()
    puesto2_R1=models.IntegerField()
    puesto3_R1=models.IntegerField()
    puesto4_R1=models.IntegerField()

    def rank_R1(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        #r_1=0 ##id player
        #r_2=0
        #r_3=0
        #r_4=0
        self.puesto1_R1=0
        self.puesto2_R1=0
        self.puesto3_R1=0
        self.puesto4_R1=0

        for p in self.get_players(): 
            if p.total_score_R1 >= i_4: 
                i_4=p.total_score_R1
                self.puesto4_R1=p.id_in_group
            if i_4 >= i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=self.puesto3_R1
                self.puesto3_R1=self.puesto4_R1
                self.puesto4_R1=tee
            if i_3 >= i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=self.puesto2_R1
                self.puesto2_R1=self.puesto3_R1
                self.puesto3_R1=tee
            if i_2 >= i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=self.puesto1_R1
                self.puesto1_R1=self.puesto2_R1
                self.puesto2_R1=tee
        return [i_1, i_2, i_3, i_4], [self.puesto1_R1, self.puesto2_R1, self.puesto3_R1, self.puesto4_R1]
        #[r_1, r_2, r_3, r_4]

    def pp_1(self):
        if self.treatment=='T1' or self.treatment=='T3':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R1:
                    player.pay_1=player.total_score_R1*Constants.c_inc
                else:
                    player.pay_1=0
        elif self.treatment=='C' or self.treatment=='T2':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R1:
                    player.pay_1=player.total_score_R1*Constants.s_inc
                else:
                    player.pay_1=0


    ##para R2
    def pato_2(self):    
        players = self.get_players()
        for p in players: 
            p.palabra_pregunta_R2=self.subsession.mariposa_2
        return p.palabra_pregunta_R2

    arrive_2=models.StringField()

    def wp_2(self):   
        self.arrive_2='Listo' 

    def rank_R2(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        r_1=0 ##id player
        r_2=0
        r_3=0
        r_4=0
    
    puesto1_R2=models.IntegerField()
    puesto2_R2=models.IntegerField()
    puesto3_R2=models.IntegerField()
    puesto4_R2=models.IntegerField()

    def rank_R2(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        #r_1=0 ##id player
        #r_2=0
        #r_3=0
        #r_4=0

        self.puesto1_R2=0
        self.puesto2_R2=0
        self.puesto3_R2=0
        self.puesto4_R2=0

        for p in self.get_players(): 
            if p.total_score_R2 >= i_4: 
                i_4=p.total_score_R2
                self.puesto4_R2=p.id_in_group
            if i_4 >= i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=self.puesto3_R2
                self.puesto3_R2=self.puesto4_R2
                self.puesto4_R2=tee
            if i_3 >= i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=self.puesto2_R2
                self.puesto2_R2=self.puesto3_R2
                self.puesto3_R2=tee
            if i_2 >= i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=self.puesto1_R2
                self.puesto1_R2=self.puesto2_R2
                self.puesto2_R2=tee
        return [i_1, i_2, i_3, i_4], [self.puesto1_R2, self.puesto2_R2, self.puesto3_R2, self.puesto4_R2]

    def pp_2(self):
        if self.treatment=='T1' or self.treatment=='T3':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R2:
                    player.pay_2=player.total_score_R2*Constants.c_inc
                else:
                    player.pay_2=0
        elif self.treatment=='C' or self.treatment=='T2':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R2:
                    player.pay_2=player.total_score_R2*Constants.s_inc
                else:
                    player.pay_2=0

    ##para R3
    def pato_3(self):    
        players = self.get_players()
        for p in players: 
            p.palabra_pregunta_R3=self.subsession.mariposa_3
        return p.palabra_pregunta_R3 
    
    arrive_3=models.StringField()

    def wp_3(self):   
        self.arrive_3='Listo'

    puesto1_R3=models.IntegerField()
    puesto2_R3=models.IntegerField()
    puesto3_R3=models.IntegerField()
    puesto4_R3=models.IntegerField()

    def rank_R3(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        #r_1=0 ##id player
        #r_2=0
        #r_3=0
        #r_4=0

        self.puesto1_R3=0
        self.puesto2_R3=0
        self.puesto3_R3=0
        self.puesto4_R3=0

        for p in self.get_players(): 
            if p.total_score_R3 >= i_4: 
                i_4=p.total_score_R3
                self.puesto4_R3=p.id_in_group
            if i_4 >= i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=self.puesto3_R3
                self.puesto3_R3=self.puesto4_R3
                self.puesto4_R3=tee
            if i_3 >= i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=self.puesto2_R3
                self.puesto2_R3=self.puesto3_R3
                self.puesto3_R3=tee
            if i_2 >= i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=self.puesto1_R3
                self.puesto1_R3=self.puesto2_R3
                self.puesto2_R3=tee
        return [i_1, i_2, i_3, i_4], [self.puesto1_R3, self.puesto2_R3, self.puesto3_R3, self.puesto4_R3]

    def pp_3(self):
        if self.treatment=='T1' or self.treatment=='T3':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R3:
                    player.pay_3=player.total_score_R3*Constants.c_inc
                else:
                    player.pay_3=0
        elif self.treatment=='C' or self.treatment=='T2':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R3:
                    player.pay_3=player.total_score_R3*Constants.s_inc
                else:
                    player.pay_3=0

    ##para R4
    def pato_4(self):    
        players = self.get_players()
        for p in players: 
            p.palabra_pregunta_R4=self.subsession.mariposa_4
        return p.palabra_pregunta_R4 
    
    arrive_4=models.StringField()

    def wp_4(self):   
        self.arrive_4='Listo'

    puesto1_R4=models.IntegerField()
    puesto2_R4=models.IntegerField()
    puesto3_R4=models.IntegerField()
    puesto4_R4=models.IntegerField()

    def rank_R4(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        #r_1=0 ##id player
        #r_2=0
        #r_3=0
        #r_4=0

        self.puesto1_R4=0
        self.puesto2_R4=0
        self.puesto3_R4=0
        self.puesto4_R4=0

        for p in self.get_players(): 
            if p.total_score_R4 >= i_4: 
                i_4=p.total_score_R4
                self.puesto4_R4=p.id_in_group
            if i_4 >= i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=self.puesto3_R4
                self.puesto3_R4=self.puesto4_R4
                self.puesto4_R4=tee
            if i_3 >= i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=self.puesto2_R4
                self.puesto2_R4=self.puesto3_R4
                self.puesto3_R4=tee
            if i_2 >= i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=self.puesto1_R4
                self.puesto1_R4=self.puesto2_R4
                self.puesto2_R4=tee
        return [i_1, i_2, i_3, i_4], [self.puesto1_R4, self.puesto2_R4, self.puesto3_R4, self.puesto4_R4]

    def pp_4(self):
        if self.treatment=='T1' or self.treatment=='T3':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R4:
                    player.pay_4=player.total_score_R4*Constants.c_inc
                else:
                    player.pay_4=0
        elif self.treatment=='C' or self.treatment=='T2':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R4:
                    player.pay_4=player.total_score_R4*Constants.s_inc
                else:
                    player.pay_4=0

class Player(BasePlayer):
    answer_1_p=models.StringField(blank=True)
    answer_2_p=models.StringField(blank=True)
    answer_3_p=models.StringField(blank=True)
    answer_4_p=models.StringField(blank=True)
    answer_5_p=models.StringField(blank=True)
    answer_6_p=models.StringField(blank=True)
    answer_7_p=models.StringField(blank=True)
    answer_8_p=models.StringField(blank=True)
    answer_9_p=models.StringField(blank=True)
    answer_10_p=models.StringField(blank=True)
    answer_11_p=models.StringField(blank=True)
    answer_12_p=models.StringField(blank=True)
    answer_13_p=models.StringField(blank=True)
    answer_14_p=models.StringField(blank=True)
    answer_15_p=models.StringField(blank=True)
    answer_16_p=models.StringField(blank=True)
    answer_17_p=models.StringField(blank=True)
    answer_18_p=models.StringField(blank=True)
    answer_19_p=models.StringField(blank=True)
    answer_20_p=models.StringField(blank=True)
    answer_21_p=models.StringField(blank=True)
    answer_22_p=models.StringField(blank=True)
    answer_23_p=models.StringField(blank=True)
    answer_24_p=models.StringField(blank=True)
    answer_25_p=models.StringField(blank=True)

    total_score_p=models.IntegerField(initial=0)

    def puntaje_p(self): 
        respuestas = [self.answer_1_p, self.answer_2_p, self.answer_3_p, self.answer_4_p, self.answer_5_p, self.answer_6_p, 
        self.answer_7_p, self.answer_8_p, self.answer_9_p, self.answer_10_p, self.answer_11_p, self.answer_12_p, self.answer_13_p, 
        self.answer_14_p, self.answer_15_p, self.answer_16_p, self.answer_17_p, self.answer_18_p, self.answer_19_p, self.answer_20_p, 
        self.answer_21_p, self.answer_22_p, self.answer_23_p, self.answer_24_p, self.answer_25_p]   
           
        for x in respuestas:
            if x in Constants.Word_list_ALEATORIO:
                self.total_score_p=self.total_score_p + 1
            else:
                self.total_score_p=self.total_score_p
        return self.total_score_p

    #para R1
    answer_1_R1=models.StringField(blank=True)
    answer_2_R1=models.StringField(blank=True)
    answer_3_R1=models.StringField(blank=True)
    answer_4_R1=models.StringField(blank=True)
    answer_5_R1=models.StringField(blank=True)
    answer_6_R1=models.StringField(blank=True)
    answer_7_R1=models.StringField(blank=True)
    answer_8_R1=models.StringField(blank=True)
    answer_9_R1=models.StringField(blank=True)
    answer_10_R1=models.StringField(blank=True)
    answer_11_R1=models.StringField(blank=True)
    answer_12_R1=models.StringField(blank=True)
    answer_13_R1=models.StringField(blank=True)
    answer_14_R1=models.StringField(blank=True)
    answer_15_R1=models.StringField(blank=True)
    answer_16_R1=models.StringField(blank=True)
    answer_17_R1=models.StringField(blank=True)
    answer_18_R1=models.StringField(blank=True)
    answer_19_R1=models.StringField(blank=True)
    answer_20_R1=models.StringField(blank=True)
    answer_21_R1=models.StringField(blank=True)
    answer_22_R1=models.StringField(blank=True)
    answer_23_R1=models.StringField(blank=True)
    answer_24_R1=models.StringField(blank=True)
    answer_25_R1=models.StringField(blank=True)

    total_score_R1=models.IntegerField(initial=0)

    palabra_pregunta_R1=models.StringField()

    def puntaje_R1(self):    
        
        respuestas = [self.answer_1_R1, self.answer_2_R1, self.answer_3_R1, self.answer_4_R1, self.answer_5_R1, 
        self.answer_6_R1, self.answer_7_R1, self.answer_8_R1, self.answer_9_R1, self.answer_10_R1, self.answer_11_R1, 
        self.answer_12_R1, self.answer_13_R1, self.answer_14_R1, self.answer_15_R1, self.answer_16_R1, self.answer_17_R1, 
        self.answer_18_R1, self.answer_19_R1, self.answer_20_R1, self.answer_21_R1, self.answer_22_R1, self.answer_23_R1, 
        self.answer_24_R1, self.answer_25_R1]

        if self.subsession.mariposa_1 == 'ARGENTINA':
            for x in respuestas:
                    if x in Constants.Word_list_ARGENTINA:
                        self.total_score_R1=self.total_score_R1 + 1
                    else:
                        self.total_score_R1=self.total_score_R1
            return self.total_score_R1  

        if self.subsession.mariposa_1 == 'EXPERIMENTO': 
            for x in respuestas:
                    if x in Constants.Word_list_EXPERIMENTO:
                        self.total_score_R1=self.total_score_R1 + 1
                    else:
                        self.total_score_R1=self.total_score_R1
            return self.total_score_R1 

        if self.subsession.mariposa_1 == 'CABALLITO': 
            for x in respuestas:
                    if x in Constants.Word_list_CABALLITO:
                        self.total_score_R1=self.total_score_R1 + 1
                    else:
                        self.total_score_R1=self.total_score_R1
            return self.total_score_R1 

        if self.subsession.mariposa_1 == 'CASCABELES':
            for x in respuestas:
                    if x in Constants.Word_list_CASCABELES:
                        self.total_score_R1=self.total_score_R1 + 1
                    else:
                        self.total_score_R1=self.total_score_R1
            return self.total_score_R1 

        if self.subsession.mariposa_1 == 'HOLOCAUSTO': 
            for x in respuestas:
                    if x in Constants.Word_list_HOLOCAUSTO:
                        self.total_score_R1=self.total_score_R1 + 1
                    else:
                        self.total_score_R1=self.total_score_R1
            return self.total_score_R1 

        if self.subsession.mariposa_1 == 'ELEFANTES': 
            for x in respuestas:
                    if x in Constants.Word_list_ELEFANTES:
                        self.total_score_R1=self.total_score_R1 + 1
                    else:
                        self.total_score_R1=self.total_score_R1
            return self.total_score_R1 

        if self.subsession.mariposa_1 == 'MANDARINA':
            for x in respuestas:
                    if x in Constants.Word_list_MANDARINA:
                        self.total_score_R1=self.total_score_R1 + 1
                    else:
                        self.total_score_R1=self.total_score_R1
            return self.total_score_R1 

        if self.subsession.mariposa_1 == 'TELEPATÍA':
            for x in respuestas:
                    if x in Constants.Word_list_TELEPATÍA:
                        self.total_score_R1=self.total_score_R1 + 1
                    else:
                        self.total_score_R1=self.total_score_R1
            return self.total_score_R1

        if self.subsession.mariposa_1 == 'COBARDÍA':
            for x in respuestas:
                    if x in Constants.Word_list_COBARDÍA:
                        self.total_score_R1=self.total_score_R1 + 1
                    else:
                        self.total_score_R1=self.total_score_R1
            return self.total_score_R1

        if self.subsession.mariposa_1 == 'COMUNICACIÓN':
            for x in respuestas:
                    if x in Constants.Word_list_COMUNICACIÓN:
                        self.total_score_R1=self.total_score_R1 + 1
                    else:
                        self.total_score_R1=self.total_score_R1
            return self.total_score_R1


    #para R2
    answer_1_R2=models.StringField(blank=True)
    answer_2_R2=models.StringField(blank=True)
    answer_3_R2=models.StringField(blank=True)
    answer_4_R2=models.StringField(blank=True)
    answer_5_R2=models.StringField(blank=True)
    answer_6_R2=models.StringField(blank=True)
    answer_7_R2=models.StringField(blank=True)
    answer_8_R2=models.StringField(blank=True)
    answer_9_R2=models.StringField(blank=True)
    answer_10_R2=models.StringField(blank=True)
    answer_11_R2=models.StringField(blank=True)
    answer_12_R2=models.StringField(blank=True)
    answer_13_R2=models.StringField(blank=True)
    answer_14_R2=models.StringField(blank=True)
    answer_15_R2=models.StringField(blank=True)
    answer_16_R2=models.StringField(blank=True)
    answer_17_R2=models.StringField(blank=True)
    answer_18_R2=models.StringField(blank=True)
    answer_19_R2=models.StringField(blank=True)
    answer_20_R2=models.StringField(blank=True)
    answer_21_R2=models.StringField(blank=True)
    answer_22_R2=models.StringField(blank=True)
    answer_23_R2=models.StringField(blank=True)
    answer_24_R2=models.StringField(blank=True)
    answer_25_R2=models.StringField(blank=True)

    total_score_R2=models.IntegerField(initial=0)

    palabra_pregunta_R2=models.StringField()

    def puntaje_R2(self):    
        
        respuestas = [self.answer_1_R2, self.answer_2_R2, self.answer_3_R2, self.answer_4_R2, self.answer_5_R2, 
        self.answer_6_R2, self.answer_7_R2, self.answer_8_R2, self.answer_9_R2, self.answer_10_R2, self.answer_11_R2, 
        self.answer_12_R2, self.answer_13_R2, self.answer_14_R2, self.answer_15_R2, self.answer_16_R2, self.answer_17_R2, 
        self.answer_18_R2, self.answer_19_R2, self.answer_20_R2, self.answer_21_R2, self.answer_22_R2, self.answer_23_R2, 
        self.answer_24_R2, self.answer_25_R2]

        if self.subsession.mariposa_2 == 'ARGENTINA':
            for x in respuestas:
                    if x in Constants.Word_list_ARGENTINA:
                        self.total_score_R2=self.total_score_R2 + 1
                    else:
                        self.total_score_R2=self.total_score_R2
            return self.total_score_R2  

        if self.subsession.mariposa_2 == 'EXPERIMENTO': 
            for x in respuestas:
                    if x in Constants.Word_list_EXPERIMENTO:
                        self.total_score_R2=self.total_score_R2 + 1
                    else:
                        self.total_score_R2=self.total_score_R2
            return self.total_score_R2 

        if self.subsession.mariposa_2 == 'CABALLITO': 
            for x in respuestas:
                    if x in Constants.Word_list_CABALLITO:
                        self.total_score_R2=self.total_score_R2 + 1
                    else:
                        self.total_score_R2=self.total_score_R2
            return self.total_score_R2 

        if self.subsession.mariposa_2 == 'CASCABELES':
            for x in respuestas:
                    if x in Constants.Word_list_CASCABELES:
                        self.total_score_R2=self.total_score_R2 + 1
                    else:
                        self.total_score_R2=self.total_score_R2
            return self.total_score_R2 

        if self.subsession.mariposa_2 == 'HOLOCAUSTO': 
            for x in respuestas:
                    if x in Constants.Word_list_HOLOCAUSTO:
                        self.total_score_R2=self.total_score_R2 + 1
                    else:
                        self.total_score_R2=self.total_score_R2
            return self.total_score_R2 

        if self.subsession.mariposa_2 == 'ELEFANTES': 
            for x in respuestas:
                    if x in Constants.Word_list_ELEFANTES:
                        self.total_score_R2=self.total_score_R2 + 1
                    else:
                        self.total_score_R2=self.total_score_R2
            return self.total_score_R2 

        if self.subsession.mariposa_2 == 'MANDARINA':
            for x in respuestas:
                    if x in Constants.Word_list_MANDARINA:
                        self.total_score_R2=self.total_score_R2 + 1
                    else:
                        self.total_score_R2=self.total_score_R2
            return self.total_score_R2 

        if self.subsession.mariposa_2 == 'TELEPATÍA':
            for x in respuestas:
                    if x in Constants.Word_list_TELEPATÍA:
                        self.total_score_R2=self.total_score_R2 + 1
                    else:
                        self.total_score_R2=self.total_score_R2
            return self.total_score_R2

        if self.subsession.mariposa_2 == 'COBARDÍA':
            for x in respuestas:
                    if x in Constants.Word_list_COBARDÍA:
                        self.total_score_R2=self.total_score_R2 + 1
                    else:
                        self.total_score_R2=self.total_score_R2
            return self.total_score_R2

        if self.subsession.mariposa_2 == 'COMUNICACIÓN':
            for x in respuestas:
                    if x in Constants.Word_list_COMUNICACIÓN:
                        self.total_score_R2=self.total_score_R2 + 1
                    else:
                        self.total_score_R2=self.total_score_R2
            return self.total_score_R2

    #para R3
    answer_1_R3=models.StringField(blank=True)
    answer_2_R3=models.StringField(blank=True)
    answer_3_R3=models.StringField(blank=True)
    answer_4_R3=models.StringField(blank=True)
    answer_5_R3=models.StringField(blank=True)
    answer_6_R3=models.StringField(blank=True)
    answer_7_R3=models.StringField(blank=True)
    answer_8_R3=models.StringField(blank=True)
    answer_9_R3=models.StringField(blank=True)
    answer_10_R3=models.StringField(blank=True)
    answer_11_R3=models.StringField(blank=True)
    answer_12_R3=models.StringField(blank=True)
    answer_13_R3=models.StringField(blank=True)
    answer_14_R3=models.StringField(blank=True)
    answer_15_R3=models.StringField(blank=True)
    answer_16_R3=models.StringField(blank=True)
    answer_17_R3=models.StringField(blank=True)
    answer_18_R3=models.StringField(blank=True)
    answer_19_R3=models.StringField(blank=True)
    answer_20_R3=models.StringField(blank=True)
    answer_21_R3=models.StringField(blank=True)
    answer_22_R3=models.StringField(blank=True)
    answer_23_R3=models.StringField(blank=True)
    answer_24_R3=models.StringField(blank=True)
    answer_25_R3=models.StringField(blank=True)

    total_score_R3=models.IntegerField(initial=0)

    palabra_pregunta_R3=models.StringField()

    def puntaje_R3(self):    
        
        respuestas = [self.answer_1_R3, self.answer_2_R3, self.answer_3_R3, self.answer_4_R3, self.answer_5_R3, 
        self.answer_6_R3, self.answer_7_R3, self.answer_8_R3, self.answer_9_R3, self.answer_10_R3, self.answer_11_R3, 
        self.answer_12_R3, self.answer_13_R3, self.answer_14_R3, self.answer_15_R3, self.answer_16_R3, self.answer_17_R3, 
        self.answer_18_R3, self.answer_19_R3, self.answer_20_R3, self.answer_21_R3, self.answer_22_R3, self.answer_23_R3, 
        self.answer_24_R3, self.answer_25_R3]

        if self.subsession.mariposa_3 == 'ARGENTINA':
            for x in respuestas:
                    if x in Constants.Word_list_ARGENTINA:
                        self.total_score_R3=self.total_score_R3 + 1
                    else:
                        self.total_score_R3=self.total_score_R3
            return self.total_score_R3  

        if self.subsession.mariposa_3 == 'EXPERIMENTO': 
            for x in respuestas:
                    if x in Constants.Word_list_EXPERIMENTO:
                        self.total_score_R3=self.total_score_R3 + 1
                    else:
                        self.total_score_R3=self.total_score_R3
            return self.total_score_R3

        if self.subsession.mariposa_3 == 'CABALLITO': 
            for x in respuestas:
                    if x in Constants.Word_list_CABALLITO:
                        self.total_score_R3=self.total_score_R3 + 1
                    else:
                        self.total_score_R3=self.total_score_R3
            return self.total_score_R3 

        if self.subsession.mariposa_3 == 'CASCABELES':
            for x in respuestas:
                    if x in Constants.Word_list_CASCABELES:
                        self.total_score_R3=self.total_score_R3 + 1
                    else:
                        self.total_score_R3=self.total_score_R3
            return self.total_score_R3 

        if self.subsession.mariposa_3 == 'HOLOCAUSTO': 
            for x in respuestas:
                    if x in Constants.Word_list_HOLOCAUSTO:
                        self.total_score_R3=self.total_score_R3 + 1
                    else:
                        self.total_score_R3=self.total_score_R3
            return self.total_score_R3 

        if self.subsession.mariposa_3 == 'ELEFANTES': 
            for x in respuestas:
                    if x in Constants.Word_list_ELEFANTES:
                        self.total_score_R3=self.total_score_R3 + 1
                    else:
                        self.total_score_R3=self.total_score_R3
            return self.total_score_R3 

        if self.subsession.mariposa_3 == 'MANDARINA':
            for x in respuestas:
                    if x in Constants.Word_list_MANDARINA:
                        self.total_score_R3=self.total_score_R3 + 1
                    else:
                        self.total_score_R3=self.total_score_R3
            return self.total_score_R3 

        if self.subsession.mariposa_3 == 'TELEPATÍA':
            for x in respuestas:
                    if x in Constants.Word_list_TELEPATÍA:
                        self.total_score_R3=self.total_score_R3 + 1
                    else:
                        self.total_score_R3=self.total_score_R3
            return self.total_score_R3

        if self.subsession.mariposa_3 == 'COBARDÍA':
            for x in respuestas:
                    if x in Constants.Word_list_COBARDÍA:
                        self.total_score_R3=self.total_score_R3 + 1
                    else:
                        self.total_score_R3=self.total_score_R3
            return self.total_score_R3

        if self.subsession.mariposa_3 == 'COMUNICACIÓN':
            for x in respuestas:
                    if x in Constants.Word_list_COMUNICACIÓN:
                        self.total_score_R3=self.total_score_R3 + 1
                    else:
                        self.total_score_R3=self.total_score_R3
            return self.total_score_R3

    #para R4
    answer_1_R4=models.StringField(blank=True)
    answer_2_R4=models.StringField(blank=True)
    answer_3_R4=models.StringField(blank=True)
    answer_4_R4=models.StringField(blank=True)
    answer_5_R4=models.StringField(blank=True)
    answer_6_R4=models.StringField(blank=True)
    answer_7_R4=models.StringField(blank=True)
    answer_8_R4=models.StringField(blank=True)
    answer_9_R4=models.StringField(blank=True)
    answer_10_R4=models.StringField(blank=True)
    answer_11_R4=models.StringField(blank=True)
    answer_12_R4=models.StringField(blank=True)
    answer_13_R4=models.StringField(blank=True)
    answer_14_R4=models.StringField(blank=True)
    answer_15_R4=models.StringField(blank=True)
    answer_16_R4=models.StringField(blank=True)
    answer_17_R4=models.StringField(blank=True)
    answer_18_R4=models.StringField(blank=True)
    answer_19_R4=models.StringField(blank=True)
    answer_20_R4=models.StringField(blank=True)
    answer_21_R4=models.StringField(blank=True)
    answer_22_R4=models.StringField(blank=True)
    answer_23_R4=models.StringField(blank=True)
    answer_24_R4=models.StringField(blank=True)
    answer_25_R4=models.StringField(blank=True)

    total_score_R4=models.IntegerField(initial=0)

    palabra_pregunta_R4=models.StringField()

    def puntaje_R4(self):    
        
        respuestas = [self.answer_1_R4, self.answer_2_R4, self.answer_3_R4, self.answer_4_R4, self.answer_5_R4, 
        self.answer_6_R4, self.answer_7_R4, self.answer_8_R4, self.answer_9_R4, self.answer_10_R4, self.answer_11_R4, 
        self.answer_12_R4, self.answer_13_R4, self.answer_14_R4, self.answer_15_R4, self.answer_16_R4, self.answer_17_R4, 
        self.answer_18_R4, self.answer_19_R4, self.answer_20_R4, self.answer_21_R4, self.answer_22_R4, self.answer_23_R4, 
        self.answer_24_R4, self.answer_25_R4]

        if self.subsession.mariposa_4 == 'ARGENTINA':
            for x in respuestas:
                    if x in Constants.Word_list_ARGENTINA:
                        self.total_score_R4=self.total_score_R4 + 1
                    else:
                        self.total_score_R4=self.total_score_R4
            return self.total_score_R4  

        if self.subsession.mariposa_4 == 'EXPERIMENTO': 
            for x in respuestas:
                    if x in Constants.Word_list_EXPERIMENTO:
                        self.total_score_R4=self.total_score_R4 + 1
                    else:
                        self.total_score_R4=self.total_score_R4
            return self.total_score_R4

        if self.subsession.mariposa_4 == 'CABALLITO': 
            for x in respuestas:
                    if x in Constants.Word_list_CABALLITO:
                        self.total_score_R4=self.total_score_R4 + 1
                    else:
                        self.total_score_R4=self.total_score_R4
            return self.total_score_R4 

        if self.subsession.mariposa_4 == 'CASCABELES':
            for x in respuestas:
                    if x in Constants.Word_list_CASCABELES:
                        self.total_score_R4=self.total_score_R4 + 1
                    else:
                        self.total_score_R4=self.total_score_R4
            return self.total_score_R4

        if self.subsession.mariposa_4 == 'HOLOCAUSTO': 
            for x in respuestas:
                    if x in Constants.Word_list_HOLOCAUSTO:
                        self.total_score_R4=self.total_score_R4 + 1
                    else:
                        self.total_score_R4=self.total_score_R4
            return self.total_score_R4 

        if self.subsession.mariposa_4 == 'ELEFANTES': 
            for x in respuestas:
                    if x in Constants.Word_list_ELEFANTES:
                        self.total_score_R4=self.total_score_R4 + 1
                    else:
                        self.total_score_R4=self.total_score_R4
            return self.total_score_R4 

        if self.subsession.mariposa_4 == 'MANDARINA':
            for x in respuestas:
                    if x in Constants.Word_list_MANDARINA:
                        self.total_score_R4=self.total_score_R4 + 1
                    else:
                        self.total_score_R4=self.total_score_R4
            return self.total_score_R4 

        if self.subsession.mariposa_4 == 'TELEPATÍA':
            for x in respuestas:
                    if x in Constants.Word_list_TELEPATÍA:
                        self.total_score_R4=self.total_score_R4 + 1
                    else:
                        self.total_score_R4=self.total_score_R4
            return self.total_score_R4

        if self.subsession.mariposa_4 == 'COBARDÍA':
            for x in respuestas:
                    if x in Constants.Word_list_COBARDÍA:
                        self.total_score_R4=self.total_score_R4 + 1
                    else:
                        self.total_score_R4=self.total_score_R4
            return self.total_score_R4

        if self.subsession.mariposa_4 == 'COMUNICACIÓN':
            for x in respuestas:
                    if x in Constants.Word_list_COMUNICACIÓN:
                        self.total_score_R4=self.total_score_R4 + 1
                    else:
                        self.total_score_R4=self.total_score_R4
            return self.total_score_R4
    
    pay_1=models.CurrencyField(initial=0)
    pay_2=models.CurrencyField(initial=0)
    pay_3=models.CurrencyField(initial=0)
    pay_4=models.CurrencyField(initial=0)

###REVISAR ID
    def id_code(self):
        abcs=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
        nums=['1','2','3','4','5','6','7','8','9']
        a=random.choice(abcs)
        b=random.choice(abcs)
        c=random.choice(abcs)
        d=random.choice(nums)
        e=random.choice(nums)
        f=random.choice(nums)
        self.participant.label=a+b+c+d+e+f
        self.participant.vars['id_code']=self.participant.label
        return self.participant.label
