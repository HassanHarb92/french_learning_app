# ===========================================
# streamlit_french_stories.py (UPDATED)
# ===========================================

import streamlit as st
import pandas as pd

# =========================================================
# 1) Data for Short Stories
# =========================================================
@st.cache_data
def load_stories():
    # Replace with your actual CSV or dataset path for the 100 stories.
    # For demonstration, we'll assume the user has stored them in 'stories.csv'.
    return pd.read_csv("stories.csv")

# =========================================================
# 2) Data for Irregular Verbs with Multiple Tenses
# =========================================================
# Below is a list of 50 common French irregular verbs.
# We now include:
#  - Présent
#  - Passé Composé (masculine forms)
#  - Imparfait
#  - Futur Simple
#  - Conditionnel Présent
# for A2/B1-level learners.
# For brevity, we show only 5 verbs fully fleshed out here.
# The same structure applies to all 50 verbs.

verbs_data = [
    {
        "infinitive": "aller",
        "meaning": "to go",
        "tenses": {
            "Présent": {
                "je": "vais",
                "tu": "vas",
                "il/elle/on": "va",
                "nous": "allons",
                "vous": "allez",
                "ils/elles": "vont"
            },
            "Passé Composé": {
                "je": "suis allé",
                "tu": "es allé",
                "il/elle/on": "est allé(e)",
                "nous": "sommes allé(e)s",
                "vous": "êtes allé(e)(s)",
                "ils/elles": "sont allé(e)s"
            },
            "Imparfait": {
                "je": "allais",
                "tu": "allais",
                "il/elle/on": "allait",
                "nous": "allions",
                "vous": "alliez",
                "ils/elles": "allaient"
            },
            "Futur Simple": {
                "je": "irai",
                "tu": "iras",
                "il/elle/on": "ira",
                "nous": "irons",
                "vous": "irez",
                "ils/elles": "iront"
            },
            "Conditionnel Présent": {
                "je": "irais",
                "tu": "irais",
                "il/elle/on": "irait",
                "nous": "irions",
                "vous": "iriez",
                "ils/elles": "iraient"
            }
        }
    },
    {
        "infinitive": "avoir",
        "meaning": "to have",
        "tenses": {
            "Présent": {
                "je": "ai",
                "tu": "as",
                "il/elle/on": "a",
                "nous": "avons",
                "vous": "avez",
                "ils/elles": "ont"
            },
            "Passé Composé": {
                "je": "ai eu",
                "tu": "as eu",
                "il/elle/on": "a eu",
                "nous": "avons eu",
                "vous": "avez eu",
                "ils/elles": "ont eu"
            },
            "Imparfait": {
                "je": "avais",
                "tu": "avais",
                "il/elle/on": "avait",
                "nous": "avions",
                "vous": "aviez",
                "ils/elles": "avaient"
            },
            "Futur Simple": {
                "je": "aurai",
                "tu": "auras",
                "il/elle/on": "aura",
                "nous": "aurons",
                "vous": "aurez",
                "ils/elles": "auront"
            },
            "Conditionnel Présent": {
                "je": "aurais",
                "tu": "aurais",
                "il/elle/on": "aurait",
                "nous": "aurions",
                "vous": "auriez",
                "ils/elles": "auraient"
            }
        }
    },
    {
        "infinitive": "être",
        "meaning": "to be",
        "tenses": {
            "Présent": {
                "je": "suis",
                "tu": "es",
                "il/elle/on": "est",
                "nous": "sommes",
                "vous": "êtes",
                "ils/elles": "sont"
            },
            "Passé Composé": {
                "je": "ai été",
                "tu": "as été",
                "il/elle/on": "a été",
                "nous": "avons été",
                "vous": "avez été",
                "ils/elles": "ont été"
            },
            "Imparfait": {
                "je": "étais",
                "tu": "étais",
                "il/elle/on": "était",
                "nous": "étions",
                "vous": "étiez",
                "ils/elles": "étaient"
            },
            "Futur Simple": {
                "je": "serai",
                "tu": "seras",
                "il/elle/on": "sera",
                "nous": "serons",
                "vous": "serez",
                "ils/elles": "seront"
            },
            "Conditionnel Présent": {
                "je": "serais",
                "tu": "serais",
                "il/elle/on": "serait",
                "nous": "serions",
                "vous": "seriez",
                "ils/elles": "seraient"
            }
        }
    },
    {
        "infinitive": "faire",
        "meaning": "to do / to make",
        "tenses": {
            "Présent": {
                "je": "fais",
                "tu": "fais",
                "il/elle/on": "fait",
                "nous": "faisons",
                "vous": "faites",
                "ils/elles": "font"
            },
            "Passé Composé": {
                "je": "ai fait",
                "tu": "as fait",
                "il/elle/on": "a fait",
                "nous": "avons fait",
                "vous": "avez fait",
                "ils/elles": "ont fait"
            },
            "Imparfait": {
                "je": "faisais",
                "tu": "faisais",
                "il/elle/on": "faisait",
                "nous": "faisions",
                "vous": "faisiez",
                "ils/elles": "faisaient"
            },
            "Futur Simple": {
                "je": "ferai",
                "tu": "feras",
                "il/elle/on": "fera",
                "nous": "ferons",
                "vous": "ferez",
                "ils/elles": "feront"
            },
            "Conditionnel Présent": {
                "je": "ferais",
                "tu": "ferais",
                "il/elle/on": "ferait",
                "nous": "ferions",
                "vous": "feriez",
                "ils/elles": "feraient"
            }
        }
    },
    {
        "infinitive": "prendre",
        "meaning": "to take",
        "tenses": {
            "Présent": {
                "je": "prends",
                "tu": "prends",
                "il/elle/on": "prend",
                "nous": "prenons",
                "vous": "prenez",
                "ils/elles": "prennent"
            },
            "Passé Composé": {
                "je": "ai pris",
                "tu": "as pris",
                "il/elle/on": "a pris",
                "nous": "avons pris",
                "vous": "avez pris",
                "ils/elles": "ont pris"
            },
            "Imparfait": {
                "je": "prenais",
                "tu": "prenais",
                "il/elle/on": "prenait",
                "nous": "prenions",
                "vous": "preniez",
                "ils/elles": "prenaient"
            },
            "Futur Simple": {
                "je": "prendrai",
                "tu": "prendras",
                "il/elle/on": "prendra",
                "nous": "prendrons",
                "vous": "prendrez",
                "ils/elles": "prendront"
            },
            "Conditionnel Présent": {
                "je": "prendrais",
                "tu": "prendrais",
                "il/elle/on": "prendrait",
                "nous": "prendrions",
                "vous": "prendriez",
                "ils/elles": "prendraient"
            }
        }
    },
    # -----------------------------------------------------------------------
    # ... Additional 45 verbs with similar structure for all requested tenses.
    # Fill these out as needed (passe_compose, imparfait, futur, conditionnel).
    # -----------------------------------------------------------------------
]

