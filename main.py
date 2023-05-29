import pandas as pd
import matplotlib.pyplot as plt

# read Excel file from data
df = pd.read_excel('data/Employee.xlsx')

# df_subset = df.drop(columns=['No'])
#
# ax = df_subset.plot.bar()
#
# ax.set_xticklabels(df['Nama Karyawan'], rotation=45, ha='right')
#
# plt.show()

# Menghitung skor karyawan
# Anda dapat menentukan bobot untuk masing-masing kriteria evaluasi
bobot_produktivitas = 0.4
bobot_kehadiran = 0.3
bobot_evaluasi = 0.3

df['Skor'] = (
    bobot_produktivitas * df['Produktivitas'] +
    bobot_kehadiran * df['Kehadiran'] +
    bobot_evaluasi * (df['Evaluasi Kinerja'].map({'Kurang': 0, 'Cukup': 1, 'Baik': 2}))
)

# Melakukan peringkat karyawan berdasarkan skor
df = df.sort_values('Skor', ascending=False).reset_index(drop=True)
df['Peringkat'] = df.index + 1

# Menampilkan hasil
print(df[['Nama Karyawan', 'Skor', 'Peringkat']])

# ax = df[['Nama Karyawan', 'Skor', 'Peringkat']].plot.bar()
# ax.set_xticklabels(df['Nama Karyawan'], rotation=45, ha='right')
# plt.show()