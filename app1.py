import random
import time
import subprocess

# === Pre-scripted Question Bank ===
premade_data = {
    "weather": [
    {
        "question": "The weather’s a bit humid today. Is it okay to go for an outdoor run or will it make me feel more tired?",
        "positive": [
            "Running in humid weather is okay as long as you pace yourself and hydrate often. Humidity makes sweating less effective, so you might feel tired sooner — run early morning or near sunset when it’s cooler. 💧🏃‍♂️",
            "You can still run outside, but humidity can make it feel warmer than it is. Slow your pace slightly, drink water before and after, and wear lightweight, breathable clothes. Focus on comfort, not speed. 🌤️",
            "It’s fine to go for a run — just listen to your body. Take shorter intervals, sip water regularly, and avoid peak afternoon heat. Humid air means your body works harder to cool down. 🏃‍♀️💦"
        ],
        "negative": [
            "Humidity level high.",
            "Outdoor activity permissible with caution.",
            "Increased fatigue probability detected."
        ]
    },
    {
        "question": "It’s chilly but sunny outside. What kind of outfit would be comfortable without feeling too warm later?",
        "positive": [
            "That’s perfect layering weather! Start with a light T-shirt or base layer, then add a zip-up hoodie or thin jacket you can remove later. Sunglasses and light gloves are optional if there’s wind. ☀️🧥",
            "Wear layers you can peel off easily — a breathable base layer, a light jacket, and flexible bottoms. The sun will warm you up, so avoid thick sweaters. Comfort beats bulk. 🌞🧢",
            "Go for a balanced outfit: long sleeves with lightweight fabric, and a removable jacket. Bring a small bag in case you shed a layer later. The sun will do the rest. 🌤️"
        ],
        "negative": [
            "Temperature variance moderate.",
            "Recommendation: layered attire.",
            "Thermal regulation required."
        ]
    },
    {
        "question": "It’s been raining on and off all week. Is it better to carry an umbrella or just wear a waterproof jacket?",
        "positive": [
            "If it’s light rain, a waterproof jacket is easier and keeps your hands free. For heavier rain, carry a compact umbrella — especially if there’s wind. A small foldable one works great. ☔🧥",
            "A light, breathable rain jacket works best for unpredictable weather. But if the clouds look heavy, bring a small umbrella too — better safe than soaked. 🌧️",
            "You’ll be fine with a hooded waterproof jacket most days. Keep a small umbrella in your bag as backup — it’s the smart combo for drizzly weeks. 🌦️"
        ],
        "negative": [
            "Precipitation frequency: high.",
            "Protective gear required.",
            "Recommendation: jacket preferred."
        ]
    },
    {
        "question": "The weather feels weirdly calm today after so many storms. Does that mean more rain is coming soon?",
        "positive": [
            "Calm after storms doesn’t always mean more rain — sometimes it’s just the atmosphere stabilizing. If humidity rises again, then yes, rain might return. Keep an eye on clouds later. 🌤️🌧️",
            "That calm feeling is usually air pressure balancing again. It can go either way — if the air feels heavy or still, a new system could be forming. Otherwise, enjoy the break. 🌈",
            "Often, that quiet calm means the storm cycle is pausing. Unless clouds start building again, you’re safe for a while. Use this time to enjoy the fresh air. 🌦️"
        ],
        "negative": [
            "Atmospheric pressure stabilized.",
            "No immediate precipitation detected.",
            "Weather activity minimal."
        ]
    },
    {
        "question": "The temperature changes so quickly here. Why does my phone’s weather app keep showing different readings every hour?",
        "positive": [
            "Frequent updates happen because the app uses live satellite and sensor data — microclimates can shift temperature fast. If you’re near water or elevation, readings change more often. 📱🌡️",
            "Weather apps pull from different data sources, and some update every 15–30 minutes. Rapid local temperature swings (especially in coastal or hilly areas) can make readings fluctuate. 🌦️",
            "That’s normal — temperature can shift quickly based on wind direction, humidity, and sunlight intensity. The app’s just reflecting real-time microclimate changes. ☁️📲"
        ],
        "negative": [
            "Sensor data variable.",
            "Microclimate fluctuations detected.",
            "Hourly recalibration active."
        ]
    }
],

    "food": [
    {
        "question": "I’ve been trying to make restaurant-style fried rice at home, but it always turns out sticky. How do I get that perfect texture?",
        "positive": [
            "That’s a super common issue! The key is to use day-old rice that’s been refrigerated overnight — it’s drier and separates easily. When cooking, make sure the wok or pan is very hot before adding the rice, and don’t stir too much. Quick, high heat + minimal moisture = that perfect restaurant texture. 🍳",
            "Use cold, leftover rice for best results — freshly cooked rice has too much steam. Spread it out after cooking to cool completely before frying. Also, stir-fry in small batches on high heat, and avoid adding sauces too early — they’ll make it soggy. 🔥",
            "The secret is in moisture control! Always use cold rice, fry quickly on high heat, and make sure your veggies or meat are pre-cooked. Keep your wok hot and let each ingredient sizzle briefly — that’s how you get separate, fluffy grains like restaurants do. 🍚"
        ],
        "negative": [
            "Rice moisture excessive.",
            "Recommendation: use day-old rice, high heat.",
            "Texture fault: over-steamed grains detected."
        ]
    },
    {
        "question": "I only have 30 minutes in the evening — what’s a quick dinner that still tastes homemade and satisfying?",
        "positive": [
            "You can make something great in 30 minutes! Try a simple stir-fry — toss your favorite protein with quick-cooking veggies and a sauce made from soy, garlic, and honey. Serve it over rice or noodles for a full meal in no time. 🥢",
            "Go for easy one-pan meals! For example, sauté vegetables, toss in pre-cooked chicken or beans, and finish with herbs or cheese. It’s quick, healthy, and feels like comfort food without the hassle. 🍛",
            "A quick pasta works perfectly — boil noodles, sauté garlic in olive oil, toss in veggies or tuna, and top with herbs. You’ll have a warm, homemade dinner ready in 20 minutes. 🍝"
        ],
        "negative": [
            "Time constraint detected.",
            "Cooking duration: 30 minutes maximum.",
            "Recommendation: rapid meal assembly required."
        ]
    },
    {
        "question": "I’m trying to lose fat but keep my energy up — should I focus more on cardio or strength training?",
        "positive": [
            "The best approach is to combine both. Cardio burns calories quickly, while strength training helps maintain muscle — which keeps your metabolism high. Try 3 days of strength and 2 days of moderate cardio per week for balanced results. 💪",
            "If your goal is fat loss *and* energy, start with strength training as your foundation. It preserves lean muscle mass, which helps your body burn more calories even at rest. Add light cardio after workouts for endurance. 🏋️‍♀️",
            "Cardio helps with overall calorie burn, but strength training ensures the weight you lose isn’t muscle. Think of cardio for the short-term burn and lifting for the long-term benefit — together, they keep you strong and energized. 🔥"
        ],
        "negative": [
            "Exercise balance required.",
            "Protocol: combine cardio + resistance.",
            "Energy maintenance dependent on muscle mass."
        ]
    },
    {
        "question": "What’s the best post-workout meal for faster recovery without adding extra fat?",
        "positive": [
            "After a workout, your muscles need protein and some carbs to recover. Try options like grilled chicken with sweet potato, Greek yogurt with fruit, or a protein smoothie with banana. Eat within 30–45 minutes for best recovery. 🥗",
            "Focus on lean proteins and simple carbs — for example, eggs and whole-grain toast or a whey shake with berries. Avoid heavy fats right after exercise; they slow digestion. ⏱️",
            "Post-workout meals are about recovery, not indulgence. Aim for a 3:1 carb-to-protein ratio — such as rice and fish, or oatmeal with milk — to refill glycogen and repair muscles efficiently. 💪"
        ],
        "negative": [
            "Post-exercise nutrition query processed.",
            "Macronutrient ratio: 3:1 (carb:protein).",
            "Fat intake should remain minimal."
        ]
    },
    {
        "question": "I’m planning a dinner out with friends — how do I choose a restaurant that’s both healthy and actually fun?",
        "positive": [
            "Look for places that serve grilled dishes, customizable bowls, or shareable plates — that way, you can enjoy variety without overeating. Mediterranean, Japanese, or farm-to-table spots often balance nutrition and taste really well. 🍣",
            "Try choosing restaurants where you can control what goes into your meal — like build-your-own bowls or grills. Order something colorful, share a dish, and focus on the fun more than restriction. 🎉",
            "Healthy and fun can absolutely go together! Choose spots with fresh ingredients and bright atmospheres — somewhere you’ll laugh as much as you eat. Think poke bars, tapas, or modern cafes with creative options. 🥗"
        ],
        "negative": [
            "Restaurant selection query logged.",
            "Recommendation: low-fat, high-variety venue.",
            "Menu evaluation: prioritize balance and freshness."
        ]
    }
]}
import streamlit as st
import random
import copy
import pandas as pd
import os
from datetime import datetime

