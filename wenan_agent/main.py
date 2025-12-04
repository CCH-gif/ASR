import os
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


os.environ["DASHSCOPE_API_KEY"] = ""

def generate_viral_copy(keyword):
    
    llm = ChatTongyi(model="qwen-max") 

    
    
    template = """
    你是一名拥有10年经验的社交媒体爆款文案专家，深谙用户心理学和平台算法机制。
    请根据用户提供的【关键词】，撰写一篇容易产生高点击、高互动的“小红书风格”文案。

    【用户关键词】：{keyword}

    【文案要求】：
    1. **标题**：必须极具吸引力，包含悬念、痛点或强烈的情绪价值。使用二极管标题法（例如：“后悔没早买...”、“这简直是...的天花板”），加上适当的Emoji。
    2. **正文结构**：
       - 开头：用痛点或场景代入，通过共情瞬间抓住眼球。
       - 中间：干货输出或产品种草，分点叙述，条理清晰。
       - 结尾：互动引导（求关注、求评论），引发讨论。
    3. **排版**：多分段，短句为主，每段之间加入空行，大量使用适合语境的Emoji表情，增加视觉愉悦感。
    4. **标签**：文末生成5-8个高热度相关Hashtag。

    请直接输出文案内容，不要输出任何解释性文字。
    """

    prompt = ChatPromptTemplate.from_template(template)

   
    chain = prompt | llm | StrOutputParser()

   
    try:
        result = chain.invoke({"keyword": keyword})
        return result
    except Exception as e:
        return f"生成出错: {e}"

# --- 测试运行 ---
if __name__ == "__main__":
    user_input = input("请输入文案关键词（例如：防晒霜、职场穿搭、减肥食谱）：")
    print("\n正在生成爆款文案...\n")
    copywriting = generate_viral_copy(user_input)
    print("-" * 30)
    print(copywriting)
    print("-" * 30)