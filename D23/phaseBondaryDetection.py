import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def findSignal(i_start: int, i_stop: int, i_exclude: list[int] = [], directory: str = None,  height: int = 45, distance: int = 50) -> dict:
    ret = {}
    temperature = []
    for i in range(i_start, i_stop+1):
        if i in i_exclude:
            continue
        df = pd.read_csv(f"{directory}/0{i}.txt", names=["QH", "QK", "QL", "CNTS", "1", "2", "3", "4", "5", "6", "T", "H", "7"], sep=",", dtype=np.float64)
        temperature.append(float(df["T"][0]))
        peaks, _ = find_peaks(df["CNTS"], height=height, distance=distance)
        ql_peaks = []        
        for point in peaks:
            ql_peaks.append(df["QL"][point])
        ret[df["H"][0]] = ql_peaks
        tolerance = 0.1
        all_close = np.allclose(temperature, temperature[0], rtol=0, atol=tolerance)
    if all_close:
        temp = temperature[0]
    else:
        print(temperature)
        temp = round(sum(temperature)/len(temperature), 2)
    ret["temp"] = temp
    return ret

def getPhaseBondary(data: dict, directory: str = None, save: bool = False, delta: float = 0.06) -> list[list[float]]:
    points_to_save = []
    prev_len = None
    prev_field = 0
    prev_peaks = []
    for field, peaks in data.items():
        print(field, peaks)
        if field == "temp":
            continue
        if len(peaks) != prev_len and prev_len is not None:
            print("New phase detected, different number of peaks")
            points_to_save.append([data["temp"], round((field+prev_field)/2, 2)])
        elif len(peaks) == prev_len and prev_peaks != []: #tady to bude slozitejsi
            print(peaks, prev_peaks)
            peaks = sorted(peaks)
            for i in range(len(peaks)):
                if abs(prev_peaks[i] - peaks[i]) > delta:
                    print("New phase detected, same peaks")
                    points_to_save.append([data["temp"], round((field+prev_field)/2, 2)])
                    break
        prev_len = len(peaks)
        prev_field = field
        prev_peaks = sorted(peaks)

    if save:
        with open(f"{directory}/transition{data['temp']}.txt", "w") as txt:
            txt.write("T (K), H (T)\n")
            for point in points_to_save:
                txt.write(f"{point[0]},{point[1]}")

    return points_to_save





if __name__ == "__main__":
    data = findSignal(90117, 90135, directory="D23/H_along_ab/1200mK", height=70, distance=30)
    print(getPhaseBondary(data, delta=0.05))