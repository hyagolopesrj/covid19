import pandas as pd
import plotly.express as px #BIBLIOTECA USADA PARA PLOTAR O GRÁFICO
import streamlit as st #BIBLIOTECA USADA PARA O FRONTEND

#streamlit run main_covid.py

#LENDO O DATASET
df = pd.read.csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#RENOMEANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos', 'newCases': 'Novos casos','deaths_per_100k_inhabitants': 'óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})

#SELEÇÃO DO ESTADO
estado = list(df['state'].unique())  #LISTA OS ESTADOS
state = st.sidebar.selectbox('Qual estado?', estados) #BARRA DE SELEÇÃO DOS ESTADOS

#SELEÇÃO DA COLUNA
#colum = 'Casos por 100 mil habitantes'
colunas = ['Novos óbitos','Novos casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

#SELEÇÃO DAS LINHAS QUE PERTENCEM AO ESTADO
df = df[df['state'] == state]

fig = px.line(df, x='date', y=column + ' - ' + state) #PLOTANDO O GRÁFICO (x = data e y=coluna(Número de casos))
fig.update_layout( xavis_title='Data', yaxix_title=column.upper(), title = {'x':0.5}) #Mudando o nome dos eixos do gráfico e posicionamento

st.title('DADOS COVID - BRASIL') #EXIBINDO TÍTULO ATRAVÉS DO STREAMLIT
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
