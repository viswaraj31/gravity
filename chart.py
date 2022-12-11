import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sorted_final.csv")
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
gravity = df["gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(radius,mass)
plt.title("radius-mass")
plt.xlabel("radius")
plt.ylabel("mass")
plt.show()

plt.plot(mass,gravity)
plt.title("mass-gravity")
plt.xlabel("mass")
plt.ylabel("gravity")
plt.show()