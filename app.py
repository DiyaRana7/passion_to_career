# passion_to_career_final_no_defaults.py
import streamlit as st
import plotly.express as px
import time
from PIL import Image
import io

# -------------------
# App Theme
# -------------------
st.set_page_config(page_title="Passion-to-Career AI Advisor", layout="wide")
st.markdown("""
<style>
.stApp {background-color: #f5f5f5;}
.stButton>button {background-color: #4a90e2; color:white; font-weight:bold; padding:10px 20px; font-size:16px; border-radius:10px;}
/* Fix selectbox text visibility */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #2c3e50 !important;
    font-size: 18px !important;
    border-radius: 12px !important;
}

/* Selected value text */
.stSelectbox span {
    color: #2c3e50 !important;
    font-size: 18px !important;
}

.stTextInput>div>input{background-color:#fff; padding:10px; font-size:18px; border-radius:10px;}
@keyframes sparkle {0% {color: #f1c40f;}25% {color: #e67e22;}50% {color: #2ecc71;}75% {color: #3498db;}100% {color: #f1c40f;}}
.animated-header h1 {animation: sparkle 3s infinite;}
.animated-header h3 {animation: sparkle 4s infinite;}
.animated-badge {animation: sparkle 2s infinite; font-size: 28px;}
</style>
""", unsafe_allow_html=True)

# -------------------
# Header
# -------------------
st.markdown("""
<div class="animated-header" style="background: linear-gradient(90deg, #1abc9c, #3498db); padding:40px; border-radius:20px; text-align:center; box-shadow: 2px 2px 15px rgba(0,0,0,0.2);">
    <h1 style="color:white; font-size:70px; font-weight:bold; margin-bottom:10px;">🎯 WELCOME TO PASSION-TO-CAREER AI ADVISOR</h1>
    <h3 style="color:#f1c40f; font-size:28px; margin-bottom:20px;">Discover your passion & turn it into a career! 🌟</h3>
    <p style="color:white; font-size:22px; margin-bottom:10px;">Enter your name below 👇</p>
</div>
""", unsafe_allow_html=True)

# -------------------
# Name Input
# -------------------
user_name = st.text_input("Your Name", placeholder="Enter your name")
if not user_name:
    st.stop()

st.markdown(f"""
<div style="background-color:#e67e22; padding:20px; border-radius:15px; text-align:center; box-shadow: 2px 2px 8px rgba(0,0,0,0.2); margin-top:15px;">
    <h2 style='color:white; font-size:32px; margin:0;'>🎉 Hello, {user_name}! Let's customize your experience:</h2>
</div>
""", unsafe_allow_html=True)

# -------------------
# Favorite Color
# -------------------
st.write("Pick your favorite color 🎨")
color_options = {
    "🔴 Red": "#FF0000", "🔵 Blue": "#0000FF", "🟢 Green": "#008000", "💛 Yellow": "#FFFF00",
    "🟣 Purple": "#800080", "💗 Pink": "#FFC0CB", "🟠 Orange": "#FFA500", "⚫ Black": "#000000",
    "⚪ White": "#FFFFFF", "💎 Cyan": "#00FFFF", "✨ Magenta": "#FF00FF", "🦚 Teal": "#008080",
    "🍫 Maroon": "#800000", "⚓ Navy": "#000080", "🌫 Grey": "#808080"
}
fav_color_name = st.selectbox("Choose Color", list(color_options.keys()))
fav_color = color_options[fav_color_name]
st.session_state.favorite_color = fav_color

# -------------------
# Questions
# -------------------
interests_options = ["💻 Technology", "🎨 Art & Design", "🎤 Music", "✍ Writing",
                     "📈 Business", "👨‍🏫 Teaching", "🎙 Public Speaking",
                     "🏋 Sports / Fitness", "🧠 Science", "🎭 Entertainment"]

