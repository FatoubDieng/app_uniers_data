import streamlit as st

def afficher_formulaire():
    st.subheader("📝 Évaluation de l'application")
    nom = st.text_input("Votre nom")
    note = st.slider("Note sur 5", 1, 5)
    commentaire = st.text_area("Commentaires")

    if st.button("Soumettre"):
        with open("form/feedbacks.txt", "a", encoding="utf-8") as f:
            f.write(f"{nom},{note},{commentaire}\n")
        st.success("Merci pour votre retour !")