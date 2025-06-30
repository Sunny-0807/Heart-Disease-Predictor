import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("GROQ_API_KEY is not foound! Please set it in the .env file.")

client = Groq(api_key = groq_api_key)

# initialize the chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role" : "system",
         "content" : "You are a heart-health assistant giving food and lifestyle tips."}
    ]

if "last_bot_reply" not in st.session_state:
    st.session_state.last_bot_reply = ""

st.title("💬 Heart Health Chatbot")

st.markdown("### 🤖 Heart Health Chatbot")

with st.expander("💬 Open Chat"):
    user_message = st.text_input("You: ", key = "user_input")

    if st.button("Send"):
        if user_message.lower() in ["exit", "clear", "quit"]:
            st.session_state.chat_history = [
                {
                "role" : "system",
                "content" : "You are a heart-health assistant giving food and lifestyle tips."
                }
            ]
            st.info("🔁 Chat cleared.")
        elif user_message.strip():
            st.session_state.chat_history.append({
                "role" : "user",
                "content" : user_message
            })

            try:
                with st.spinner("🤖 Thinking..."):
                    response = client.chat.completions.create(
                        model = "llama3-70b-8192",
                        messages = st.session_state.chat_history
                    )
                assistant_reply = response.choices[0].message.content
                st.session_state.chat_history.append({
                    "role" : "assistant",
                    "content" : assistant_reply
                })
                st.session_state.last_bot_reply = assistant_reply
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
    if st.session_state.last_bot_reply:
        st.markdown(
            f"""
            <div style='text-align: left; background-color: #0; padding: 12px 15px; border-radius: 10px; margin: 10px 0; display: inline-block; max-width: 90%;'>
                <strong>🤖 Bot:</strong> {st.session_state.last_bot_reply}
            </div>
            """,
            unsafe_allow_html=True
        )


with st.expander("📖 View Full Chat History"):
    for msg in st.session_state.chat_history[1:]:
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div style='text-align: right; background-color: #000000; padding: 10px 15px; border-radius: 10px; margin: 5px 0; display: inline-block; max-width: 80%; float: right; clear: both;'>
                    <strong>You:</strong> {msg['content']}
                </div>
                """,
                unsafe_allow_html=True
            )
        elif msg["role"] == "assistant":
            st.markdown(
                f"""
                <div style='text-align: left; background-color: #000000; padding: 10px 15px; border-radius: 10px; margin: 5px 0; display: inline-block; max-width: 80%; float: left; clear: both;'>
                    <strong>Bot:</strong> {msg['content']}
                </div>
                """,
                unsafe_allow_html=True
            )