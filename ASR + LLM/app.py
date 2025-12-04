import streamlit as st
from faster_whisper import WhisperModel
from openai import OpenAI
import os
import tempfile

# ================= 配置区域 =================
# 1. 配置通义千问 (Qwen)
# 阿里云 DashScope 兼容 OpenAI 格式的接口
# 获取 Key 地址: https://bailian.console.aliyun.com/
client = OpenAI(
    api_key="sk-395e24bde759444382abbf4cbb94b0b7",  # 🔴 请替换为你的阿里云 DashScope API Key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 🔴 通义千问兼容接口地址
)

# 2. 加载 Whisper 模型 (本地运行)
# 第一次运行会自动下载模型到本地缓存
@st.cache_resource
def load_whisper():
    device="cpu" 
    # 如果你有 NVIDIA 显卡，请改为 device="cuda" 速度会快几十倍
    return WhisperModel("medium", device="cpu", compute_type="int8")

model = load_whisper()

# ================= 功能函数 =================

# 语音转文字 (STT)
def transcribe_audio(file_path):
    beam_size=5 
    segments, info = model.transcribe(file_path, beam_size=5)
    full_text = ""
    
    # 创建进度条
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Whisper 是流式生成的，我们需要遍历 segments
    segment_list = list(segments) 
    total_segments = len(segment_list)
    
    for i, segment in enumerate(segment_list):
        
        full_text += f"[{segment.start:.0f}s -> {segment.end:.0f}s] {segment.text}\n"
        
        if total_segments > 0:
            progress_bar.progress((i + 1) / total_segments)
            
    status_text.text("转写完成！")
    return full_text

# AI 整理 (LLM - 通义千问)
def summarize_meeting(raw_text):
    prompt = f"""
    你是一个专业的会议记录秘书。请根据以下识别出的会议原始文本，生成一份结构化的会议纪要。
    
    要求：
    1. 修正明显的语音识别错误（例如同音字）和口语废话（如“嗯、啊、那个”）。
    2. 提取【会议主题】。
    3. 总结【主要内容】（分点阐述）。
    4. 列出【待办事项/Action Items】（必须包含负责人，如果没有提到具体人名则标记为待定）。
    5. 语气专业、客观，不要编造未提及的内容。

    原始文本：
    {raw_text}
    """
    
    try:
        response = client.chat.completions.create(
            model="qwen-plus", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3  
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI 总结出错: {str(e)}"

# ================= UI 界面 =================
st.set_page_config(page_title="会议纪要助手 (Qwen版)", page_icon="📝")

st.title("🎙️ 智能会议纪要生成 Agent")
st.caption("Powered by Faster-Whisper (本地转写) + 通义千问 (云端整理)")

uploaded_file = st.file_uploader("上传会议录音 (支持 mp3, wav, m4a)", type=['mp3', 'wav', 'm4a'])

if uploaded_file is not None:
    # 保存临时文件
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    st.audio(uploaded_file)
    
    if st.button("🚀 开始生成纪要"):
        
        # 1. 语音转文字
        with st.spinner("正在转写语音，请稍候... (本地运算取决于电脑性能)"):
            raw_text = transcribe_audio(tmp_path)
            
        with st.expander("👀 查看原始识别结果 (逐字稿)", expanded=False):
            st.text_area("Raw Text", raw_text, height=200)
        
        # 2. AI 整理
        with st.spinner("正在呼叫通义千问整理文档..."):
            summary = summarize_meeting(raw_text)
            
            st.divider()
            st.markdown("### 📝 会议纪要")
            st.markdown(summary)
            
            # 提供下载
            st.download_button(
                label="📥 下载 Markdown 文档",
                data=summary,
                file_name="meeting_notes.md",
                mime="text/markdown"
            )

    # 清理临时文件
    try:
        os.remove(tmp_path)
    except:
        pass