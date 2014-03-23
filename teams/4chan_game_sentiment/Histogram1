import numpy as np
import matplotlib.pyplot as plt

with open('4chandata.txt', 'r') as f:
    avg = [float(line.strip()) for line in f]
print avg

with open('4chandata.txt', 'r') as f:
    avg = [float(line.strip()) for line in f]
print avg

meta_score, user_score = [], []
with open('metacritic_score_list.txt', 'r') as f:
	meta_score = [float(line.split()[2]) for line in f]
	user_score = [line.split()[3] for line in f]
	release = [line.split()[2] for line in f]

n_groups = 10




fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, avg, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=release,
                 error_kw=error_config,
                 label='4chan')

rects2 = plt.bar(index + bar_width, meta_score, bar_width,
                 alpha=opacity,
                 color='r',
                 yerr=release,
                 error_kw=error_config,
                 label='Metascore')


plt.xlabel('Release Date')
plt.ylabel('Score')
plt.title('Scores by release date and genre')
plt.xticks(index + bar_width, ('Bio', 'SP', 'H:A', 'MGSV', 'Dis', 'DD', 'FC3', 'W2', 'DS', 'MP3', 'MGSR'))
plt.legend()

plt.tight_layout()
plt.show()
