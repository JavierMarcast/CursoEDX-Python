import pandas as pd 
"Importar datos a python"
url= "imports-85.csv"
df = pd.read_csv(url, header = None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length"," width","height", 
"curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg", "price","",""]
df.columns=headers


print(df)

"guardar"
df.to_csv(url)

"Tipos de datos"
df.dtypes