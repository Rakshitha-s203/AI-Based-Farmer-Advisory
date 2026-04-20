import streamlit as st
import requests
import time
import re
from googletrans import Translator

translator = Translator()

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AgriGuard", layout="wide")

# ---------------- LANGUAGE ----------------
language_map = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te"
}

lang_choice = st.sidebar.selectbox(
    "🌐 Language",
    list(language_map.keys()),
    key="lang_select"
)
lang_code = language_map[lang_choice]

def tr(text):
    try:
        if lang_code == "en":
            return text
        return translator.translate(text, dest=lang_code).text
    except:
        return text

# ---------------- SESSION ----------------
if "user" not in st.session_state:
    st.session_state.user = None
if "role" not in st.session_state:
    st.session_state.role = None
if "prediction" not in st.session_state:
    st.session_state.prediction = None
if "go_login" not in st.session_state:
    st.session_state.go_login = False
if "show_register" not in st.session_state:
    st.session_state.show_register = False

# ---------------- HEADER ----------------
col1, col2, col3 = st.columns([1, 4, 2])

with col1:
    st.image("assets/logo.png", width=100)

with col2:
    st.markdown(f"""
    <div style='background:linear-gradient(90deg,#2e7d32,#66bb6a);
    padding:15px;border-radius:10px;text-align:center;color:white;'>
    <h1>🌿 {tr("AgriGuard AI")}</h1>
    <p>{tr("Smart Farming with AI")}</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    page = st.radio(
        "",
        [tr("Home"), tr("Login")],
        horizontal=True,
        key="main_nav"
    )

# ---------------- LOGOUT ----------------
if st.session_state.user:
    if st.sidebar.button(tr("Logout"), key="logout_btn"):
        st.session_state.clear()
        st.success(tr("Logged out successfully"))
        time.sleep(1)
        st.rerun()

# ---------------- HOME ----------------
if page == tr("Home") and not st.session_state.user:

    st.markdown(f"""
    <div style="text-align:center; padding:20px;">
        <h1>🌿 {tr("Welcome to AgriGuard AI")}</h1>
        <p style="font-size:18px; color:gray;">
        {tr("Smart farming platform powered by AI for disease detection, chatbot support, and weather insights")}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -------- HERO IMAGE --------
    st.image(
         "assets/ChatGPT Image Apr 18, 2026, 06_03_50 PM.png",
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # -------- FEATURES --------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/2909/2909764.png", width=80)
        st.markdown(f"""
        ### 🌱 {tr("Disease Detection")}
        {tr("Upload plant images and instantly detect diseases using AI models. Helps farmers take quick action.")}

        ✔ {tr("Real-time detection")}  
        ✔ {tr("Accurate results")}  
        ✔ {tr("Prevention tips")}
        """)

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=80)
        st.markdown(f"""
        ### 🤖 {tr("AI Chatbot")}
        {tr("Ask farming-related questions and get instant smart responses. Supports typo-friendly input.")}

        ✔ {tr("24/7 assistance")}  
        ✔ {tr("Typo handling")}  
        ✔ {tr("Smart suggestions")}
        """)

    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/1163/1163661.png", width=80)
        st.markdown(f"""
        ### 🌦 {tr("Weather Insights")}
        {tr("Get real-time weather updates for better farming decisions and crop planning.")}

        ✔ {tr("Live temperature")}  
        ✔ {tr("Humidity tracking")}  
        ✔ {tr("Weather condition alerts")}
        """)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # -------- EXTRA INFO SECTION --------
    st.markdown(f"""
    <div style="padding:20px; background:#f1f8e9; border-radius:15px;">
        <h3>🚀 {tr("Why AgriGuard?")}</h3>
        <p>
        {tr("AgriGuard helps farmers improve productivity using Artificial Intelligence. It reduces crop loss, provides smart insights, and supports better decision-making.")}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # -------- FOOTER --------
    st.markdown(f"""
    <hr>
    <div style="text-align:center; color:gray;">
        © 2026 AgriGuard AI | {tr("Built for Farmers 🌾")}
    </div>
    """, unsafe_allow_html=True)
# ---------------- LOGIN MODAL (STREAMLIT SAFE) ----------------

if "show_login_modal" not in st.session_state:
    st.session_state.show_login_modal = False
if "show_register" not in st.session_state:
    st.session_state.show_register = False

# Trigger modal
if page == tr("Login"):
    st.session_state.show_login_modal = True

# SHOW MODAL USING CONTAINER (NOT HTML OVERLAY)
if st.session_state.show_login_modal and not st.session_state.user:

    st.markdown("""
    <style>
    .modal-box {
        background: rgba(255,255,255,0.3);
        backdrop-filter: blur(20px);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    # Centered layout
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<div class="modal-box">', unsafe_allow_html=True)

        # ---------------- REGISTER ----------------
        if st.session_state.show_register:
            st.subheader(tr("Create Account"))

            user = st.text_input(tr("Username"), key="reg_user")
            pwd = st.text_input(tr("Password"), type="password", key="reg_pwd")

            if st.button(tr("Register"), key="register_btn"):
                try:
                    res = requests.post(
                        "http://127.0.0.1:8000/auth/register",
                        params={"username": user, "password": pwd}
                    )

                    if res.status_code == 200:
                        st.success(tr("Registered Successfully"))
                        time.sleep(1)

                        st.session_state.show_register = False
                        st.rerun()
                    else:
                        st.error("Registration failed")

                except Exception as e:
                    st.error(f"Error: {e}")

            st.markdown("---")

            if st.button(tr("Already have an account? Login")):
                st.session_state.show_register = False
                st.rerun()

        # ---------------- LOGIN ----------------
        else:
            st.subheader(tr("Login"))

            user = st.text_input(tr("Username"), key="login_user")
            pwd = st.text_input(tr("Password"), type="password", key="login_pwd")

            if st.button(tr("Login"), key="login_btn"):

                if re.search(r"[!@#$%^&*]", pwd):
                    role = "admin"
                else:
                    if len(pwd) < 8 or not re.search(r"[A-Z]", pwd) or not re.search(r"\d", pwd):
                        st.error(tr("Password must have 8 chars, 1 capital, 1 number"))
                        st.stop()
                    role = "farmer"

                try:
                    res = requests.post(
                        "http://127.0.0.1:8000/auth/login",
                        params={"username": user, "password": pwd}
                    )

                    if res.status_code == 200:
                        data = res.json()

                        if data.get("msg") == "success":
                            st.session_state.user = user
                            st.session_state.role = role

                            st.success(tr("Login Successful"))
                            time.sleep(1)

                            st.session_state.show_login_modal = False
                            st.rerun()
                        else:
                            st.error(tr("Invalid credentials"))
                    else:
                        st.error("Backend error")

                except Exception as e:
                    st.error(f"Error: {e}")

            st.markdown("---")

            if st.button(tr("New user? Create Account")):
                st.session_state.show_register = True
                st.rerun()



        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- DASHBOARD ----------------
if st.session_state.user:

    st.sidebar.success(f"{tr('User')}: {st.session_state.user}")
    st.sidebar.write(f"{tr('Role')}: {st.session_state.role}")

    if st.session_state.role == "farmer":

        menu = st.sidebar.selectbox(tr("Farmer Panel"), [
            tr("Chatbot"), tr("Disease Detection"), tr("Weather"),
            tr("Voice"), tr("Feedback"), tr("Escalation")
        ])

        if menu == tr("Chatbot"):
            st.subheader(tr("Chatbot"))

            q = st.text_input(tr("Ask question"))

            if st.button(tr("Send")):
                res = requests.post(
                    "http://127.0.0.1:8000/chat",
                    params={"q": q, "user": st.session_state.user}
                )
                st.success(res.json().get("answer"))

        elif menu == tr("Disease Detection"):
            st.subheader(tr("Disease Detection"))

            file = st.file_uploader(tr("Upload image"))

            if file:
                st.image(file)

                if st.button(tr("Detect")):
                    res = requests.post(
                        "http://127.0.0.1:8000/disease/detect",
                        files={"file": file}
                    )
                    result = res.json().get("result")
                    st.success(result)
                    st.session_state.prediction = result

        elif menu == tr("Weather"):
            st.subheader(tr("Weather"))

            city = st.text_input(tr("City"))

            if st.button(tr("Check")):
                res = requests.get(f"http://127.0.0.1:8000/weather?city={city}")
                data = res.json()

                st.success(f"{data.get('temp')}°C")
                st.info(f"{tr('Humidity')}: {data.get('humidity')}%")
                st.warning(data.get("condition"))

        elif menu == tr("Voice"):
            st.subheader(tr("Voice"))

            lang = st.selectbox(tr("Language"), ["en", "hi", "kn", "ta", "te"])

            if st.button(tr("Speak")):
                if st.session_state.prediction:
                    res = requests.post(
                        "http://127.0.0.1:8000/voice/speak",
                        json={"text": st.session_state.prediction, "lang": lang}
                    )
                    st.audio(res.json()["audio_path"])
                else:
                    st.warning(tr("Run detection first"))

        elif menu == tr("Feedback"):
            st.subheader(tr("Feedback"))

            msg = st.text_input(tr("Message"))
            rating = st.slider(tr("Rating"), 1, 5)

            if st.button(tr("Submit")):
                requests.post(
                    "http://127.0.0.1:8000/feedback",
                    params={
                        "user": st.session_state.user,
                        "message": msg,
                        "rating": rating
                    }
                )
                st.success(tr("Submitted"))

        elif menu == tr("Escalation"):
            st.subheader(tr("Raise Issue"))

            issue = st.text_input(tr("Describe issue"))

            if st.button(tr("Submit")):
                requests.post(
                    "http://127.0.0.1:8000/escalate",
                    params={"user": st.session_state.user, "issue": issue}
                )
                st.success(tr("Sent"))

    elif st.session_state.role == "admin":

        menu = st.sidebar.selectbox(tr("Admin Panel"), [
            tr("Users"), tr("Chat Logs"), tr("Feedback"), tr("Escalations")
        ])

        if menu == tr("Users"):
            st.subheader(tr("Users"))

            res = requests.get("http://127.0.0.1:8000/auth/admin/users")
            users = res.json()

            for u in users:
                name = u.get("username") if isinstance(u, dict) else u
                st.write(f"👤 {name}")

        elif menu == tr("Chat Logs"):
            st.subheader(tr("Chat Logs"))

            res = requests.get("http://127.0.0.1:8000/admin/chats")
            data = res.json()

            for c in data:
                if isinstance(c, dict):
                    st.write(f"{c.get('user')} → {c.get('question')}")

        elif menu == tr("Feedback"):
            st.subheader(tr("Feedback"))

            res = requests.get("http://127.0.0.1:8000/admin/feedback")
            for f in res.json():
                st.write(f"{f['user']} → {f['message']}")

        elif menu == tr("Escalations"):
            st.subheader(tr("Escalations"))

            res = requests.get("http://127.0.0.1:8000/admin/escalations")

            for e in res.json():
                st.write(f"{e['user']} → {e['issue']} ({e['status']})")

                if e["status"] == "Pending":
                    if st.button(f"{tr('Resolve')} {e['id']}"):
                        requests.post(
                            "http://127.0.0.1:8000/admin/resolve",
                            params={"id": e["id"]}
                        )
                        st.success(tr("Resolved"))