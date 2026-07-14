import streamlit as st
st.set_page_config(page_title="Sonic Palace of Scorpions")
pesquisa =st.text_input("Digite oque deseja encontrar", key="pesquisa principal")
espaco_resultado = st.empty()
st.divider()
st.title("Sonic Palace of Scorpions")
st.divider()
st.subheader("Bem vindos ao site oficial de Sonic Palace of Scorpions!")
st.write("Aqui teremos in formações sobre as músicas da HQ:")
st.divider()
st.subheader("Primeira música: Year Zero:")
st.html('<div id="year-zero"></div>')
st.video("C:\\Users\\lulu9\\Downloads\\lv_0_20260712164740.mkv")
st.caption("Vídeo da música Year Zero")
conteudo_site = ["Bem vindosao site oficial de Sonic Palace of Scorpions!", "rimeira música: Year Zero:", "Vídeo da música Year Zero"]
if pesquisa:
    espaco_resultado.write(f"Você pesquisou por: {pesquisa}")
    encontrado = False

    for texto in conteudo_site:
        if str(pesquisa).lower() in str(texto).lower():
            espaco_resultado.write(f"Resultado encontrado: {texto}")
            encontrado = True
            if  "year zero" in str(texto).lower():
                espaco_resultado.video("C:\\Users\\lulu9\\Documents\\python\\sites\\HQ\\Audio\\Musicas\\lv_0_20260712164740.mkv")
                espaco_resultado.caption("Vídeo da música Year Zero")

    if not encontrado:
            espaco_resultado.write("Nenhum resultado encontrado para a sua pesquisa.")
    
else:
     pass

