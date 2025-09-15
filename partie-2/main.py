import logging
import time

from generators.bulletin import BulletinGenerator
from generators.rapport_anomalies import RapportAnomaliesGenerator
from interface import PsyelAPIInterface
from settings import settings

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def start() -> tuple[str, ...]:
    """
    Point d’entrée principal qui exécute les trois étapes ETL pour chaque sortie attendue :
        Extraction : Chargement des données depuis l’API
        Transformation : Nettoyage des données et préparation du format final
        Chargement : Export des données dans le format approprié (CSV ou JSON)

    :returns Chemins des fichiers CSV/JSON générés, en l’occurrence :
        - un CSV pour les « bulletins par étudiant »
        - un JSON pour le « rapport d’anomalies »
    """
    logging.info("Start")
    psyel_api = PsyelAPIInterface()
    bulletin_generator = BulletinGenerator(psyel_api)
    # Générer les bulletins
    bulletin_generator.run()

    logging.info(
        f"Bulletin généré avec succès sous le path {settings.BULLETIN_OUTPUT_PATH}"
    )
    # Générer le rapport d'anomalies
    RapportAnomaliesGenerator(bulletin_generator).run()

    logging.info(
        f"Rapport d'anomalies généré avec succès sous le path {settings.RAPPORT_ANOMALIES_OUTPUT_PATH}"
    )

    logging.info("End")


if __name__ == "__main__":
    start()

    while True:
        time.sleep(60)
