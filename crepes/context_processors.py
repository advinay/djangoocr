from datetime import datetime

def get_infos(request):
    date_actuelle = datetime.now()
    return {'date_actuelle': date_actuelle}


def inject_constantes(request):
	return {'taux_change': 1.41}

def inject_taux_change(request):
	return {'taux_change': 1.618033989}