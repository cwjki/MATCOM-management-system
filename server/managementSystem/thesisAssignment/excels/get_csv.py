import csv
from typing import List
from ..models import ThesisCommittee
from ..serializers_csv import ThesisCommitteeSerializerCSV


class TC_CSV_GENERATOR():
    def __init__(self, file_dir) -> None:
        self.csv_dir = file_dir

    def generate_csv(self):
        queryset = ThesisCommittee.objects.all()
        data = [
            ThesisCommitteeSerializerCSV(thesis_committee).data
            for thesis_committee in queryset]

        fieldnames = ['Día', 'Hora', 'Lugar', 'Estudiantes', 'Tutor(es)',
                      'Presidente', 'Secretario', 'Oponente', 'Tesis', 'Palabras Claves']

        rows: List[dict] = []
        for thesis_committee in data:
            row: dict = {}
            row['Día'] = thesis_committee['date']
            row['Hora'] = thesis_committee['time']
            row['Lugar'] = thesis_committee['place']['name']
            row['Estudiantes'] = thesis_committee['thesis']['student']
            row['Tutor(es)'] = ", ".join(thesis_committee['thesis']['tutors'])
            row['Tesis'] = thesis_committee['thesis']['title']
            row['Palabras Claves'] = ", ".join(
                thesis_committee['thesis']['keywords'])
            row['Presidente'] = thesis_committee['president']['name'] + \
                ' ' + thesis_committee['president']['last_name']
            row['Oponente'] = thesis_committee['opponent']['name'] + \
                ' ' + thesis_committee['opponent']['last_name']
            row['Secretario'] = thesis_committee['secretary']['name'] + \
                ' ' + thesis_committee['secretary']['last_name']
            rows.append(row)

        with open(self.csv_dir, 'w', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