# =========================================================
# Streamlit App
# =========================================================
def main():
    st.title("French Learning App")

    tab1, tab2 = st.tabs(["Stories", "Irregular Verbs"])

    # ------------------
    # Tab 1: Stories
    # ------------------
    with tab1:
        st.header("Read French-English Short Stories")
        df_stories = load_stories()
        story_titles = df_stories["Title (French)"].unique()
        selected_title = st.selectbox("Choisissez une histoire / Choose a story", story_titles)
        selected_story = df_stories[df_stories["Title (French)"] == selected_title]
        st.subheader(selected_title)
        for _, row in selected_story.iterrows():
            st.markdown(f"**🇫🇷 {row['French Line']}**")
            st.markdown(f"*🇬🇧 {row['English Translation']}*\n")
        st.write("💡 Use this app to practice reading and comprehension in French!")

    # ------------------
    # Tab 2: Irregular Verbs (Extended Tenses)
    # ------------------
    with tab2:
        st.header("50 Common Irregular French Verbs")
        verbs_list = [v["infinitive"] for v in verbs_data]
        selected_verb_inf = st.selectbox("Choisissez un verbe / Choose a verb", verbs_list)

        selected_verb = next((v for v in verbs_data if v["infinitive"] == selected_verb_inf), None)
        if selected_verb:
            st.write(f"**Infinitive:** {selected_verb['infinitive']}")
            st.write(f"**Meaning:** {selected_verb['meaning']}")

            # Add a dropdown for tenses
            available_tenses = list(selected_verb["tenses"].keys())
            tense_choice = st.selectbox("Choisissez un temps / Choose a tense", available_tenses)

            st.subheader(tense_choice)

            # Retrieve the conjugation dict for this tense
            conjugation_dict = selected_verb["tenses"][tense_choice]

            # Convert the dictionary to a DataFrame
            df_verb = pd.DataFrame(
                list(conjugation_dict.items()),
                columns=["Subject Pronoun", "Conjugation"]
            )
            st.table(df_verb)
        else:
            st.write("No verb data found.")

if __name__ == "__main__":
    main()

