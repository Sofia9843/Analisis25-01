import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from wordcloud import WordCloud

dp = pd.read_csv('desempleo(cr).csv')
tmr = pd.read_csv('tasa_cambio(cr).csv')
pib = pd.read_csv('pib(cr).csv')
cp = pd.read_csv('colcap(cr).csv')
inf = pd.read_csv('inflacion(cr).csv')

# Días y tendencias
degree = 3

dp['fecha'] = pd.to_datetime(dp['fecha'])
dp = dp.sort_values('fecha')
dp['dias'] = (dp['fecha'] - dp['fecha'].min()).dt.days
coefs_dp = np.polyfit(dp['dias'], dp['tasa_desempleo'], degree)
poly_dp = np.poly1d(coefs_dp)
dp['tendencia'] = poly_dp(dp['dias'])

pib['fecha'] = pd.to_datetime(pib['fecha'])
pib = pib.sort_values('fecha')
pib['dias'] = (pib['fecha'] - pib['fecha'].min()).dt.days
coefs_pib = np.polyfit(pib['dias'], pib['pib_trimestral'], degree)
poly_pib = np.poly1d(coefs_pib)
pib['tendencia'] = poly_pib(pib['dias'])

tmr['fecha'] = pd.to_datetime(tmr['fecha'])
tmr = tmr.sort_values('fecha')
tmr['dias'] = (tmr['fecha'] - tmr['fecha'].min()).dt.days
coefs_tmr = np.polyfit(tmr['dias'], tmr['tasa_cambio(trm)'], degree)
poly_tmr = np.poly1d(coefs_tmr)
tmr['tendencia'] = poly_tmr(tmr['dias'])

cp['fecha'] = pd.to_datetime(cp['fecha'])
cp = cp.sort_values('fecha')
cp['dias'] = (cp['fecha'] - cp['fecha'].min()).dt.days
coefs_cp = np.polyfit(cp['dias'], cp['colcap'], degree)
poly_cp = np.poly1d(coefs_cp)
cp['tendencia'] = poly_cp(cp['dias'])

inf['fecha'] = pd.to_datetime(inf['fecha'])
inf = inf.sort_values('fecha')
inf['dias'] = (inf['fecha'] - inf['fecha'].min()).dt.days
coefs_inf = np.polyfit(inf['dias'], inf['inflacion'], degree)
poly_inf = np.poly1d(coefs_inf)
inf['tendencia'] = poly_inf(inf['dias'])

st.title("Análisis variables económicas")

Tab1, Tab2, Tab3, Tab4, Tab5 = st.tabs(['Desempleo', 'PIB', 'TRM', 'COLCAP', 'Inflación'])

with Tab1:
    st.subheader("Análisis Desempleo")
    fig = px.line(dp, x='fecha', y='tasa_desempleo', title='Tendencia del desempleo en el tiempo')
    fig.add_trace(px.line(dp, x='fecha', y='tendencia').data[0])  
    fig.data[1].line.dash = 'dash'  
    fig.data[1].line.color = 'red'  
    fig.data[1].name = 'Tendencia'  
    fig.add_vline(x='2018-08-07', line_dash="dash", line_color="gray")
    fig.add_vline(x='2022-08-07', line_dash="dash", line_color="gray")
    fig.add_annotation(x='2014-08-07', y=14, text="P.Santos", showarrow=False, font=dict(size=16))
    fig.add_annotation(x='2019-08-07', y=18, text="P.Duque", showarrow=False, font=dict(size=16))
    fig.add_annotation(x='2023-08-07', y=16, text="P.Petro", showarrow=False, font=dict(size=16))
    fig.update_layout(
        xaxis_title='Fecha',
        yaxis_title='Tasa de Desempleo %', 
        xaxis_tickangle=45,
        template='plotly_white',
        width=1000,
        height=500
    )
    st.plotly_chart(fig)

    st.subheader("Nube de palabras del discurso sobre el desempleo")
    with open("DESEMPLEO_2.txt", "r", encoding="utf-8") as file:
        text = file.read()
    wordcloud = WordCloud(width=1000, height=500, background_color='white', colormap='viridis').generate(text)
    fig_wc, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig_wc)

    with open("DESEMPLEO.txt", "r", encoding="utf-8") as file:
        text = file.read()
    wordcloud = WordCloud(width=1000, height=500, background_color='white', colormap='viridis').generate(text)
    fig_wc, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig_wc)

    st.subheader("Conclusión evaluando coherencia entre el discurso gubernamental con datos de desempleo")
    with open("DMAN.txt", "r", encoding="utf-8") as file:
        comentario = file.read()
    st.write(comentario)

with Tab2:
    st.subheader("Análisis PIB")
    fig = px.line(pib, x='fecha', y='pib_trimestral', title='PIB en el tiempo')
    fig.add_trace(px.line(pib, x='fecha', y='tendencia').data[0])
    fig.data[1].line.dash = 'dash'
    fig.data[1].line.color = 'red'
    fig.data[1].name = 'Tendencia'
    fig.add_vline(x='2018-08-07', line_dash="dash", line_color="gray")
    fig.add_vline(x='2022-08-07', line_dash="dash", line_color="gray")
    fig.add_annotation(x='2014-08-07', y=10, text="P.Santos", showarrow=False, font=dict(size=16))
    fig.add_annotation(x='2019-08-07', y=18, text="P.Duque", showarrow=False, font=dict(size=16))
    fig.add_annotation(x='2023-08-07', y=16, text="P.Petro", showarrow=False, font=dict(size=16))
    fig.update_layout(
        xaxis_title='Fecha',
        yaxis_title='Porcentaje de cambio del PIB', 
        xaxis_tickangle=45,
        template='plotly_white',
        width=1000,
        height=500
    )
    st.plotly_chart(fig)

    st.subheader("Nube de palabras del discurso sobre el PIB")
    with open("PIB.txt", "r", encoding="utf-8") as file:
        text = file.read()
    wordcloud = WordCloud(width=1000, height=500, background_color='white', colormap='viridis').generate(text)
    fig_wc, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig_wc)

    with open("PIB_2.txt", "r", encoding="utf-8") as file:
        text = file.read()
    wordcloud = WordCloud(width=1000, height=500, background_color='white', colormap='viridis').generate(text)
    fig_wc, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig_wc)

    st.subheader("Conclusión evaluando coherencia entre el discurso gubernamental con datos de PIB")
    with open("PIBAN.txt", "r", encoding="utf-8") as file:
        comentario = file.read()
    st.write(comentario)

