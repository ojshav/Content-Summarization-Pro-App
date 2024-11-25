import streamlit as st
import validators
from langchain_groq import ChatGroq
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from yt_dlp import YoutubeDL
from langchain_core.documents import Document

# Page Configuration
st.set_page_config(
    page_title="Content Summarizer Pro",
    page_icon="📝",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f0f8ff;
        border: 1px solid #e1e4e8;
        color: #000000;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/000000/video-playlist.png", width=100)
    st.title("⚙️ Settings")
    model_name = st.selectbox(
        "Select Model",
        ["Gemma-7b-it", "llama-3.1-8b-instant", "llama-3.1-70b-versatile"]
    )
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This app helps you summarize:
    - YouTube Videos 🎥
    - Web Articles 📰
    """)

# Main App
st.title("🎯 Content Summarizer Pro")
st.markdown("### 📊 Get quick summaries of videos and articles")

# Input Section
input_type = st.radio(
    "Select Content Type",
    ["YouTube Video", "Web Article"],
    horizontal=True
)

url = st.text_input(
    "Enter URL",
    placeholder="Paste your YouTube video or article URL here..."
)

# Initialize LLM
@st.cache_resource
def get_llm(api_key, model):
    return ChatGroq(api_key=api_key, model_name=model, streaming=True)

# Prompts
youtube_prompt = """
You are a professional content summarizer specialized in YouTube videos.

Video Content:
{text}

Please provide a comprehensive summary including:
1. Main Topic and Key Points
2. Important Details and Examples
3. Key Takeaways
4. Timestamps of important moments (if available)

Make the summary engaging and well-structured.
"""

article_prompt = """
You are a professional content summarizer specialized in web articles.

Article Content:
{text}

Please provide a comprehensive summary including:
1. Main Topic and Key Points
2. Important Arguments and Evidence
3. Key Conclusions
4. Notable Quotes or Statistics

Make the summary engaging and well-structured.
"""

if url:
    if not validators.url(url):
        st.error("🚫 Please enter a valid URL")
        st.stop()

    if st.button("🚀 Generate Summary"):
        groq_api_key = st.secrets["GROQ_API_KEY"]

        try:
            with st.spinner("🔄 Processing content..."):
                # Initialize LLM
                llm = get_llm(groq_api_key, model_name)
                
                # Process based on content type
                if input_type == "YouTube Video" and ("youtube.com" in url or "youtu.be" in url):
                    progress_bar = st.progress(0)
                    st.markdown("#### 📥 Downloading video information...")
                    
                    ydl_opts = {
                        'writesubtitles': True,
                        'subtitlesformat': 'txt',
                        'skip_download': True,
                        'quiet': True
                    }
                    
                    with YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=False)
                        transcript = info.get('subtitles', {}).get('en', [{}])[0].get('data', '')
                        if not transcript:
                            transcript = info.get('description', '')
                        
                        # Display video info
                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(info.get('thumbnail', ''), use_container_width=True)
                        with col2:
                            st.markdown(f"**Title:** {info.get('title', '')}")
                            st.markdown(f"**Duration:** {info.get('duration_string', '')}")
                            st.markdown(f"**Channel:** {info.get('channel', '')}")
                        
                        docs = [Document(
                            page_content=transcript,
                            metadata={"title": info.get('title', ''),
                                     "source": url}
                        )]
                        
                        progress_bar.progress(50)
                        PROMPT = PromptTemplate(template=youtube_prompt, input_variables=["text"])
                else:
                    st.markdown("#### 📥 Downloading article content...")
                    try:
                        loader = UnstructuredURLLoader(
                            urls=[url],
                            ssl_verify=False,
                            headers={"User-Agent": "Mozilla/5.0"}
                        )
                        docs = loader.load()
                        
                        # Check if content was successfully loaded
                        if not docs or len(docs) == 0:
                            st.error("❌ Unable to extract content from this article. Please check if the URL is accessible.")
                            st.stop()
                            
                        PROMPT = PromptTemplate(template=article_prompt, input_variables=["text"])

                    except Exception as e:
                        st.error(f"❌ Failed to load article content: {str(e)}")
                        st.markdown("Please check if:")
                        st.markdown("- The URL is accessible")
                        st.markdown("- The website allows content extraction")
                        st.markdown("- The article is not behind a paywall")
                        st.stop()

                # Split and summarize
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,
                    chunk_overlap=100,
                    length_function=len
                )
                texts = text_splitter.split_documents(docs)

                chain = load_summarize_chain(
                    llm=llm,
                    chain_type="refine",
                    question_prompt=PROMPT,
                    refine_prompt=PROMPT,
                    verbose=True
                )

                summary = chain.run(texts)
                
                # Display summary in a nice format
                st.markdown("### 📋 Summary")
                st.markdown("""
                    <div class="success-box" style="color: black;">
                        {}
                    </div>
                """.format(summary), unsafe_allow_html=True)
                
                # Add download button for summary
                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )

        except Exception as e:
            if "YouTube" in str(e):
                st.error("❌ Error accessing YouTube video. Please check if the video exists and is publicly available.")
            else:
                st.error(f"❌ An error occurred: {e}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Made with ❤️ by Ojshav Saxena</p>
    </div>
    """,
    unsafe_allow_html=True
)






  





