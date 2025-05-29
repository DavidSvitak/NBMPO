import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
from scipy.interpolate import griddata

def prepare(file:str, directory: str = None):
    name = file.replace(".dat", ".txt")
    to_save = []
    with open(f"D23/rawdata/{file}", "r") as txt_read:
        for line in txt_read:
            numbers = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            to_save.append(numbers)

    if directory is None:
        with open(f"field_scans/{name}", "w") as txt:
            for line in to_save:
                for num in line:
                    txt.write(f"{float(num)},")
                txt.write("\n")
    else:
        with open(f"{directory}/{name}", "w") as txt:
            for line in to_save:
                for num in line:
                    txt.write(f"{float(num)},")
                txt.write("\n")

def make_map(i_start: int, i_stop: int, i_exclude: list[int] = [], title: str = "", x_label: str = "", y_axis: str = "", z_axis: str = "", directory: str = None) -> None:
    
    for i in range(i_start, i_stop+1):
        if i in i_exclude:
            continue
        file = f"0{i}.dat"
        prepare(file, directory=directory)
    
    x_data = np.array([])
    z_data = np.array([])
    y_data = np.array([])
    temperature = []

    for i in range(i_start, i_stop+1):
        if i in i_exclude:
            continue
        df = pd.read_csv(f"{directory}/0{i}.txt", names=["QH", "QK", "QL", "CNTS", "1", "2", "3", "4", "5", "6", "T", "H", "7"], sep=",", dtype=np.float64)
        x_data = np.append(x_data, df["QL"])
        z_data = np.append(z_data, df["CNTS"])
        y_data = np.append(y_data, df["H"])
        temperature.append(float(df["T"][0]))

    xi = np.linspace(x_data.min(), x_data.max(), 300)
    yi = np.linspace(y_data.min(), y_data.max(), 300)
    X, Y = np.meshgrid(xi, yi)

    # 2. Interpolate z_data onto the grid
    Z = griddata((x_data, y_data), z_data, (X, Y), method='cubic')  # 'linear' or 'nearest' are alternatives
    plt.clf()
    # 3. Plot as an image
    im = plt.imshow(Z, extent=(xi.min(), xi.max(), yi.min(), yi.max()), origin='lower',
                cmap='viridis', aspect='auto')
    plt.colorbar(im, label=f"{z_axis}")
    
    tolerance = 0.1
    all_close = np.allclose(temperature, temperature[0], rtol=0, atol=tolerance)
    if all_close:
        title = title.replace("{temp}", str(temperature[0]))
    else:
        print(temperature)
        title = title.replace("{temp}", str(round(sum(temperature)/len(temperature), 2)))
    plt.title(f"{title}")
    plt.xlabel(f"{x_label}")
    plt.ylabel(f"{y_axis}")
    plt.savefig(f"{directory}/{title.strip()}.png")


if __name__ == "__main__":
    make_map(89766, 89792, i_exclude=[88884], directory="D23/900mK", title="Scan at temperature {temp} K", x_label="(1/3, 1/3, QL)", y_axis="H (T)", z_axis="Intensity (a.u.)")