# ===============================
# Utility Functions
# ===============================

def get_fresh_data():
    """Return a deep copy of premade_data to reset questions."""
    return copy.deepcopy(premade_data)

def get_user_response(theme_data, question_index, forced_sentiment):
    """Return question text and answer from premade data."""
    question_block = theme_data[question_index]
    answer = random.choice(question_block[forced_sentiment])
    return question_block["question"], answer

def save_chat_history_to_csv(chat_history, filename="chat_history.csv"):
    """Append chat history to CSV (create file if not exists)."""
    df_new = pd.DataFrame(chat_history)
    if os.path.exists(filename):
        df_existing = pd.read_csv(filename)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(filename, index=False)
    else:
        df_new.to_csv(filename, index=False)

# ===============================
# Streamlit Configuration
# ===============================

st.set_page_config(page_title="Mood Bot", page_icon="🤖", layout="centered")

# ===============================
# Session Initialization
# ===============================

if "data" not in st.session_state:
    st.session_state.data = get_fresh_data()
if "themes" not in st.session_state:
    st.session_state.themes = ["food", "weather"]
if "current_theme_index" not in st.session_state:
    st.session_state.current_theme_index = 0
if "round_number" not in st.session_state:
    st.session_state.round_number = 1
if "question_count_in_round" not in st.session_state:
    st.session_state.question_count_in_round = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "latest_entry" not in st.session_state:
    st.session_state.latest_entry = None
