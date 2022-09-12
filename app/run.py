import sys, os
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from NoPilot import GPT2


@st.cache(hash_funcs={GPT2: lambda _: None})
def load_model():
    return GPT2()


def app():
    gpt2 = load_model()

    st.title("NoPilot")

    text = st.text_input("")
    topk = st.slider("Display Number", 1, 10, 5)
    if text:
        with st.spinner("Loading..."):
            prediction = gpt2.predict_next(text, topk)

        expander = st.beta_expander("View Results", expanded=True)
        for index, word in enumerate(prediction):
            expander.write(f"{index}. {word}")


if __name__ == "__main__":
    app()
