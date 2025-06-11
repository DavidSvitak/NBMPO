import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("cp/along_ab.txt", names=["T","B(Oe)","B","Cp"],  )

x_data = []
y_data = []

i = 1
while float(df["B"][i]) < 0.1:
    x_data.append(float(df["T"][i]))
    y_data.append(float(df["Cp"][i]))
    i += 1

plt.plot(x_data, y_data, "ro", label = "Zero magnetic field measuremen")
plt.xlabel("T (K)")
plt.text(1.11, 71, r"T$_{N1}$")
plt.text(1.265, 51.5, r"T$_{N2}$")
plt.ylim(0,75)
plt.ylabel(r"C$_{p}$ ($\mu $J$\cdot$K$^{-1}$)")
plt.legend(loc='upper left')
plt.savefig("cp/Heat_capacity_zero_field.png")