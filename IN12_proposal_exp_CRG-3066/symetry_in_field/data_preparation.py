import pandas as pd

def prepare(data1, data2):
    path = "IN12_proposal_exp_CRG-3066/rawdata"
    metadata = []
    with open(f"{path}/075{data1}","r") as txt:
        for line in txt.readlines():
            line = line.strip()
            if line == "DATA_:":
                metadata.append(line)
                break
            metadata.append(line)

    names = ["PNT", "QH", "QK", "QL", "EN", "M1", "TIME", "CNTS", "A2", "A3", "A3P", "A4", "KI", "KF", "RMH", "RA", "TT", "TRT", "MAG"]
    panda1 = pd.read_csv(f"{path}/075{data1}", sep="     ", skiprows=50, names=names, engine='python')
    panda2 = pd.read_csv(f"{path}/075{data2}", sep="     ", skiprows=50, names=names, engine='python')

    with open(f"{path}/new_075{data1}", "w") as txt:
        for line in metadata:
            txt.write(f"{line}\n")
        for i in range(len(panda1["PNT"])):
            if i == 0:
                txt.write(f"{panda1['PNT'][i]}    {panda1['QH'][i]}    {panda1['QK'][i]}    {panda1['QL'][i]}    {panda1['EN'][i]}    {panda1['M1'][i]}    {panda1['TIME'][i]}    {panda1['CNTS'][i]}    {panda1['A2'][i]}    {panda1['A3'][i]}    {panda1['A3P'][i]}    {panda1['A4'][i]}    {panda1['KI'][i]}    {panda1['KF'][i]}    {panda1['RMH'][i]}    {panda1['RA'][i]}    {panda1['TT'][i]}    {panda1['TRT'][i]}    {panda1['MAG'][i]}\n")
            else:
                txt.write(f"{panda1['PNT'][i]}    {panda1['QH'][i]}    {panda1['QK'][i]}    {panda1['QL'][i]}    {panda1['EN'][i]}    {panda1['M1'][i]}    {panda1['TIME'][i]}    {panda1['CNTS'][i]}    {panda1['A2'][i]}    {panda1['A3'][i]}    {panda1['A3P'][i]}    {panda1['A4'][i]}\n")
        for i in range(len(panda2["PNT"])):
            if i == 0:
                pass
            else:
                txt.write(f"{panda2['PNT'][i]}    {panda2['QH'][i]}    {panda2['QK'][i]}    {panda2['QL'][i]}    {panda2['EN'][i]}    {panda2['M1'][i]}    {panda2['TIME'][i]}    {panda2['CNTS'][i]}    {panda2['A2'][i]}    {panda2['A3'][i]}    {panda2['A3P'][i]}    {panda2['A4'][i]}\n")

if __name__ == "__main__":

    prepare(265, 256)

