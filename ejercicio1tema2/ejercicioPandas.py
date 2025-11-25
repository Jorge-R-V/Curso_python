import pandas as pd

serie1 = pd.Series([1,2,3])
serie1.name = "primeros"

df1 = pd.DataFrame({"columna1":[3,2,5,4,1], "columna2": ["a","b","c","d","e"], "columna3":["?","!","#","@","&"]})
print (df1.head())

df2 = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
print (df2.head())

print (df2.size)
print (df2.shape)

print (df2.tail(7)) #Enseña los ultimos que marques de base son 5 

df2.columns = ["largo_sepalo","ancho_sepalo","largo_petalo","ancho_petalo","especie"]
print(df2.head())

df2.memory_usage().sum()