import streamlit as st
import json
import os

ARQUIVO = "progresso.json"

conteudos = {
    "Língua Portuguesa": {
        "Gramática e Estruturas da Língua Portuguesa": [
            "Fonologia", "Classes de palavras", "Concordância verbal e nominal",
            "Regência verbal e nominal", "Sintaxe", "Crase", "Colocação pronominal",
            "Formação de palavras"
        ],
        "Pontuação": [
            "Vírgula", "Ponto e vírgula", "Dois-pontos", "Ponto final",
            "Aspas", "Travessão", "Parênteses"
        ],
        "Ortografia Oficial": [
            "Emprego de letras", "Emprego do hífen", "Uso de acentos gráficos"
        ],
        "Compreensão e Interpretação de Textos": [
            "Identificação do tema", "Inferência de informações implícitas",
            "Estrutura textual", "Coesão e coerência", "Gêneros e tipos textuais"
        ]
    },
    "Gestão Pública, Ética e Legislação": {
        "Administração Pública": [
            "Modelos", "Administração Direta e Indireta", "Entidades", "Princípios (Art. 37)"
        ],
        "Ética": [
            "Código de Ética", "Postura e responsabilidade"
        ],
        "Gestão Universitária": [
            "CF/88", "LDB", "Estatuto da UFRGS", "PDI"
        ]
    }
}

if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r") as f:
        progresso = json.load(f)
else:
    progresso = {area: {sub: [False]*len(itens) for sub, itens in subs.items()} for area, subs in conteudos.items()}

st.title("📘 Checklist de Estudos – Concurso UFRGS")

for area, subareas in conteudos.items():
    st.header(area)
    for subarea, itens in subareas.items():
        st.subheader(subarea)
        for i, item in enumerate(itens):
            marcado = st.checkbox(item, value=progresso[area][subarea][i], key=f"{area}-{subarea}-{i}")
            progresso[area][subarea][i] = marcado

if st.button("💾 Salvar progresso"):
    with open(ARQUIVO, "w") as f:
        json.dump(progresso, f)
    st.success("Progresso salvo com sucesso!")

st.markdown("---")
st.subheader("📊 Estatísticas de Estudo")
for area, subareas in progresso.items():
    total = sum(len(itens) for itens in subareas.values())
    feitos = sum(sum(itens) for itens in subareas.values())
    percentual = (feitos / total) * 100 if total > 0 else 0
    st.write(f"**{area}**: {feitos}/{total} itens estudados ({percentual:.1f}%)")