all_questions = [
    {"type":"interests","question":"💡 Which areas are you interested in? (1–3 choose)","options":interests_options,"input":"multiselect"},
    {"type":"teamwork","question":"Do you prefer working in a team or solo?","options":["Team","Solo"],"input":"radio"},
    {"type":"creative_analytical","question":"Do you prefer creative or analytical work?","options":["Creative","Analytical"],"input":"radio"},
    {"type":"problem_solving","question":"Rate your problem-solving skill (1–5)","options":[1,2,3,4,5],"input":"selectbox"},
    {"type":"helping","question":"Rate your helping/guidance ability (1–5)","options":[1,2,3,4,5],"input":"selectbox"},
    {"type":"confidence","question":"Rate your self-confidence (1–5)","options":[1,2,3,4,5],"input":"selectbox"},
    {"type":"leadership","question":"Rate your leadership ability (1–5)","options":[1,2,3,4,5],"input":"selectbox"},
    {"type":"risk_taking","question":"Rate your risk-taking comfort (1–5)","options":[1,2,3,4,5],"input":"selectbox"},
    {"type":"passion_intensity","question":"How passionate are you about your top interest? (1–5)","options":[1,2,3,4,5],"input":"selectbox"},
]

if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.answers = {}

q = all_questions[st.session_state.q_index]
st.markdown(f"<h2 style='text-align:center;color:#2c3e50;'>{q['question']}</h2>", unsafe_allow_html=True)

# -------------------
# No Default Selections
# -------------------
ans = None
if q["input"]=="radio":
    ans = st.radio("", q["options"])
elif q["input"]=="selectbox":
    ans = st.selectbox("", q["options"])
elif q["input"]=="multiselect":
    ans = st.multiselect("", q["options"])

