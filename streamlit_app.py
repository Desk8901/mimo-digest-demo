import os
import time

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

DEFAULT_BASE_URL = "https://api.xiaomimimo.com/v1"
DEFAULT_MODEL = "mimo-v2.5-pro"
DEFAULT_INPUT = """请把下面内容处理成 3 个部分：
1. 150 字以内执行摘要
2. 3-5 条行动项
3. Mermaid 思维导图代码

原文：
最近我们在梳理一个提醒功能改版，目标是提升用户创建提醒后的到达率和完成率。
目前问题包括：入口分散、文案不清晰、用户不知道提醒是否创建成功、历史提醒和新提醒混在一起导致辨识度不高。
我们计划新增创建成功反馈、统一入口、补充提醒类型说明，并在消息触达后增加二次确认机制。"""


def build_client(api_key: str, base_url: str) -> OpenAI:
    return OpenAI(api_key=api_key, base_url=base_url)


def generate_digest(
    api_key: str,
    base_url: str,
    model_name: str,
    temperature: float,
    user_text: str,
) -> tuple[str, float]:
    client = build_client(api_key, base_url)
    started_at = time.perf_counter()

    response = client.chat.completions.create(
        model=model_name,
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": (
                    "你是一个帮助产品、研究和知识整理场景提炼信息的 AI 助手。"
                    "请输出结构清晰、可执行、可复用的结果。"
                ),
            },
            {"role": "user", "content": user_text},
        ],
    )

    elapsed = time.perf_counter() - started_at
    content = response.choices[0].message.content or ""
    return content.strip(), elapsed


st.set_page_config(page_title="MiMo Digest Demo", layout="wide")

st.markdown(
    """
    <style>
    .main { background-color: #f7f8fa; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #ff5a3d;
        color: white;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.title("MiMo Console")
    api_key = st.text_input(
        "MiMo API Key",
        type="password",
        value=os.getenv("MIMO_API_KEY", ""),
    )
    base_url = st.text_input(
        "Base URL",
        value=os.getenv("MIMO_BASE_URL", DEFAULT_BASE_URL),
    )
    model_name = st.text_input(
        "Model Name",
        value=os.getenv("MIMO_MODEL", DEFAULT_MODEL),
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.3, 0.1)
    st.caption("Uses the OpenAI-compatible MiMo API endpoint.")

st.header("MiMo Long-Text Digest Demo")
st.caption(
    "Convert long-form text into an executive summary, action items, and Mermaid mind map output."
)

left_col, right_col = st.columns([1, 1])

with left_col:
    input_text = st.text_area(
        "Input Text",
        value=DEFAULT_INPUT,
        height=360,
        help="Paste requirement docs, meeting notes, research text, or other long content.",
    )
    process_btn = st.button("Run with MiMo")

with right_col:
    if process_btn:
        if not input_text.strip():
            st.warning("Please enter the content you want to process.")
        elif not api_key.strip():
            st.warning("Please enter your MiMo API key.")
        else:
            try:
                with st.spinner("Calling MiMo API..."):
                    result_text, elapsed = generate_digest(
                        api_key=api_key.strip(),
                        base_url=base_url.strip(),
                        model_name=model_name.strip(),
                        temperature=temperature,
                        user_text=input_text.strip(),
                    )

                st.success("Generation succeeded. The result below is returned from the model.")
                st.markdown(result_text)

                with st.expander("Validation Details", expanded=True):
                    st.write(
                        {
                            "model": model_name.strip(),
                            "base_url": base_url.strip(),
                            "elapsed_seconds": round(elapsed, 2),
                            "input_characters": len(input_text.strip()),
                            "output_characters": len(result_text),
                        }
                    )
            except Exception as exc:
                st.error("Request failed. Check your API key, base URL, and model name.")
                st.code(str(exc))
    else:
        st.info("Click the button to generate a real output via the MiMo API.")

st.divider()
st.markdown("### Quick Validation")
metric_col1, metric_col2, metric_col3 = st.columns(3)
metric_col1.metric("Input Characters", len(input_text.strip()))
metric_col2.metric("Default Model", model_name.strip() or DEFAULT_MODEL)
metric_col3.metric("Base URL", base_url.strip() or DEFAULT_BASE_URL)
