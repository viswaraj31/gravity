import pandas as pd

df = pd.read_csv("final_data.csv")

df.drop(['Unnamed: 0'],axis = 1,inplace = True)
df.reset_index(drop = True,inplace=True)

df["Mass"] = df["Mass"].astype(float)
df["Radius"] = df["Radius"].apply(lambda x : x.replace(",","")).astype(float)

mass = df["Mass"].to_list()
radi = df["Radius"].to_list()

for i in range(0,len(mass) -1):
    radi[i] = radi[i] * 6.957e+8
    mass[i] = mass[i] * 1.989e+30

gravity = []

for i in range(0,len(mass)) :
    grav = (6.67e-11) * (mass[i])/(radi[i]**2)
    gravity.append(grav)

df["gravity"] = gravity

df.to_csv("sorted_final.csv")