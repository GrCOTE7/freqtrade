# F:\freqtrade\user_data\paris_formatter.py
import logging
from datetime import datetime
from zoneinfo import ZoneInfo


class ParisTimeFormatter(logging.Formatter):
    """Formateur qui force l'affichage de l'heure de Paris."""

    def formatTime(self, record, datefmt=None):
        # Convertit le timestamp du log en heure de Paris
        dt = datetime.fromtimestamp(record.created, tz=ZoneInfo("Europe/Paris"))
        if datefmt:
            return dt.strftime(datefmt)
        return dt.isoformat()
