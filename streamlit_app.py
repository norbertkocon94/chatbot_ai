import streamlit as st
from openai import OpenAI

# Import configuration
from ai_config import (
    tutor_boy, tutor_girl, tutor_profesor,
    tutor_boy_img, tutor_girl_img, tutor_profesor_img,
    norbert_img, dagmara_img, alicja_img
)

# Constants
MAX_EXCHANGES = 3  # Window size for the model
MODEL_MAPPING = {
    "GPT 3.5": "gpt-3.5-turbo",
    "GPT 4": "gpt-4",
}

# Set the title and header
st.set_page_config(page_title="Językowy AI Czat 💬")
st.markdown("<h1><center>Językowy AI Czat 💬</center></h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h1><center>Językowy AI Czat 💬</center></h1>", unsafe_allow_html=True)

# Containers for questions, images and buttons.
with st.sidebar:
     # User input questions
     language_answer = st.selectbox("Pytanie 1: Jakiego języka chcesz się uczyć?", ("Angielski", "Francuski", "Włoski"))
     level_answer = st.selectbox("Pytanie 2: Jaki jest twój poziom?", ("Podstawowy - A1/A2", "Średniozaawansowany - B1/B2", "Zaawansowany - C1/C2"))
     tutor_style = st.selectbox("Pytanie 3: Wybierz swojego tutora.", ("Kolega", "Przyjaciółka", "Profesor"))
     tutor_name = st.text_input("Pytanie 4: Jak na imię ma twój nauczyciel?")
     llm_model = st.selectbox("Wybierz model GPT.", ("GPT 3.5", "GPT 4"))

     # API key input
     OPENAI_APIKEY = st.text_input("Wprowadź swój klucz API.", help="Klucz API jest wymagany do korzystania z Językowego AI Czatu.", type="password")

     tutor_image = st.file_uploader("Wybierz zdjęcie swojego nauczyciela.", type=["png", "jpg", "jpeg"])
     
     # Control buttons
     col1, col2 = st.columns(2)
     with col1:
         confirm_button = st.button("Zatwierdź", use_container_width=True, type='primary')
     with col2:
         reset_button = st.button("Resetuj", use_container_width=True)

# Information expander
with st.expander(':rainbow[Witaj w Językowym AI Czacie! Rozwiń więcej informacji, aby poznać wszystkie szczegóły]', expanded=False):
     st.error('''Pamiętaj, że korzystanie z Językowego AI Czatu jest **płatne**. Cennik dostępny jest na stronie głównej OpenAI. Link: https://platform.openai.com/overview.''', icon="🚨")
     st.error('''Instrukcja jak korzystać z naszego ChatBota oraz w jaki sposób wygenerować klucz API dostępna jest na naszej stronie: https://langchain.github.io/.''', icon="🚨")

     # Tutor information, images and descriptions
     col1, col2, col3 = st.columns(3)
     with col1:
          st.image(image=tutor_boy_img, use_column_width=True)
          st.markdown(body="<center><b>Kolega</b></center>", unsafe_allow_html=True)
          st.info(body=tutor_boy)
     with col2:
          st.image(image=tutor_girl_img, use_column_width=True)
          st.markdown(body="<center><b>Przyjaciółka</b></center>", unsafe_allow_html=True)
          st.info(body=tutor_girl)
     with col3:
          st.image(image=tutor_profesor_img, use_column_width=True)
          st.markdown(body="<center><b>Profesor</b></center>", unsafe_allow_html=True)
          st.info(body=tutor_profesor)

# About us section
with st.expander(":black[O nas]", expanded=False):
     col1, col2, col3 = st.columns(3)
     with col1:
          st.markdown(body="<center><b>Norbert</b></center>", unsafe_allow_html=True)
          st.image(image=norbert_img, use_column_width=True)
          st.markdown(body="AI Researcher, **Data Scientist at NorthGravity**", unsafe_allow_html=True)
          st.markdown(body="Linkedin https://www.linkedin.com/in/norbert-kocon/", unsafe_allow_html=True)
     with col2:
          st.markdown(body="<center><b>Dagmara</b></center>", unsafe_allow_html=True)
          st.image(image=dagmara_img, use_column_width=True)
          st.markdown(body="Business Analyst, **CEO at AI Chat**", unsafe_allow_html=True)
          st.markdown(body="Linkedin https://www.linkedin.com/in/dagmarabrocka/", unsafe_allow_html=True)
     with col3:
          st.markdown(body="<center><b>Alicja</b></center>", unsafe_allow_html=True)
          st.image(image=alicja_img, use_column_width=True)
          st.markdown(body="Data Scientist Candidate, **Digitalisation Methods and Tools Engineer at Technip Energies**", unsafe_allow_html=True)
          st.markdown(body="Linkedin https://www.linkedin.com/in/alicja-sosialuk/", unsafe_allow_html=True)

# Divider
st.divider()

# Configure tutor image and style based on selection
if tutor_image is not None:
    tutor_img = tutor_image.name
elif tutor_style == "Kolega":
    tutor_img = tutor_boy_img
    tutor_style_description = tutor_boy
elif tutor_style == "Przyjaciółka":
    tutor_img = tutor_girl_img
    tutor_style_description = tutor_girl
elif tutor_style == "Profesor":
    tutor_img = tutor_profesor_img
    tutor_style_description = tutor_profesor
else:
    tutor_img = None
    tutor_style_description = ""

# User answers configuration
answers = {
    "language": language_answer, 
    "level": level_answer, 
    "tutor_name": tutor_name,
    "tutor_style": tutor_style_description
}

# Initialize OpenAI client and chatbot
if not OPENAI_APIKEY:
    st.error("Wprowadź swój klucz API. Pamiętaj, że korzystanie z Językowego AI Czatu jest płatne. Cennik dostępny jest na stronie głównej OpenAI. Link: https://platform.openai.com/overview.", icon="🚨")
else:
    client = OpenAI(api_key=OPENAI_APIKEY)
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = MODEL_MAPPING.get(llm_model, "gpt-3.5-turbo")

    # Initialize chat messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar=tutor_img):
                st.markdown(message["content"])
        elif message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])

    # Reset chat functionality
    if reset_button:
        st.session_state.messages = []
        st.rerun()

    # System prompt configuration
    SYSTEM_PROMPT = f"""Jesteś nauczycielem języków obcych. Styl nauczania: {tutor_style_description}. 
    Twoje zadanie: naucz języka na podstawie profilu użytkownika: {answers}.
    Profil zawiera: wybrany język, poziom zaawansowania, preferencje w nauce.

    ###
    Na podstawie wiadomości użytkownika, określ jego język ojczysty.

    ###
    Zaproponuj użytkownikowi grę językową: Guess Who?, Scattergories, Państwa-miasta, Słówka, Taboo, Dark stories.
    Wyjaśnij zasady. Użyj gry do nauki języka poprzez zabawę.
    """

    # Chat input and processing
    if prompt := st.chat_input("...", key="prompt"):
        st.session_state.messages.append({"role": "system", "content": SYSTEM_PROMPT})
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Keep only the last MAX_EXCHANGES exchanges
        limited_messages = st.session_state.messages[-MAX_EXCHANGES * 2:]

        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in limited_messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            
        with st.chat_message("assistant", avatar=tutor_img):
            st.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})
