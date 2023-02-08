import openai
import gradio as gr

from config import api_key


openai.api_key = api_key


def chatbot(text):
    return openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    ).choices[0].text.strip()


def gradio_interface(prompt, history=[]):
    output = chatbot(prompt)
    history.append((prompt, output))
    return history, history


def main():
    gr.Interface(fn=gradio_interface,
                 inputs=["text", 'state'],
                 outputs=["chatbot", 'state']).launch(debug=False, share=False)


if __name__ == '__main__':
    main()
