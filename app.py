
import streamlit as st

st.set_page_config(page_title="Quiz TCC – Distorções Cognitivas", layout="centered")

st.title("🧠 Quiz: Distorções Cognitivas (CD-Quest)")
st.markdown("Teste seus conhecimentos sobre distorções cognitivas com base na Terapia Cognitivo-Comportamental.")

# Dados das perguntas
perguntas = [
    {
        "pergunta": "1. Qual das frases abaixo representa um exemplo de PENSAMENTO DICOTÔMICO?",
        "opcoes": [
            "Eu fui bem, mas poderia ter ido melhor.",
            "Cometi um erro, então sou um fracasso total.",
            "Às vezes acerto, às vezes erro.",
            "Aprendi algo novo, mesmo que tenha errado."
        ],
        "correta": 1
    },
    {
        "pergunta": "2. Quando uma pessoa ignora os aspectos positivos de uma situação, ela comete qual distorção?",
        "opcoes": [
            "Catastrofização",
            "Leitura mental",
            "Desqualificação do positivo",
            "Personalização"
        ],
        "correta": 2
    },
    {
        "pergunta": "3. Qual é a distorção cognitiva presente nesta frase: 'Se eu não for perfeito, serei rejeitado'?",
        "opcoes": [
            "Afirmações do tipo 'deveria'",
            "Raciocínio emocional",
            "Supergeneralização",
            "Personalização"
        ],
        "correta": 0
    },
    {
        "pergunta": "4. 'Tenho certeza de que todos perceberam meu erro' é um exemplo de:",
        "opcoes": [
            "Previsão do futuro",
            "Leitura mental",
            "Ampliação",
            "Rotulação"
        ],
        "correta": 1
    },
    {
        "pergunta": "5. Qual distorção cognitiva é demonstrada por: 'Vou fracassar e isso será insuportável'?",
        "opcoes": [
            "Pensamento dicotômico",
            "Visão em túnel",
            "Catastrofização",
            "Raciocínio emocional"
        ],
        "correta": 2
    }
]

respostas_usuario = []
pontuacao = 0

with st.form("quiz_form"):
    for i, p in enumerate(perguntas):
        st.markdown(f"**{p['pergunta']}**")
        escolha = st.radio("Escolha uma opção:", p["opcoes"], key=f"q{i}")
        respostas_usuario.append(escolha)

    submitted = st.form_submit_button("Enviar respostas")

if submitted:
    for i, p in enumerate(perguntas):
        resposta_correta = p["opcoes"][p["correta"]]
        if respostas_usuario[i] == resposta_correta:
            st.success(f"✅ Pergunta {i+1}: Correta!")
            pontuacao += 1
        else:
            st.error(f"❌ Pergunta {i+1}: Incorreta. Resposta correta: **{resposta_correta}**")

    st.markdown("---")
    st.subheader(f"🎯 Pontuação final: {pontuacao} de {len(perguntas)}")