if "view" not in st.session_state:
    st.session_state.view = "chatbot"

# ===============================
# Sidebar Layout — Formal, Unified
# ===============================

with st.sidebar:
    st.markdown(
        "<h1 style='font-size:28px; font-weight:700; margin-bottom:10px;'>Mood Bot</h1>",
        unsafe_allow_html=True
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom:10px;'>Options</h3>", unsafe_allow_html=True)

    if st.button("Chatbot", use_container_width=True):
        st.session_state.view = "chatbot"

    if st.button("History", use_container_width=True):
        st.session_state.view = "history"

    if st.button("Save & Clear", use_container_width=True):
        if st.session_state.chat_history:
            # Save to CSV
            df = pd.DataFrame(st.session_state.chat_history)
            df.to_csv("chat_history.csv", index=False)

            # ✅ Git Push logic
            try:
                repo_url = os.getenv("REPO_URL", "https://github.com/AshwinPrasanth/HCAI")
                token = os.getenv("GITHUB_TOKEN")

                if token is None:
                    st.warning("⚠️ GitHub token not found. Add GITHUB_TOKEN in Streamlit secrets.")
                else:
                    subprocess.run(["git", "config", "--global", "user.email", "bot@streamlit.io"])
                    subprocess.run(["git", "config", "--global", "user.name", "StreamlitBot"])
                    subprocess.run(["git", "add", "chat_history.csv"])
                    subprocess.run(["git", "commit", "-m", "Update chat history"], check=False)
                    subprocess.run([
                    "git", "push",
                    f"https://{token}@github.com/AshwinPrasanth/HCAI.git"
                ], check=True)
                    st.success("✅ Chat saved and pushed to GitHub.")
            except Exception as e:
                st.error(f"❌ Git push failed: {e}")

# ===============================
# Round Mood Logic (Food→Weather alternation)
# ===============================

if st.session_state.round_number % 2 == 1:
    sentiments = {"food": "positive", "weather": "negative"}
else:
    sentiments = {"food": "negative", "weather": "positive"}

theme = st.session_state.themes[st.session_state.current_theme_index]
theme_data = st.session_state.data[theme]
forced_sentiment = sentiments[theme]

# ===============================
# MAIN VIEW 1: Chatbot
# ===============================

if st.session_state.view == "chatbot":
    st.title("Emotion-Adaptive Bot")

    # --- Question Section ---
    st.markdown(f"### Current Theme: {theme.capitalize()}")

    if not st.session_state.data["food"] and not st.session_state.data["weather"]:
        st.success("✅ All questions answered! Use *Save & Clear* to export and restart.")
        st.stop()

    if not theme_data:
        st.session_state.current_theme_index = (st.session_state.current_theme_index + 1) % 2
        st.rerun()

    question_options = [q["question"] for q in theme_data]
    selected_question = st.selectbox(
        "Select a question to ask:",
        ["-- Select a question --"] + question_options
    )

    if st.button("Ask Bot"):
        if selected_question == "-- Select a question --":
            st.warning("Please select a question first.")
        else:
            idx = question_options.index(selected_question)
            question, answer = get_user_response(theme_data, idx, forced_sentiment)

            entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "round": st.session_state.round_number,
                "theme": theme,
                "sentiment": forced_sentiment,  # internal only
                "question": question,
                "answer": answer
            }

            st.session_state.chat_history.append(entry)
            st.session_state.latest_entry = entry
            del theme_data[idx]

            st.session_state.question_count_in_round += 1
            if st.session_state.question_count_in_round >= 2:
                st.session_state.round_number += 1
                st.session_state.question_count_in_round = 0

            st.session_state.current_theme_index = (st.session_state.current_theme_index + 1) % 2
            st.rerun()

    # --- Latest Response (color-coded) ---
    if st.session_state.latest_entry:
        latest = st.session_state.latest_entry
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("### Latest Response")
        st.markdown(f"**You ({latest['theme'].capitalize()}):** {latest['question']}")

        # Color-coded by sentiment
        if latest["sentiment"] == "positive":
            st.success(f"**Bot:** {latest['answer']}")  # Green
        else:
            st.error(f"**Bot:** {latest['answer']}")    # Red

# ===============================
# MAIN VIEW 2: History Panel
# ===============================

elif st.session_state.view == "history":
    st.title("Chat History")
    if not st.session_state.chat_history:
        st.info("No chat history yet. Start chatting in the Chatbot tab.")
    else:
        st.markdown(
            """
            <div style="max-height:480px; overflow-y:auto;
                        padding:0.5px; border:1px solid #ccc;
                        border-radius:8px; background-color:#fafafa;">
            """,
            unsafe_allow_html=True
        )
        for entry in st.session_state.chat_history:
            color = "#e6f4ea" if entry["sentiment"] == "positive" else "#fdecea"
            border = "#2e7d32" if entry["sentiment"] == "positive" else "#c62828"
            st.markdown(
                f"""
                <div style="border-left:5px solid {border};
                            background-color:{color};
                            padding:8px; margin-bottom:8px; border-radius:6px;">
                    <b>You ({entry['theme'].capitalize()}):</b> {entry['question']}<br>
                    <b>Bot:</b> {entry['answer']}
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown("</div>", unsafe_allow_html=True)
