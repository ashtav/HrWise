import pandas as pd

# Menghitung skor karyawan
# Mmenentukan bobot untuk masing-masing kriteria evaluasi
bobot_produktivitas = 0.4
bobot_kehadiran = 0.3
bobot_evaluasi = 0.3


class EmployeeAssessment:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def calculate_score(self):
        self.data['Skor'] = (
                bobot_produktivitas * self.data['Produktivitas'] +
                bobot_kehadiran * self.data['Kehadiran (%)'] +
                bobot_evaluasi * (self.data['Evaluasi Kinerja'].map({'Kurang': 0, 'Cukup': 1, 'Baik': 2}))
        )
        return self.data

    def calculate_rank(self):
        self.data = self.data.sort_values('Skor', ascending=False).reset_index(drop=True)
        self.data['Peringkat'] = self.data.index + 1
        self.data['Skor'] = self.data['Skor'].round(2)
        return self.data

    def get_result(self):
        self.calculate_score()
        self.calculate_rank()
        result = self.data[['Nama Karyawan', 'Skor', 'Peringkat']]

        result = result.rename(columns={
            'Nama Karyawan': 'name',
            'Skor': 'score',
            'Peringkat': 'rate'
        })

        return result
