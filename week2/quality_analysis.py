import numpy as np
import matplotlib.pyplot as plt

# 1. Define the categories and ratings
labels = ['Functional', 'Performance', 'Compatibility', 'Usability', 
          'Reliability', 'Security', 'Maintainability', 'Portability']
spotify = [5, 4, 5, 4, 4, 4, 4, 5]
yt_music = [4, 4, 5, 4, 4, 4, 5, 5]

# 2. Setup the radar chart angles
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1] # Close the circle
spotify += spotify[:1]
yt_music += yt_music[:1]

# 3. Create the plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw the axes and labels
plt.xticks(angles[:-1], labels)
ax.set_rlabel_position(0)
plt.yticks([1,2,3,4,5], ["1","2","3","4","5"], color="grey", size=8)
plt.ylim(0,5)

# 4. Plot the data
ax.plot(angles, spotify, color='green', linewidth=2, label='Spotify')
ax.fill(angles, spotify, color='green', alpha=0.25)
ax.plot(angles, yt_music, color='red', linewidth=2, label='YouTube Music')
ax.fill(angles, yt_music, color='red', alpha=0.25)

plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()
