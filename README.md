# Policy document chat

- Streamlit PoC to ask questions about a policy document.
- Example document available [here](https://static.aviva.io/content/dam/document-library/health/gen6843.pdf)


## Copying Claude

This can be done in the Claude app - and trying this out gives pretty helpful clues as to what might be going on.

When you upload the pdf to Claude - it gets converted to text. This looks like a pretty basic pdf text extraction that's not particularly well formatted.

<image src="./pics/claude_screenshot.png" />

## Document chat PoC

Based on the above - this repo implements a simple LLM chat with the text extracted from a pdf given as context to the model. The whole flow is:

- Extract text from pdf using `PyPDF2`
- Add a system prompt to the model calls - instructing it to answer questions based on the document.
- Provide the document as context in the first `user` message.
- Add subsequent `user` messages and `assistant` responses to the message list to be sent in the model call.

## Repo setup

- Clone the repo and run `uv sync`

## Running the app

- Activate the virtual environemnt (e.g. `source .venv/bin/activate`)
- Run

    ```streamlit run src/policy_explainer/app.py```
