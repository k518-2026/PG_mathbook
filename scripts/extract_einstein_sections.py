# -*- coding: utf-8 -*-
"""
Extract 32 Sections and 4 Appendices of Einstein's Relativity (#30155)
into a structured JSON file.
"""
import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

SOURCE_TXT = "books/30155_einstein_relativity/pg30155.txt"
OUTPUT_JSON = "books/30155_einstein_relativity/einstein_sections.json"

SECTION_TITLES = {
    "I": "Physical Meaning of Geometrical Propositions",
    "II": "The System of Co-ordinates",
    "III": "Space and Time in Classical Mechanics",
    "IV": "The Galileian System of Co-ordinates",
    "V": "The Principle of Relativity (in the Restricted Sense)",
    "VI": "The Theorem of the Addition of Velocities employed in Classical Mechanics",
    "VII": "The Apparent Incompatibility of the Law of Propagation of Light with the Principle of Relativity",
    "VIII": "On the Idea of Time in Physics",
    "IX": "The Relativity of Simultaneity",
    "X": "On the Relativity of the Conception of Distance",
    "XI": "The Lorentz Transformation",
    "XII": "The Behaviour of Measuring-Rods and Clocks in Motion",
    "XIII": "Theorem of the Addition of Velocities. The Experiment of Fizeau",
    "XIV": "The Heuristic Value of the Theory of Relativity",
    "XV": "General Results of the Theory",
    "XVI": "Experience and the Special Theory of Relativity",
    "XVII": "Minkowski's Four-Dimensional Space",
    "XVIII": "Special and General Principle of Relativity",
    "XIX": "The Gravitational Field",
    "XX": "The Equality of Inertial and Gravitational Mass as an Argument for the General Postulate of Relativity",
    "XXI": "In What Respects are the Foundations of Classical Mechanics and of the Special Theory of Relativity Unsatisfactory?",
    "XXII": "A Few Inferences from the General Principle of Relativity",
    "XXIII": "Behaviour of Clocks and Measuring-Rods on a Rotating Body of Reference",
    "XXIV": "Euclidean and Non-Euclidean Continuum",
    "XXV": "Gaussian Co-ordinates",
    "XXVI": "The Space-Time Continuum of the Special Theory of Relativity Considered as a Euclidean Continuum",
    "XXVII": "The Space-Time Continuum of the General Theory of Relativity is Not a Euclidean Continuum",
    "XXVIII": "Exact Formulation of the General Principle of Relativity",
    "XXIX": "The Solution of the Problem of Gravitation on the Basis of the General Principle of Relativity",
    "XXX": "Cosmological Difficulties of Newton's Theory",
    "XXXI": "The Possibility of a \"Finite\" and Yet \"Unbounded\" Universe",
    "XXXII": "The Structure of Space According to the General Theory of Relativity"
}

APPENDIX_TITLES = {
    "App_I": ("Simple Derivation of the Lorentz Transformation", "APPENDIX I"),
    "App_II": ("Minkowski's Four-Dimensional Space (\"World\")", "APPENDIX II"),
    "App_III": ("The Experimental Confirmation of the General Theory of Relativity", "APPENDIX III"),
    "App_IV": ("The Structure of Space According to the General Theory of Relativity (Supplementary)", "APPENDIX IV")
}

def extract_sections():
    with open(SOURCE_TXT, "r", encoding="utf-8") as f:
        text = f.read()

    pref_start = text.find("PREFACE\n")
    p1_start = text.find("PART I: THE SPECIAL THEORY OF RELATIVITY\n\n\n\nI.")
    if p1_start == -1:
        p1_start = text.find("PART I: THE SPECIAL THEORY OF RELATIVITY")
    
    preface_text = text[pref_start:p1_start].replace("PREFACE", "").strip()

    romans = [
        "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
        "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
        "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX",
        "XXXI", "XXXII"
    ]

    # Find starting index of each section
    indices = {}
    search_from = p1_start
    for r in romans:
        if r == "IV":
            pos = text.find("IV. THE GALILEIAN SYSTEM OF CO-ORDINATES", search_from)
        elif r == "XXI":
            pos = text.find("XXI.\n\nIN WHAT RESPECTS ARE THE FOUNDATIONS", search_from)
            if pos == -1:
                pos = text.find("XXI.", search_from)
        elif r == "XXXI":
            pos = text.find("XXXI.\n\nTHE POSSIBILITY OF A", search_from)
            if pos == -1:
                pos = text.find("XXXI.", search_from)
        else:
            # find '\n' + r + '.\n'
            pos = text.find(f"\n{r}.\n", search_from)
            if pos == -1:
                pos = text.find(f"\n{r}.", search_from)
        
        if pos != -1:
            indices[r] = pos
            search_from = pos + 10
        else:
            print(f"Warning: could not find section {r}")

    app1_pos = text.find("APPENDIX I\n")
    app2_pos = text.find("APPENDIX II\n")
    app3_pos = text.find("APPENDIX III\n")
    app4_pos = text.find("APPENDIX IV\n")
    end_pos = text.find("End of the Project Gutenberg EBook")
    if end_pos == -1:
        end_pos = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")

    sections_data = []

    # Add Preface
    sections_data.append({
        "number": "Preface",
        "part": "Preface",
        "title_en": "Preface",
        "text_en": preface_text,
        "length": len(preface_text)
    })

    for i, r in enumerate(romans):
        start = indices[r]
        if i + 1 < len(romans):
            next_r = romans[i+1]
            end = indices[next_r]
        else:
            end = app1_pos

        sec_text = text[start:end].strip()
        # Clean section header from body
        # E.g. remove "I. PHYSICAL MEANING..."
        part = "Part I" if i < 17 else ("Part II" if i < 29 else "Part III")
        
        sections_data.append({
            "number": r,
            "part": part,
            "title_en": SECTION_TITLES[r],
            "text_en": sec_text,
            "length": len(sec_text)
        })

    # Appendices
    apps = [
        ("App_I", "Appendix I", "Simple Derivation of the Lorentz Transformation", app1_pos, app2_pos),
        ("App_II", "Appendix II", "Minkowski's Four-Dimensional Space (\"World\")", app2_pos, app3_pos),
        ("App_III", "Appendix III", "The Experimental Confirmation of the General Theory of Relativity", app3_pos, app4_pos),
        ("App_IV", "Appendix IV", "The Structure of Space According to the General Theory of Relativity (Supplementary)", app4_pos, end_pos),
    ]

    for code, num, title, st, ed in apps:
        app_text = text[st:ed].strip()
        sections_data.append({
            "number": code,
            "part": "Appendix",
            "title_en": title,
            "text_en": app_text,
            "length": len(app_text)
        })

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(sections_data, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(sections_data)} sections/appendices to {OUTPUT_JSON}")
    for s in sections_data:
        print(f"[{s['number']}] {s['title_en']} ({s['length']} chars)")

if __name__ == "__main__":
    extract_sections()
