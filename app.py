import streamlit as st
Les_Fillieres = {
    "SMA":{
        "Maths": 9,
        "PC": 7,
        "SVT": 3,
        "SI": 0,
        "Fr": 4,
        "Sport": 4,
        "Ang": 2,
        "Philo": 2,
        "Ar": 2,
        "Is": 2,
        "Assiduite": 1,
    },
    "SMB":{
            "Maths": 9,
            "PC": 7,
            "SVT": 0,
            "SI": 3,
            "Fr": 4,
            "Sport": 4,
            "Ang": 2,
            "Philo": 2,
            "Ar": 2,
            "Is": 2,
            "Assiduite": 1,
        },
        "PC":{
                "Maths": 7,
                "PC": 7,
                "SVT": 5,
                "SI": 0,
                "Fr": 4,
                "Sport": 4,
                "Ang": 2,
                "Philo": 2,
                "Ar": 2,
                "Is": 2,
                "Assiduite": 1,
            },
            "SVT":{
                    "Maths": 7,
                    "PC": 5,
                    "SVT": 7,
                    "SI": 0,
                    "Fr": 4,
                    "Sport": 4,
                    "Ang": 2,
                    "Philo": 2,
                    "Ar": 2,
                    "Is": 2,
                    "Assiduite": 1,
                },
}
liste_fillieres = list(Les_Fillieres.keys())
if 'page' not in st.session_state:
     st.session_state.page = "filiere"
if st.session_state.page == "filiere":
    st.title("Claculateure des notes")
    st.write("Marhba bik !! khtar la filliere dyalek bach  ndozo ndkhlo les notes")
    choix = st.selectbox("Khtar la filliere dyaleek : ", liste_fillieres)
    if st.button("Suivant"):
         st.session_state.choix_de_filliere = choix
         st.session_state.page = "Notes"
         st.rerun()
elif st.session_state.page == "Notes":
     choix_de_fillière = st.session_state.choix_de_filliere
     st.title("Saisie Des Notes")
     st.success(f"Mzyan! khtariti la filliere : {choix_de_fillière}")
     if st.button("Previous"):
          st.session_state.page = "filliere"
          st.rerun()
     st.markdown("---")
     Mawad_l_élève = Les_Fillieres[choix_de_fillière]
     Majmo3_no9at = 0
     Majmo3_lmo3amilat = 0
     Moyennes_mawad = {}
     for mada, coeff in Mawad_l_élève.items():
          if coeff > 0:
               st.write(f"   {mada}   (coefficient: {coeff}) ")
               no9at_lmada = []
               for i in range(1, 4):
                    Skip = st.checkbox(f"skip lfard {i} dyal {mada}", key=f"skip_{mada}_fard_{i}")
                    if not Skip:
                         n9ta_jdida = st.number_input(
                              f"ch7al fl fard {i}, dyal lmada {mada}     (dir Skip ila makayench):",
                              min_value=0.00, max_value=20.00, step=0.25,
                              key=f"{mada}_fard_{i}"
                         )
                         no9at_lmada.append(n9ta_jdida)
               if len(no9at_lmada) > 0:
                    moyenne = sum(no9at_lmada)/len(no9at_lmada)
                    Moyennes_mawad[mada] = moyenne
                    Majmo3_no9at += (moyenne*coeff)
                    Majmo3_lmo3amilat += coeff
     st.markdown("---")
     if Majmo3_lmo3amilat > 0:
          if st.button("Caculer Ma Moyenne Generale"):
               st.session_state.moyennes_mawad = Moyennes_mawad
               st.session_state.moyenne_generale = Majmo3_no9at / Majmo3_lmo3amilat
               st.session_state.page = "Resaults"
               st.rerun()
elif st.session_state.page == "Resaults":
     st.balloons()
     st.title("Resultat de la Moyenne")
     st.success(f"Filliere ; -{st.session_state.choix_de_filliere}-")
     st.markdown("---")
     st.subheader("Les moyennes dyal kolla mada:")
     for mada_smiya, moyenne_dyalha in st.session_state.moyennes_mawad.items():
          st.write(f"  {mada_smiya}: {moyenne_dyalha:.2f}")
     st.markdown("---")
     st.success(f" La mooyenne generale dyalek hiya : {st.session_state.moyenne_generale:.2f}")
     st.markdown("---")
     col1, col2 = st.columns(2)
     with col1:
          if st.button("Modification des notes"):
               st.session_state.page = "Notes"
               st.rerun()
     with col2:
          if st.button("khtar  filliere akhra"):
               st.session_state.page = "filliere"
               st.rerun()