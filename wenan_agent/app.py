import streamlit as st
import os
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 页面配置
st.set_page_config(page_title="AI爆款文案生成器", page_icon="✍️")

# 侧边栏配置
with st.sidebar:
    st.header("⚙️ 配置")
    api_key = st.text_input("请输入 DashScope API Key", type="password")
    model_name = st.selectbox("选择模型", ["qwen-plus", "qwen-max", "qwen-turbo"], index=0)
    st.markdown("---")
    st.markdown("基于 **LangChain + 通义千问** 构建")

# 主界面
st.title("🔥 AI 爆款文案生成助手")
st.subheader("输入关键词，一键生成小红书/抖音风格文案")

# 用户输入
keyword = st.text_input("请输入产品或主题关键词", placeholder="例如：平价洗面奶、杭州旅游攻略...")
style_option = st.selectbox("选择文案风格", ["小红书种草风", "抖音口播风", "朋友圈营销风"])

# 生成逻辑
def get_prompt_template(style):
    if style == "小红书种草风":
        return """
        你是一名小红书博主。请根据关键词【{keyword}】写一篇笔记。
        要求：
        1. 标题要带Emoji，使用“震惊体”或“干货体”。
        2. 正文多用Emoji，口语化，像闺蜜聊天。
        3. 包含痛点+解决方案。
        4. 文末加Tags。
        """
    elif style == "抖音口播风":
        return """
        你是一名抖音短视频编剧。请根据关键词【{keyword}】写一段口播脚本。
        要求：
        1. 开头前3秒必须有黄金钩子（引起好奇）。
        2. 句式短促有力，适合快节奏朗读。
        3. 结尾要有明确的引导点赞关注话术。
        """
    else:
        return """
        你是一名私域流量营销专家。请根据关键词【{keyword}】写一条朋友圈文案。
        要求：
        1. 亲切自然，不要太硬广。
        2. 突出限时福利或核心价值。
        3. 引导私聊或评论。
        """

if st.button("开始生成 ✨"):
    if not api_key:
        st.warning("请先在左侧输入 API Key")
    elif not keyword:
        st.warning("请输入关键词")
    else:
        os.environ["DASHSCOPE_API_KEY"] = api_key
        
        with st.spinner("AI 正在疯狂创作中..."):
            try:
                
                llm = ChatTongyi(model=model_name)
                
                
                template_str = get_prompt_template(style_option)
                prompt = ChatPromptTemplate.from_template(template_str)
                
                
                chain = prompt | llm | StrOutputParser()
                result = chain.invoke({"keyword": keyword})
                
                
                st.success("生成成功！")
                st.text_area("生成结果", value=result, height=400)
                
            except Exception as e:
                st.error(f"发生错误: {e}")