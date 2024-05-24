from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
import os


def generate_script(api_key, video_length, creativity, subject):
    subject_template = ChatPromptTemplate.from_messages([
        ("human", "请给关于{subject}主题的视频起一个标题")
    ])
    script_template = ChatPromptTemplate.from_messages([
        ("human", "根据以下信息，写一个视频脚本/"
                  "###/"
                  "视频长度{video_length}分钟，{title}为标题，维基百科参考资料{wiki_search}/"
                  "###")
    ])
    wikipedia_api_wrapper = WikipediaAPIWrapper(lang="zh")
    wiki_search = wikipedia_api_wrapper.run(subject)
    model = ChatOpenAI(api_key=api_key, temperature=creativity, base_url="https://jiekou.wlai.vip/v1")
    subject_template_model_chain = subject_template | model
    script_template_model_chain = script_template | model
    video_title = subject_template_model_chain.invoke({"subject": subject}).content
    video_script = script_template_model_chain.invoke(
        {"video_length": video_length, "title": video_title, "wiki_search": wiki_search}).content
    return wiki_search, video_title, video_script


# result = generate_script(api_key=os.getenv("OPENAI_API_KEY"), video_length=0.2, creativity=1.3, subject="sora模型")
#
# print(result)