with Tab3:
    st.subheader("Análisis TRM")
    fig = px.line(tmr, x='fecha', y='tasa_cambio(trm)', title='TRM en el tiempo')
    fig.add_trace(px.line(tmr, x='fecha', y='tendencia').data[0])
    fig.data[1].line.dash = 'dash'
    fig.data[1].line.color = 'red'
    fig.data[1].name = 'Tendencia'
    fig.add_vline(x='2018-08-07', line_dash="dash", line_color="gray")
    fig.add_vline(x='2022-08-07', line_dash="dash", line_color="gray")
    fig.add_annotation(x='2014-08-07', y=1000, text="P.Santos", showarrow=False, font=dict(size=16))
    fig.add_annotation(x='2019-08-07', y=1800, text="P.Duque", showarrow=False, font=dict(size=16))
    fig.add_annotation(x='2023-08-07', y=1600, text="P.Petro", showarrow=False, font=dict(size=16))
    fig.update_layout(
        xaxis_title='Fecha',
        yaxis_title='Tasa de Cambio (TRM)',  
        xaxis_tickangle=45,
        template='plotly_white',
        width=1000,
        height=500
    )
    st.plotly_chart(fig)

    st.subheader("Nube de palabras del discurso sobre la TRM")
    with open("TRM.txt", "r", encoding="utf-8") as file:
        text = file.read()
    wordcloud = WordCloud(width=1000, height=500, background_color='white', colormap='viridis').generate(text)
    fig_wc, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig_wc)

    st.subheader("Conclusión evaluando coherencia entre el discurso gubernamental con datos de TRM")
    with open("TRMAN.txt", "r", encoding="utf-8") as file:
        comentario = file.read()
    st.write(comentario)

with Tab4:
    st.subheader("Análisis Colcap")
    fig = px.line(cp, x='fecha', y='colcap', title='Colcap en el tiempo')
    fig.add_trace(px.line(cp, x='fecha', y='tendencia').data[0])
    fig.data[1].line.dash = 'dash'
    fig.data[1].line.color = 'red'
    fig.data[1].name = 'Tendencia'
    fig.add_vline(x='2018-08-07', line_dash="dash", line_color="gray")
    fig.add_vline(x='2022-08-07', line_dash="dash", line_color="gray")
    fig.add_annotation(x='2014-08-07', y=1150, text="P.Santos", showarrow=False, font=dict(size=16))
    fig.add_annotation(x='2019-08-07', y=1800, text="P.Duque", showarrow=False, font=dict(size=16))
    fig.add_annotation(x='2023-08-07', y=1600, text="P.Petro", showarrow=False, font=dict(size=16))
    fig.update_layout(
        xaxis_title='Fecha',
        yaxis_title='Valor del COLCAP',
        xaxis_tickangle=45,
        template='plotly_white',
        width=1000,
        height=500
    )
    st.plotly_chart(fig)

    st.subheader("Conclusión evaluando coherencia entre el discurso gubernamental con datos de COLCAP")
    with open("COLAN.txt", "r", encoding="utf-8") as file:
        comentario = file.read()
    st.write(comentario)

with Tab5:
    st.subheader("Análisis Inflación")
    fig = px.line(inf, x='fecha', y='inflacion', title='Inflación en el tiempo')
    fig.add_trace(px.line(inf, x='fecha', y='tendencia').data[0])
    fig.data[1].line.dash = 'dash'
    fig.data[1].line.color = 'red'
    fig.data[1].name = 'Tendencia'
    fig.add_vline(x='2018-08-07', line_dash="dash", line_color="gray")
    fig.add_vline(x='2022-08-07', line_dash="dash", line_color="gray")
    fig.add_annotation(x='2014-08-07', y=10, text="P.Santos", showarrow=False, font=dict(size=16))
    fig.add_annotation(x='2019-08-07', y=18, text="P.Duque", showarrow=False, font=dict(size=16))
    fig.add_annotation(x='2023-08-07', y=16, text="P.Petro", showarrow=False, font=dict(size=16))
    fig.update_layout(
        xaxis_title='Fecha',
        yaxis_title='Inflación %', 
        xaxis_tickangle=45,
        template='plotly_white',
        width=1000,  
        height=500
    )
    st.plotly_chart(fig)

    st.subheader("Nube de palabras del discurso sobre el inflación")
    with open("INFLACION.txt", "r", encoding="utf-8") as file:
        text = file.read()
    wordcloud = WordCloud(width=1000, height=500, background_color='white', colormap='viridis').generate(text)
    fig_wc, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig_wc)

    st.subheader("Conclusión evaluando coherencia entre el discurso gubernamental con datos de INFLACIÓN")
    with open("INFAN.txt", "r", encoding="utf-8") as file:
        comentario = file.read()
    st.write(comentario)