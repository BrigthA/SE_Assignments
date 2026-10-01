import html

import streamlit as st

st.set_page_config(page_title="Student Grade Portal", page_icon="📘", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

    :root {
        --ink: #17342d;
        --muted: #66776f;
        --paper: #f5f7f2;
        --line: #dce5dc;
        --green: #246b50;
        --lime: #d8ef9f;
    }
    .stApp {
        background:
            radial-gradient(ellipse at 8% 5%, rgba(216, 239, 159, .34), transparent 29rem),
            var(--paper);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }
    .block-container { max-width: 780px; padding-top: 3.2rem; padding-bottom: 4rem; }
    h1, h2, h3, p, label, button, input { font-family: 'DM Sans', sans-serif; }
    .hero { padding: 1.4rem 0 1.7rem; border-bottom: 1px solid var(--line); margin-bottom: 1.6rem; }
    .eyebrow { color: var(--green); font-size: .75rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; }
    .hero h1 { color: var(--ink); font-family: 'Manrope', sans-serif; font-size: 2.65rem; font-weight: 800; line-height: 1.08; margin: .7rem 0 .65rem; }
    .hero p { color: var(--muted); font-size: 1rem; margin: 0; max-width: 34rem; }
    [data-testid="stForm"] { background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 1.35rem 1.45rem 1.15rem; box-shadow: 0 12px 32px rgba(23, 52, 45, .06); }
    [data-testid="stTextInput"] label, [data-testid="stNumberInput"] label { color: var(--ink); font-weight: 600; }
    [data-testid="stTextInput"] input, [data-testid="stNumberInput"] input { background: #fff; border-radius: 7px; color: var(--ink); }
    [data-testid="stTextInput"] input::placeholder { color: #819087; opacity: 1; }
    [data-testid="stNumberInput"] button { background: #fff; color: var(--ink); }
    [data-testid="stFormSubmitButton"] button { background: var(--green); border: 1px solid var(--green); border-radius: 7px; color: white; font-weight: 700; min-height: 2.8rem; transition: background .18s ease, transform .18s ease; }
    [data-testid="stFormSubmitButton"] button:hover { background: #194f3b; border-color: #194f3b; transform: translateY(-1px); }
    .section-title { color: var(--ink); font-family: 'Manrope', sans-serif; font-size: 1.1rem; font-weight: 800; margin: 1.9rem 0 .85rem; }
    .grade-item { background: rgba(255,255,255,.72); border: 1px solid var(--line); border-radius: 8px; padding: .85rem .6rem; text-align: center; height: 100%; }
    .grade-letter { color: var(--green); font-family: 'Manrope', sans-serif; font-size: 1.25rem; font-weight: 800; }
    .grade-range { color: var(--muted); font-size: .75rem; margin-top: .2rem; white-space: nowrap; }
    .result { background: #fff; border: 1px solid var(--line); border-left: 5px solid var(--green); border-radius: 9px; margin-top: 1.25rem; padding: 1.2rem 1.4rem; }
    .result.grade-c { border-left-color: #d39b32; }
    .result.grade-d, .result.grade-e { border-left-color: #cf644e; }
    .result-label { color: var(--muted); font-size: .72rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
    .result h2 { color: var(--ink); font-family: 'Manrope', sans-serif; font-size: 1.25rem; margin: .35rem 0 .25rem; }
    .result p { color: var(--muted); margin: 0; }
    .grade-mark { color: var(--green); font-size: 1.45rem; font-weight: 800; }
    @media (max-width: 640px) {
        .block-container { padding: 2rem 1rem 3rem; }
        [data-testid="stForm"] { padding: 1rem; }
        .hero h1 { font-size: 2rem; }
        .grade-range { font-size: .68rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <header class="hero">
        <div class="eyebrow">Academic services / Results</div>
        <h1>Student grade portal</h1>
        <p>Enter a student roll number and mark to view the grade result.</p>
    </header>
    """,
    unsafe_allow_html=True,
)

with st.form("grade_form"):
    username = st.text_input("Roll number", placeholder="e.g. STU-2048")
    mark = st.number_input("Mark", min_value=0, max_value=100, value=0, step=1, help="Enter a whole-number score from 0 to 100.")
    submitted = st.form_submit_button("Calculate grade", use_container_width=True)

if submitted:
    if not username.strip():
        st.error("Please enter a roll number to continue.")
    else:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "E"

        messages = {
            "A": "Excellent work. Keep it up!",
            "B": "Good work. You are making strong progress.",
            "C": "A solid result. Keep building on it.",
            "D": "There is room to improve. Keep practicing.",
            "E": "Keep working hard and ask for support when you need it.",
        }
        safe_username = html.escape(username.strip())
        st.markdown(
            f"""
            <section class="result grade-{grade.lower()}">
                <div class="result-label">Grade result</div>
                <h2>{safe_username}</h2>
                <p>Mark: <strong>{mark}/100</strong> &nbsp; <span class="grade-mark">{grade}</span></p>
                <p>{messages[grade]}</p>
            </section>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-title">Grade scale</div>', unsafe_allow_html=True)
grade_columns = st.columns(5)
for column, (grade, score_range) in zip(grade_columns, [("A", "90–100"), ("B", "80–89"), ("C", "70–79"), ("D", "60–69"), ("E", "0–59")]):
    with column:
        st.markdown(
            f'<div class="grade-item"><div class="grade-letter">{grade}</div><div class="grade-range">{score_range}</div></div>',
            unsafe_allow_html=True,
        )
