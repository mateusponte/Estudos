#Passo 1: Importando as bibliotecas para manipulação dos dados#
import pandas as pd #biblioteca para calculos
import numpy as np
from pandas_datareader import data #Para ler os dados
import matplotlib.pyplot as plt #biblioteca para importar gráficos
import seaborn as sns #biblioteca para gráficos estáticos
import plotly.express as px #gráficos interativos

acoes = ['ABEV3.SA', 'ODPV3.SA', 'VIVT3.SA', 'BBAS3.SA','PETR3.SA', 'BOVA11.SA']   #QUAIS AÇÕES PESQUISAR
acoes_df = pd.DataFrame() #dateframe vazio, receber os dados
for acao in acoes:

    acoes_df[acao]=data.DataReader(acao, data_source='yahoo', start = '2015-01-01') #laço para buscar as ações selecionadas

acoes_df