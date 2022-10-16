import csv
from typing import List
from ..models import ThesisCommittee, ThesisDefense
from ..serializers_csv import ThesisCommitteeSerializerCSV, ThesisDefenseSerializerCSV


class TC_CSV_GENERATOR():
    def __init__(self, file_dir, model_name) -> None:
        self.csv_dir = file_dir
        self.model_name = model_name

    def generate_csv(self):

        if self.model_name == 'ThesisCommittees':
            queryset = ThesisCommittee.objects.all()
            data = [
                ThesisCommitteeSerializerCSV(thesis_committee).data
                for thesis_committee in queryset]

            fieldnames = ['Estudiantes', 'Tesis', 'Tutor(es)',
                          'Presidente', 'Secretario', 'Oponente', 'Palabras Claves']

            rows: List[dict] = []
            for thesis_committee in data:
                row: dict = {}
                row['Estudiantes'] = thesis_committee['thesis']['student']
                row['Tutor(es)'] = ", ".join(
                    thesis_committee['thesis']['tutors'])
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

        elif self.model_name == 'ThesisDefenses':
            queryset = ThesisDefense.objects.all()
            data = [
                ThesisDefenseSerializerCSV(thesis_defense).data
                for thesis_defense in queryset]

            fieldnames = ['Fecha', 'Hora', 'Lugar',  'Estudiantes', 'Tesis', 'Tutor(es)',
                          'Presidente', 'Secretario', 'Oponente', 'Palabras Claves']

            rows: List[dict] = []
            for thesis_defense in data:
                row: dict = {}
                row['Fecha'] = thesis_defense['date']
                row['Hora'] = thesis_defense['time']
                row['Lugar'] = thesis_defense['place']['name']
                row['Estudiantes'] = thesis_defense['thesis_committee']['student']
                row['Tutor(es)'] = ", ".join(
                    thesis_defense['thesis_committee']['tutors'])
                row['Tesis'] = thesis_defense['thesis_committee']['thesis_title']
                row['Palabras Claves'] = "\n".join(
                    thesis_defense['thesis_committee']['keywords'])
                row['Presidente'] = thesis_defense['thesis_committee']['president']
                row['Oponente'] = thesis_defense['thesis_committee']['opponent']
                row['Secretario'] = thesis_defense['thesis_committee']['secretary']
                rows.append(row)

        with open(self.csv_dir, 'w', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