# -------------------
# Next Button
# -------------------
if st.button("Next"):
    if ans is None or (isinstance(ans,list) and len(ans)==0):
        st.warning("⚠ Please select an answer before proceeding!")
    else:
        st.session_state.answers[q['type']] = ans
        if st.session_state.q_index < len(all_questions)-1:
            st.session_state.q_index += 1
            st.rerun()
        else:
            # -------------------
            # Completion Progress
            # -------------------
            st.markdown(f"<h3 style='text-align:center;color:{fav_color};'>Calculating your best careers & courses...</h3>", unsafe_allow_html=True)
            progress_bar = st.progress(0)
            for i in range(101):
                time.sleep(0.01)
                progress_bar.progress(i)
            st.balloons()

            # -------------------
            # Career & Courses
            # -------------------
            career_mapping = {
                "💻 Technology":["Software Developer","Data Analyst","AI Engineer"],
                "🎨 Art & Design":["Graphic Designer","Illustrator"],
                "🎤 Music":["Musician","Music Producer"],
                "✍ Writing":["Writer","Content Creator"],
                "📈 Business":["Entrepreneur","Product Manager"],
                "👨‍🏫 Teaching":["Teacher","Life Coach"],
                "🎙 Public Speaking":["Speaker","Trainer"],
                "🏋 Sports / Fitness":["Fitness Trainer","Athlete"],
                "🧠 Science":["Scientist","Researcher"],
                "🎭 Entertainment":["Actor","Performer"]
            }

            course_mapping = {
                "Software Developer":["CS50","Python for Everybody"],
                "Data Analyst":["Data Analysis with Python","Excel for Data Analytics"],
                "AI Engineer":["Machine Learning by Andrew Ng","Deep Learning Specialization"],
                "Graphic Designer":["Photoshop Masterclass","UI/UX Design Fundamentals"],
                "Illustrator":["Illustrator CC Fundamentals","Digital Illustration"],
                "Musician":["Music Production Logic Pro","Ableton Live Courses"],
                "Music Producer":["Electronic Music Production","Mixing & Mastering Basics"],
                "Writer":["Creative Writing Workshop","Copywriting Masterclass"],
                "Content Creator":["Social Media Content","Video Editing with Premiere Pro"],
                "Entrepreneur":["Startup School","Business Model Canvas"],
                "Product Manager":["Product Management 101","Agile & Scrum Fundamentals"],
                "Teacher":["Effective Teaching Strategies","Classroom Management"],
                "Life Coach":["Life Coaching Certification","NLP for Coaches"],
                "Speaker":["Public Speaking Mastery","Storytelling Techniques"],
                "Trainer":["Corporate Training Skills","Presentation Skills"],
                "Fitness Trainer":["Personal Trainer Certification","Nutrition & Fitness"],
                "Athlete":["Sports Science Basics","Strength & Conditioning"],
                "Scientist":["Intro to Research Methods","Data Analysis for Scientists"],
                "Researcher":["Advanced Research Techniques","Scientific Writing"],
                "Actor":["Acting Fundamentals","Theater Workshop"],
                "Performer":["Stage Performance Skills","Dance & Movement Classes"]
            }

            # -------------------
            # Bubble Chart
            # -------------------
            selected_interests = st.session_state.answers.get("interests", [])
            interest_scores = {intr:10 for intr in selected_interests}
            extra_scores = ["problem_solving","helping","confidence","leadership","risk_taking","passion_intensity"]
            for es in extra_scores:
                interest_scores[es] = st.session_state.answers.get(es,3)

            df = {"Interest":list(interest_scores.keys()),"Score":list(interest_scores.values())}
            max_idx = df["Score"].index(max(df["Score"]))
            colors = [fav_color if i==max_idx else "#3498db" for i in range(len(df["Interest"]))]
            fig = px.scatter(df,x="Interest",y="Score",size="Score",color=df["Interest"],size_max=60)
            for i, trace in enumerate(fig.data):
                trace.marker.color = colors[i]
            st.subheader("💡 Your Interest & Skill Scores Visualization")
            st.plotly_chart(fig)

            # -------------------
            # Skills Progress Bars
            # -------------------
            st.subheader("💡 Your Skills Summary")
            skills_dict = {
                "Creativity": interest_scores.get("creative_analytical", 5),
                "Analytical Thinking": interest_scores.get("problem_solving", 5),
                "Leadership": interest_scores.get("leadership", 5),
                "Teamwork": interest_scores.get("teamwork", 5),
                "Risk Appetite": interest_scores.get("risk_taking", 5),
                "Passion Intensity": interest_scores.get("passion_intensity", 5)
            }
            for skill, val in skills_dict.items():
                st.markdown(f"{skill}:")
                st.progress(val/10)

            # -------------------
            # Passion Score & Badge
            # -------------------
            passion_score = sum(skills_dict.values())
            if passion_score>=45: badge="🌟 Passion Star"
            elif passion_score>=36: badge="🏅 Rising Talent"
            elif passion_score>=25: badge="🎯 Emerging Explorer"
            else: badge="✨ Curious Beginner"

            personality_text = f"{user_name}, based on your answers, you are {('creative and analytical' if 'Creative' in st.session_state.answers.get('creative_analytical',[]) else 'analytical')} and {'enjoy teamwork' if 'Team' in st.session_state.answers.get('teamwork',[]) else 'prefer solo work'}. Careers in {', '.join(selected_interests)} suit your strengths."

            # -------------------
            # Summary Card
            # -------------------
            top_careers = []
            for intr in selected_interests:
                top_careers.extend(career_mapping.get(intr,[]))

            summary_html = f"""
            <div style='background-color:{fav_color}; color:white; border-radius:20px; padding:20px; box-shadow:2px 2px 15px rgba(0,0,0,0.2); margin-top:20px;'>
                <h2 style='text-align:center;'>🎉 Your Career Summary</h2>
                <p><strong>Name:</strong> {user_name}</p>
                <p><strong>Top Interest(s):</strong> {", ".join(selected_interests)}</p>
                <p><strong>Top Careers:</strong> {", ".join(top_careers[:3])}</p>
                <p><strong>Recommended Courses:</strong> {", ".join(course_mapping.get(top_careers[0],[]))}</p>
                <p><strong>Passion Score:</strong> {passion_score}</p>
                <p class="animated-badge"><strong>Badge Earned:</strong> {badge}</p>
                <p><strong>Personality:</strong> {personality_text}</p>
            </div>
            """
            st.markdown(summary_html,unsafe_allow_html=True)

          
            # -------------------
            # Try Again
            # -------------------
            if st.button("🔄 Try Again"):
                for key in st.session_state.keys():
                    del st.session_state[key]
                st.rerun()