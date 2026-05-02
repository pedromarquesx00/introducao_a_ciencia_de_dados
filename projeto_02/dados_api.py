# %% Bibliotecas usadas
import requests
import pandas as pd
from io import StringIO
import plotly.express as px
# %% Função para puxar os dados da API
def estacoesSubBaciaAPI(cod, tpEst):
    """
    Busca estações de uma sub-bacia no inventário da ANA (HidroWeb)

    cod: código da sub-bacia (string)
    tpEst: '1' = fluviométrica  |  '2' = pluviométrica
    """
    if (tpEst != '1' and tpEst != '2'):
      print('ERRO: Informe um valor válido para tpEst. ("1" - fluviométrica; "2" - pluviométrica)')
    else:
        url = 'http://telemetriaws1.ana.gov.br/ServiceANA.asmx/HidroInventario'
        params = {
            'codEstDE': '',
            'codEstATE': '',
            'tpEst': tpEst,
            'nmEst': '',
            'nmRio': '',
            'codSubBacia': cod,
            'codBacia': '',
            'nmMunicipio': '',
            'nmEstado': '',
            'sgResp': '',
            'sgOper': '',
            'telemetrica': ''
        }

        response = requests.get(url, params = params)

        df = pd.read_xml(StringIO(response.text), xpath = '//Table')
        return df
# %%
df = estacoesSubBaciaAPI("51","1")
df
# %%
df["DataIns"], df["DataAlt"] = pd.to_datetime(df["DataIns"]), pd.to_datetime(df["DataAlt"])

# %%
df = df.sort_values(["id","DataIns"],ascending=False)

# %%
df["Operando"] = df['Operando'].astype(str)
# %%
fig = px.timeline(df,x_start="DataIns",x_end="DataAlt",y="RioNome",color="Operando",color_discrete_map={1:"blue",0:"red"},
                  hover_data={
                     "DataIns": "|%d/%m/%y",
                     "DataAlt": "|%d/%m/%y"
                  })
fig.update_yaxes(autorange="reversed")
fig.show()
