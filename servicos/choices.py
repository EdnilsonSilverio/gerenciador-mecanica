from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):

    TROCAR_VALVULA_MOTOR = 'TVM', 'Trocar a válvula do motor'
    TROCAR_OLEO = 'TO', 'Troca de óleo'
    BALANCEAMENTO = 'B', 'Balanceamento'
    TROCAR_FREIOS = 'TF', 'Troca de freios'
    TROCAR_BATERIA = 'TB', 'Troca de bateria'
    TROCAR_PASTILHAS_FREIO = 'TPF', 'Troca de pastilhas de freio'
    ALINHAMENTO = 'A', 'Alinhamento'
    TROCAR_AMORTECEDORES = 'TA', 'Troca de amortecedores'
    TROCAR_FILTRO_AR = 'TFA', 'Troca de filtro de ar'
    TROCAR_FILTRO_OLEO = 'TFO', 'Troca de filtro de óleo'
    REPARAR_CAIXA_DE_CAMBIO = 'RCC', 'Reparar caixa de câmbio'
    TROCAR_CORREIA_DISTRIBUICAO = 'TCD', 'Troca de correia de distribuição'
    REPARAR_SUSPENSAO = 'RS', 'Reparar suspensão'
    TROCAR_BUJIAS = 'TBU', 'Troca de velas de ignição'
    TROCAR_FILTRO_COMBUSTIVEL = 'TFC', 'Troca de filtro de combustível'
