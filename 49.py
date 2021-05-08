from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

allergenek = ["gluten", "peanuts", "tree nuts", "celery", "mustard", "eggs", "milk", "sesame", "fish", "crustaceans",
              "molluscs", "soya", "sulphites", "lupin"]
allergia = list(map(str, input("Mely allergénekre allergiás?(Több válasz esetén vesszővel elválasztva) ").split(",")))
print(allergia)
fin = open("input.txt", "r")
data = fin.read()

gluten = data.count("gluten")
peanuts = data.count("peanuts")
treenuts = data.count("tree nuts")
celery = data.count("celery")
mustard = data.count("mustard")
eggs = data.count("eggs")
milk = data.count("milk")
sesame = data.count("sesame")
fish = data.count("fish")
crustaceans = data.count("crustaceans")
molluscs = data.count("molluscs")
soya = data.count("soya")
sulphites = data.count("sulphites")
lupin = data.count("lupin")


indexes = [gluten, peanuts, treenuts, celery, mustard, eggs, milk, sesame, fish, crustaceans, molluscs, soya,
           sulphites, lupin]
x = np.arange(len(allergenek))
width = 0.35

fig, ax = plt.subplots()
rects = ax.bar(x, indexes, width, label="Allergének száma")
ax.set_ylabel("Előfordulások száma")
ax.set_title("Allergének az összetevőkben")
ax.set_xticks(x)
ax.set_xticklabels(allergenek)
ax.legend()

ax.bar_label(rects, padding=1)

fig.tight_layout()
plt.show()




