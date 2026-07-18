import streamlit as st

st.set_page_config(page_title="Sonic Palace of Scorpions")
pesquisa = st.text_input("Digite o que deseja encontrar", key="pesquisa_principal")
espaco_resultado = st.empty()

st.divider()
st.title("Sonic Palace of Scorpions")
st.divider()

st.subheader("Bem vindos ao site oficial de Sonic Palace of Scorpions!")
st.write("Aqui teremos informações sobre as músicas da HQ:")
st.divider()

st.subheader("Primeira Musica: Year Zero:")
st.html('<div id="year-zero"></div>')
st.video("Musicas/lv_0_20260712164740.mp4")
st.caption("Vídeo da música Year Zero")
st.write("Creditos: Ghost B.C")
st.divider()
st.subheader("Segunda Musica: This Is My Song: ")
st.video("Musicas/km_20260714-2_1080p_30f_20260714_135737.mp4")
st.caption("Thi is my song")
conteudo_site = [
    "Bem vindos ao site oficial de Sonic Palace of Scorpions!",
    "Primeira música: Year Zero:",
    "Vídeo da música Year Zero",
    "creditos: Ghost B.C",
    "Segunda Musica: This Is My Song:"
]

if pesquisa:
    espaco_resultado.write(f"Você pesquisou por: {pesquisa}")
    encontrado = False
    for texto in conteudo_site:
        if str(pesquisa).lower() in str(texto).lower():
            espaco_resultado.write(f"Resultado encontrado: {texto}")
            encontrado = True
        
            
    if not encontrado:
        espaco_resultado.write("Nenhum resultado encontrado para a sua pesquisa.")
else:
    pass   
