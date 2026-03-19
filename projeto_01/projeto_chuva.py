# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# %%
df = pd.read_csv("../data/chuvas_er.csv", sep=";")
df.head()

# %%
df["Data"] = pd.to_datetime(df["Data"],dayfirst=True)
df["Total"] = df["Total"].str.replace(",",".").astype(float)
df["Maxima"] = df["Maxima"].str.replace(",",".").astype(float)
df["Chuva01"] = df["Chuva01"].str.replace(",",".").astype(float)
df["Chuva02"] = df["Chuva02"].str.replace(",",".").astype(float)
df["Chuva03"] = df["Chuva03"].str.replace(",",".").astype(float)
df["Chuva04"] = df["Chuva04"].str.replace(",",".").astype(float)
df["Chuva05"] = df["Chuva05"].str.replace(",",".").astype(float)
df["Chuva06"] = df["Chuva06"].str.replace(",",".").astype(float)
df["Chuva07"] = df["Chuva07"].str.replace(",",".").astype(float)
df["Chuva08"] = df["Chuva08"].str.replace(",",".").astype(float)
df["Chuva09"] = df["Chuva09"].str.replace(",",".").astype(float)
df["Chuva10"] = df["Chuva10"].str.replace(",",".").astype(float)
df["Chuva11"] = df["Chuva11"].str.replace(",",".").astype(float)
df["Chuva12"] = df["Chuva12"].str.replace(",",".").astype(float)
df["Chuva13"] = df["Chuva13"].str.replace(",",".").astype(float)
df["Chuva14"] = df["Chuva14"].str.replace(",",".").astype(float)
df["Chuva15"] = df["Chuva15"].str.replace(",",".").astype(float)
df["Chuva16"] = df["Chuva16"].str.replace(",",".").astype(float)
df["Chuva17"] = df["Chuva17"].str.replace(",",".").astype(float)
df["Chuva18"] = df["Chuva18"].str.replace(",",".").astype(float)
df["Chuva19"] = df["Chuva19"].str.replace(",",".").astype(float)
df["Chuva20"] = df["Chuva20"].str.replace(",",".").astype(float)
df["Chuva21"] = df["Chuva21"].str.replace(",",".").astype(float)
df["Chuva22"] = df["Chuva22"].str.replace(",",".").astype(float)
df["Chuva23"] = df["Chuva23"].str.replace(",",".").astype(float)
df["Chuva24"] = df["Chuva24"].str.replace(",",".").astype(float)
df["Chuva25"] = df["Chuva25"].str.replace(",",".").astype(float)
df["Chuva26"] = df["Chuva26"].str.replace(",",".").astype(float)
df["Chuva27"] = df["Chuva27"].str.replace(",",".").astype(float)
df["Chuva28"] = df["Chuva28"].str.replace(",",".").astype(float)
df["Chuva29"] = df["Chuva29"].str.replace(",",".").astype(float)
df["Chuva30"] = df["Chuva30"].str.replace(",",".").astype(float)
df["Chuva31"] = df["Chuva31"].str.replace(",",".").astype(float)

# %%
df.head()
# %%
df["Maxima"].describe()

# %%
df.head()
# %%
px.bar(df,x="Data",y="Maxima")
# %%

# %%
chuvas = ["Chuva01","Chuva02","Chuva03","Chuva04",
          "Chuva05","Chuva06","Chuva07","Chuva08",
          "Chuva09","Chuva10","Chuva11","Chuva12",
          "Chuva13","Chuva14","Chuva15","Chuva16",
          "Chuva17","Chuva18","Chuva19","Chuva20",
          "Chuva21","Chuva22","Chuva23","Chuva24",
          "Chuva25","Chuva26","Chuva27","Chuva28",
          "Chuva29","Chuva30","Chuva31"]
# %%
# %%
df_melt = df.melt(id_vars=["Data","NivelConsistencia"],
                  value_vars=chuvas,
                  ar_name="Chuvas",
                  value_name="QtdeChuva")

# %%
df_melt
# %%
df_tratado = df_melt[["Data","NivelConsistencia","QtdeChuva"]]

# %%
df_tratado.head()

# %%
df_mes = df_tratado.groupby(pd.Grouper(key="Data",freq="MS")).max()
# %%
px.line(df_mes,y="QtdeChuva")

# %%
df_mes1 = df_tratado.query("Data.dt.month == 1").groupby(df_tratado["Data"].dt.year).max()

# %%

# %%
df_mes1.head()
# %% Grafico com plotly
px.line(df_mes1,
        y="QtdeChuva",
        title="Chuvas de Janeiro",
        labels={
            "QtdeChuva":"Quatidade de chuva",
            "index":"Anos"
        })
#sns.lineplot(df_mes1,x="Data",y="QtdeChuva",marker="o")
#plt.xticks(rotation=60)
#plt.title("Chuvas de Janeiro")
#plt.ylabel("Quantidade de chuvas")
#plt.show()

# %%
