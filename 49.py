from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

allergenek = ["gluten", "peanuts", "tree nuts", "celery", "mustard", "eggs", "milk", "sesame", "fish", "crustaceans",
              "molluscs", "soya", "sulphites", "lupin"]
allergia = list(map(str, input("Mely allergénekre allergiás?(Több válasz esetén szóközzel elválasztva) ").split()))
# print(allergia)
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


ertekek = [gluten, peanuts, treenuts, celery, mustard, eggs, milk, sesame, fish, crustaceans, molluscs, soya,
           sulphites, lupin]
x = np.arange(len(allergenek))
width = 0.35

fig, ax = plt.subplots()
rects = ax.bar(x, ertekek, width, label="Allergének száma",color="b")
rects2 = ax.bar(x, ertekek, width, label="Válaszott allergének",color="r")
barlist = plt.bar(x, ertekek,color="b" )
if "gluten" in allergia:
    barlist[0].set_color("r")
if "penauts" in allergia:
    barlist[1].set_color("r")
if "tree nuts" in allergia:
    barlist[2].set_color("r")
if "celery" in allergia:
    barlist[3].set_color("r")
if "mustard" in allergia:
    barlist[4].set_color("r")
if "eggs" in allergia:
    barlist[5].set_color("r")
if "milk" in allergia:
    barlist[6].set_color("r")
if "sesame" in allergia:
    barlist[7].set_color("r")
if "fish" in allergia:
    barlist[8].set_color("r")
if "crustaceans" in allergia:
    barlist[9].set_color("r")
if "molluscs" in allergia:
    barlist[10].set_color("r")
if "soya" in allergia:
    barlist[11].set_color("r")
if "sulphites" in allergia:
    barlist[12].set_color("r")
if "lupin" in allergia:
    barlist[13].set_color("r")
ax.set_ylabel("Előfordulások száma")
ax.set_title("Allergének az összetevőkben")
ax.set_xticks(x)
ax.set_xticklabels(allergenek)
ax.legend()

ax.bar_label(rects)

fig.tight_layout()
plt.show()




