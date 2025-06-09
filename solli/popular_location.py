import os
import django
from dbfread import DBF

# Configura o Django para rodar o script standalone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "solli.settings")  # <<< troque "seuprojeto" pelo nome do seu projeto
django.setup()

# Importa o model
from core.models import Location  # ajuste se seu model estiver em outro app ou nome

def popular_location_do_dbf(dbf_path):
    # Abre o DBF
    table = DBF(dbf_path, encoding='utf-8')

    count_created = 0
    count_existing = 0

    for record in table:
        estado = record.get('SIGLA_UF')
        cidade = record.get('NM_MUN')

        if not estado or not cidade:
            continue  # pula se faltar dado

        location, created = Location.objects.get_or_create(
            estate=estado,
            city=cidade
        )

        if created:
            count_created += 1
            print(f"Criado: {location}")
        else:
            count_existing += 1
            print(f"Já existente: {location}")

    print(f"Total criado: {count_created}")
    print(f"Total já existentes: {count_existing}")

if __name__ == "__main__":
    caminho_arquivo_dbf = r"C:\learning\ufrpe\ihm\projeto\BR_Municipios_2024\BR_Municipios_2024.dbf"  # <<< coloque o caminho correto
    popular_location_do_dbf(caminho_arquivo_dbf)
