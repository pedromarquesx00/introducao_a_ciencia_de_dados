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
chuvas = ["Chuva01","Chuva02","Chuva03","Chuva04",
          "Chuva05","Chuva06","Chuva07","Chuva08",
          "Chuva09","Chuva10","Chuva11","Chuva12",
          "Chuva13","Chuva14","Chuva15","Chuva16",
          "Chuva17","Chuva18","Chuva19","Chuva20",
          "Chuva21","Chuva22","Chuva23","Chuva24",
          "Chuva25","Chuva26","Chuva27","Chuva28",
          "Chuva29","Chuva30","Chuva31"]

# %%
df_melt = df.melt(id_vars=["Data","NivelConsistencia"],
                  value_vars=chuvas,
                  var_name="Chuvas",
                  value_name="QtdeChuva")

# %%
dias = df_melt["Chuvas"].str[-2:].astype(int) - 1

df_melt["Data_Efetiva"] = df_melt["Data"] + pd.to_timedelta(dias, unit='D')

df_melt["Ano"] = df_melt["Data_Efetiva"].dt.year
df_melt["Mes"] = df_melt["Data_Efetiva"].dt.month

# %%
df_anual = (df_melt.groupby("Ano")
            .agg({"QtdeChuva":"sum"})
            .reset_index())

# %%
df_mensal = (df_melt.groupby(["Mes","Ano"])["QtdeChuva"]
          .sum()
          .reset_index())

# %%
px.bar(df,x="Data",y="Total")
# %%
plt.figure(figsize=(12,8))
plt.title("Boxplot dos dados de chuvas anuais")
sns.boxplot(df_mensal,x="Ano",y="QtdeChuva")
plt.tick_params(axis="x",labelrotation=45)
plt.xlabel("Anos")
plt.ylabel("Quantidade de Chuva (Em Milímetros)")

#plt.savefig("boxplot_anual", dpi=300)

# %%
plt.title("Boxplot dos dados de chuvas mensais")
sns.boxplot(df_mensal,x="Mes",y="QtdeChuva")
plt.xlabel("Meses")
plt.ylabel("Quantidade de Chuva (Em Milímetros)")

#plt.savefig("boxplot_mensal", dpi=300)