import anthropic
import streamlit as st

from policy_explainer.prompts import SYSTEM_PROMPT, INITIAL_QUESTION

from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

MODEL = "claude-3-5-haiku-20241022"

with open("data/health_ipd.txt", "r") as f:
    policy_document = f.read()

if __name__ == "__main__":
    st.title("Policy explainer")

    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append(
            {
                "role": "user",
                "content": INITIAL_QUESTION.format(document=policy_document),
            }
        )

    for message in st.session_state.messages[1:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question about the policy"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = client.messages.create(
            model=MODEL,
            system=SYSTEM_PROMPT,
            max_tokens=2048,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )
        content = response.content[0].text
        st.session_state.messages.append({"role": "assistant", "content": content})
        st.rerun()
