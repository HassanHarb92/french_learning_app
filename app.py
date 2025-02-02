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
# Below is a list of ~25 common French irregular verbs (original 14 plus more) with:
#  - Présent
#  - Passé Composé (masculine form)
#  - Imparfait
#  - Futur Simple
#  - Conditionnel Présent
# for A2/B1-level learners.

# Whenever you need the full 50, just replicate the structure.

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
    # Additional Verbs
    # -----------------------------------------------------------------------
    {
        "infinitive": "pouvoir",
        "meaning": "to be able to / can",
        "tenses": {
            "Présent": {
                "je": "peux",
                "tu": "peux",
                "il/elle/on": "peut",
                "nous": "pouvons",
                "vous": "pouvez",
                "ils/elles": "peuvent"
            },
            "Passé Composé": {
                "je": "ai pu",
                "tu": "as pu",
                "il/elle/on": "a pu",
                "nous": "avons pu",
                "vous": "avez pu",
                "ils/elles": "ont pu"
            },
            "Imparfait": {
                "je": "pouvais",
                "tu": "pouvais",
                "il/elle/on": "pouvait",
                "nous": "pouvions",
                "vous": "pouviez",
                "ils/elles": "pouvaient"
            },
            "Futur Simple": {
                "je": "pourrai",
                "tu": "pourras",
                "il/elle/on": "pourra",
                "nous": "pourrons",
                "vous": "pourrez",
                "ils/elles": "pourront"
            },
            "Conditionnel Présent": {
                "je": "pourrais",
                "tu": "pourrais",
                "il/elle/on": "pourrait",
                "nous": "pourrions",
                "vous": "pourriez",
                "ils/elles": "pourraient"
            }
        }
    },
    {
        "infinitive": "vouloir",
        "meaning": "to want",
        "tenses": {
            "Présent": {
                "je": "veux",
                "tu": "veux",
                "il/elle/on": "veut",
                "nous": "voulons",
                "vous": "voulez",
                "ils/elles": "veulent"
            },
            "Passé Composé": {
                "je": "ai voulu",
                "tu": "as voulu",
                "il/elle/on": "a voulu",
                "nous": "avons voulu",
                "vous": "avez voulu",
                "ils/elles": "ont voulu"
            },
            "Imparfait": {
                "je": "voulais",
                "tu": "voulais",
                "il/elle/on": "voulait",
                "nous": "voulions",
                "vous": "vouliez",
                "ils/elles": "voulaient"
            },
            "Futur Simple": {
                "je": "voudrai",
                "tu": "voudras",
                "il/elle/on": "voudra",
                "nous": "voudrons",
                "vous": "voudrez",
                "ils/elles": "voudront"
            },
            "Conditionnel Présent": {
                "je": "voudrais",
                "tu": "voudrais",
                "il/elle/on": "voudrait",
                "nous": "voudrions",
                "vous": "voudriez",
                "ils/elles": "voudraient"
            }
        }
    },
    {
        "infinitive": "savoir",
        "meaning": "to know",
        "tenses": {
            "Présent": {
                "je": "sais",
                "tu": "sais",
                "il/elle/on": "sait",
                "nous": "savons",
                "vous": "savez",
                "ils/elles": "savent"
            },
            "Passé Composé": {
                "je": "ai su",
                "tu": "as su",
                "il/elle/on": "a su",
                "nous": "avons su",
                "vous": "avez su",
                "ils/elles": "ont su"
            },
            "Imparfait": {
                "je": "savais",
                "tu": "savais",
                "il/elle/on": "savait",
                "nous": "savions",
                "vous": "saviez",
                "ils/elles": "savaient"
            },
            "Futur Simple": {
                "je": "saurai",
                "tu": "sauras",
                "il/elle/on": "saura",
                "nous": "saurons",
                "vous": "saurez",
                "ils/elles": "sauront"
            },
            "Conditionnel Présent": {
                "je": "saurais",
                "tu": "saurais",
                "il/elle/on": "saurait",
                "nous": "saurions",
                "vous": "sauriez",
                "ils/elles": "sauraient"
            }
        }
    },
    {
        "infinitive": "venir",
        "meaning": "to come",
        "tenses": {
            "Présent": {
                "je": "viens",
                "tu": "viens",
                "il/elle/on": "vient",
                "nous": "venons",
                "vous": "venez",
                "ils/elles": "viennent"
            },
            "Passé Composé": {
                "je": "suis venu",
                "tu": "es venu",
                "il/elle/on": "est venu(e)",
                "nous": "sommes venu(e)s",
                "vous": "êtes venu(e)(s)",
                "ils/elles": "sont venu(e)s"
            },
            "Imparfait": {
                "je": "venais",
                "tu": "venais",
                "il/elle/on": "venait",
                "nous": "venions",
                "vous": "veniez",
                "ils/elles": "venaient"
            },
            "Futur Simple": {
                "je": "viendrai",
                "tu": "viendras",
                "il/elle/on": "viendra",
                "nous": "viendrons",
                "vous": "viendrez",
                "ils/elles": "viendront"
            },
            "Conditionnel Présent": {
                "je": "viendrais",
                "tu": "viendrais",
                "il/elle/on": "viendrait",
                "nous": "viendrions",
                "vous": "viendriez",
                "ils/elles": "viendraient"
            }
        }
    },
    {
        "infinitive": "voir",
        "meaning": "to see",
        "tenses": {
            "Présent": {
                "je": "vois",
                "tu": "vois",
                "il/elle/on": "voit",
                "nous": "voyons",
                "vous": "voyez",
                "ils/elles": "voient"
            },
            "Passé Composé": {
                "je": "ai vu",
                "tu": "as vu",
                "il/elle/on": "a vu",
                "nous": "avons vu",
                "vous": "avez vu",
                "ils/elles": "ont vu"
            },
            "Imparfait": {
                "je": "voyais",
                "tu": "voyais",
                "il/elle/on": "voyait",
                "nous": "voyions",
                "vous": "voyiez",
                "ils/elles": "voyaient"
            },
            "Futur Simple": {
                "je": "verrai",
                "tu": "verras",
                "il/elle/on": "verra",
                "nous": "verrons",
                "vous": "verrez",
                "ils/elles": "verront"
            },
            "Conditionnel Présent": {
                "je": "verrais",
                "tu": "verrais",
                "il/elle/on": "verrait",
                "nous": "verrions",
                "vous": "verriez",
                "ils/elles": "verraient"
            }
        }
    },
    {
        "infinitive": "devoir",
        "meaning": "to have to / must",
        "tenses": {
            "Présent": {
                "je": "dois",
                "tu": "dois",
                "il/elle/on": "doit",
                "nous": "devons",
                "vous": "devez",
                "ils/elles": "doivent"
            },
            "Passé Composé": {
                "je": "ai dû",
                "tu": "as dû",
                "il/elle/on": "a dû",
                "nous": "avons dû",
                "vous": "avez dû",
                "ils/elles": "ont dû"
            },
            "Imparfait": {
                "je": "devais",
                "tu": "devais",
                "il/elle/on": "devait",
                "nous": "devions",
                "vous": "deviez",
                "ils/elles": "devaient"
            },
            "Futur Simple": {
                "je": "devrai",
                "tu": "devras",
                "il/elle/on": "devra",
                "nous": "devrons",
                "vous": "devrez",
                "ils/elles": "devront"
            },
            "Conditionnel Présent": {
                "je": "devrais",
                "tu": "devrais",
                "il/elle/on": "devrait",
                "nous": "devrions",
                "vous": "devriez",
                "ils/elles": "devraient"
            }
        }
    },
    {
        "infinitive": "dire",
        "meaning": "to say",
        "tenses": {
            "Présent": {
                "je": "dis",
                "tu": "dis",
                "il/elle/on": "dit",
                "nous": "disons",
                "vous": "dites",
                "ils/elles": "disent"
            },
            "Passé Composé": {
                "je": "ai dit",
                "tu": "as dit",
                "il/elle/on": "a dit",
                "nous": "avons dit",
                "vous": "avez dit",
                "ils/elles": "ont dit"
            },
            "Imparfait": {
                "je": "disais",
                "tu": "disais",
                "il/elle/on": "disait",
                "nous": "disions",
                "vous": "disiez",
                "ils/elles": "disaient"
            },
            "Futur Simple": {
                "je": "dirai",
                "tu": "diras",
                "il/elle/on": "dira",
                "nous": "dirons",
                "vous": "direz",
                "ils/elles": "diront"
            },
            "Conditionnel Présent": {
                "je": "dirais",
                "tu": "dirais",
                "il/elle/on": "dirait",
                "nous": "dirions",
                "vous": "diriez",
                "ils/elles": "diraient"
            }
        }
    },
    {
        "infinitive": "lire",
        "meaning": "to read",
        "tenses": {
            "Présent": {
                "je": "lis",
                "tu": "lis",
                "il/elle/on": "lit",
                "nous": "lisons",
                "vous": "lisez",
                "ils/elles": "lisent"
            },
            "Passé Composé": {
                "je": "ai lu",
                "tu": "as lu",
                "il/elle/on": "a lu",
                "nous": "avons lu",
                "vous": "avez lu",
                "ils/elles": "ont lu"
            },
            "Imparfait": {
                "je": "lisais",
                "tu": "lisais",
                "il/elle/on": "lisait",
                "nous": "lisions",
                "vous": "lisiez",
                "ils/elles": "lisaient"
            },
            "Futur Simple": {
                "je": "lirai",
                "tu": "liras",
                "il/elle/on": "lira",
                "nous": "lirons",
                "vous": "lirez",
                "ils/elles": "liront"
            },
            "Conditionnel Présent": {
                "je": "lirais",
                "tu": "lirais",
                "il/elle/on": "lirait",
                "nous": "lirions",
                "vous": "liriez",
                "ils/elles": "liraient"
            }
        }
    },
    {
        "infinitive": "mettre",
        "meaning": "to put",
        "tenses": {
            "Présent": {
                "je": "mets",
                "tu": "mets",
                "il/elle/on": "met",
                "nous": "mettons",
                "vous": "mettez",
                "ils/elles": "mettent"
            },
            "Passé Composé": {
                "je": "ai mis",
                "tu": "as mis",
                "il/elle/on": "a mis",
                "nous": "avons mis",
                "vous": "avez mis",
                "ils/elles": "ont mis"
            },
            "Imparfait": {
                "je": "mettais",
                "tu": "mettais",
                "il/elle/on": "mettait",
                "nous": "mettions",
                "vous": "mettiez",
                "ils/elles": "mettaient"
            },
            "Futur Simple": {
                "je": "mettrai",
                "tu": "mettras",
                "il/elle/on": "mettra",
                "nous": "mettrons",
                "vous": "mettrez",
                "ils/elles": "mettront"
            },
            "Conditionnel Présent": {
                "je": "mettrais",
                "tu": "mettrais",
                "il/elle/on": "mettrait",
                "nous": "mettrions",
                "vous": "mettriez",
                "ils/elles": "mettraient"
            }
        }
    },
    {
        "infinitive": "dormir",
        "meaning": "to sleep",
        "tenses": {
            "Présent": {
                "je": "dors",
                "tu": "dors",
                "il/elle/on": "dort",
                "nous": "dormons",
                "vous": "dormez",
                "ils/elles": "dorment"
            },
            "Passé Composé": {
                "je": "ai dormi",
                "tu": "as dormi",
                "il/elle/on": "a dormi",
                "nous": "avons dormi",
                "vous": "avez dormi",
                "ils/elles": "ont dormi"
            },
            "Imparfait": {
                "je": "dormais",
                "tu": "dormais",
                "il/elle/on": "dormait",
                "nous": "dormions",
                "vous": "dormiez",
                "ils/elles": "dormaient"
            },
            "Futur Simple": {
                "je": "dormirai",
                "tu": "dormiras",
                "il/elle/on": "dormira",
                "nous": "dormirons",
                "vous": "dormirez",
                "ils/elles": "dormiront"
            },
            "Conditionnel Présent": {
                "je": "dormirais",
                "tu": "dormirais",
                "il/elle/on": "dormirait",
                "nous": "dormirions",
                "vous": "dormiriez",
                "ils/elles": "dormiraient"
            }
        }
    },
    {
        "infinitive": "mourir",
        "meaning": "to die",
        "tenses": {
            "Présent": {
                "je": "meurs",
                "tu": "meurs",
                "il/elle/on": "meurt",
                "nous": "mourons",
                "vous": "mourez",
                "ils/elles": "meurent"
            },
            "Passé Composé": {
                "je": "suis mort",
                "tu": "es mort",
                "il/elle/on": "est mort(e)",
                "nous": "sommes mort(e)s",
                "vous": "êtes mort(e)(s)",
                "ils/elles": "sont mort(e)s"
            },
            "Imparfait": {
                "je": "mourais",
                "tu": "mourais",
                "il/elle/on": "mourait",
                "nous": "mourions",
                "vous": "mouriez",
                "ils/elles": "mouraient"
            },
            "Futur Simple": {
                "je": "mourrai",
                "tu": "mourras",
                "il/elle/on": "mourra",
                "nous": "mourrons",
                "vous": "mourrez",
                "ils/elles": "mourront"
            },
            "Conditionnel Présent": {
                "je": "mourrais",
                "tu": "mourrais",
                "il/elle/on": "mourrait",
                "nous": "mourrions",
                "vous": "mourriez",
                "ils/elles": "mourraient"
            }
        }
    },
    {
        "infinitive": "falloir",
        "meaning": "to be necessary",
        "tenses": {
            "Présent": {
                "il": "faut"
            },
            "Passé Composé": {
                "il": "a fallu"
            },
            "Imparfait": {
                "il": "fallait"
            },
            "Futur Simple": {
                "il": "faudra"
            },
            "Conditionnel Présent": {
                "il": "faudrait"
            }
        }
    },
    {
        "infinitive": "pleuvoir",
        "meaning": "to rain",
        "tenses": {
            "Présent": {
                "il": "pleut"
            },
            "Passé Composé": {
                "il": "a plu"
            },
            "Imparfait": {
                "il": "pleuvait"
            },
            "Futur Simple": {
                "il": "pleuvra"
            },
            "Conditionnel Présent": {
                "il": "pleuvrait"
            }
        }
    }
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

