import pandas as pd
import matplotlib.pyplot as plt
import json

with open('data/data.json', 'r') as f:
    data = json.load(f)

columns = [
    "extra", "civility", "lastname", "firstname", "middle", 
    "address", "zip", "city", "canton", "email"
]

df = pd.DataFrame(data["data"], columns=columns)

fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(2, 2)

ax1 = fig.add_subplot(gs[0,1])
df["civility"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", ax=ax1, startangle=90, 
    colors=["#66b3ff","#ff9999"]
)
ax1.set_title("Gender Distribution")
ax1.set_ylabel("")

ax2 = fig.add_subplot(gs[1,1])
canton_counts = df["canton"].value_counts()
bars = ax2.bar(canton_counts.index, canton_counts, color="lightgreen", edgecolor="black")
ax2.set_title("Distribution by Canton")
ax2.set_xlabel("Canton")
ax2.set_ylabel("Count")
ax2.bar_label(bars, labels=canton_counts, padding=2)

ax3 = fig.add_subplot(gs[:,0])
city_counts = df["city"].value_counts().head(50)
bars = df["city"].value_counts().head(50).plot(
    kind="barh", ax=ax3, color="skyblue", edgecolor="black"
)
bars = ax3.barh(city_counts.index, city_counts, color="skyblue")
ax3.set_title("Top 50 Cities")
ax3.set_xlabel("Count")
ax3.set_ylabel("City")
ax3.bar_label(bars, labels=city_counts, padding=2)

# Adjust layout
plt.tight_layout()
plt.show()