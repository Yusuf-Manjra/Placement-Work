import pandas as pd

df = pd.read_csv('/home/ymanjra/traccc-projects/traccc/data/HTTSim_ATLAS_ITK/event000000000-cells-mod.csv')
linesToRemove = []

for line in range(len(df)):
    row = df.iloc[line].to_numpy()
    if (str(row[0]).__contains__("1657")):
        linesToRemove.append(line)
        
df= df.drop(linesToRemove)
print(len(df))

df.to_csv('/home/ymanjra/traccc-projects/traccc/data/HTTSim_ATLAS_ITK/event000000000-cells-mod-2.csv',index=False)