import gradio as gr
from openai import OpenAI

# OpenAI API 설정
client = OpenAI(
    api_key="key",
)

# 봇의 안내 지침 설정
instructions = """
#봇 정보
- 내담자의 감정을 이해하고 위로하며, 심리적 안정을 제공하는 역할을 해야해
- 내담자의 고민에 깊이 공감하고, 그들의 감정을 비판 없이 받아들여줘
- 내담자의 상황에 맞는 적절한 해결책을 제시하고, 현실적인 도움을 줘야해
- 내담자의 회복 과정에 동기를 부여하고, 긍정적인 회복 가능성을 제시해줘
- 내담자가 실질적인 변화를 이룰 수 있도록 구체적인 실행 계획을 제시하고, 그 과정을 지원해줘
"""

# OpenAI API로 챗봇 응답 생성 함수
def chat_response(text):
    messages = [
        {
            "role": "system",
            "content": instructions,
        },
        {
            "role": "user",
            "content": text,
        }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return chat_completion.choices[0].message.content

# Gradio 인터페이스 설정
iface = gr.Interface(
    fn=chat_response,
    inputs="text",
    outputs="text",
    title="심리 상담 챗봇",
    description="내담자의 감정을 이해하고 위로하며 심리적 안정을 제공하는 상담 챗봇입니다. 고민을 입력하세요."
)

# Gradio 인터페이스 실행
iface.launch(share=True)