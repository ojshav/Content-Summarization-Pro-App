# Content Summarizer Pro 📝

A powerful Streamlit application that generates comprehensive summaries of YouTube videos and web articles using advanced language models. Try it out at [Content Summarizer Pro](https://content-summarization-pro-app-az3qwm8zf8gcpkvkbbzhqd.streamlit.app/)!

## Features 🌟

- **Dual Content Support**: Summarizes both YouTube videos and web articles
- **Multiple LLM Options**: Choose between different language models:
  - Gemma-7b-it
  - llama-3.1-8b-instant
  - mixtral-8x7b-32768
- **Smart Processing**: Automatically handles different content types
- **Rich Summaries**: Provides structured summaries with key points and insights
- **Download Option**: Export summaries as text files
- **User-Friendly Interface**: Clean, intuitive design with progress indicators

## How It Works 🔧

### For YouTube Videos 🎥

1. Extracts video information including:
   - Title
   - Duration
   - Channel name
   - Thumbnail
   - Subtitles/Description
2. Processes the content using the selected language model
3. Generates a summary including:
   - Main Topic and Key Points
   - Important Details and Examples
   - Key Takeaways
   - Timestamps of important moments

### For Web Articles 📰

1. Downloads article content using UnstructuredURLLoader
2. Processes the text using the selected language model
3. Generates a summary including:
   - Main Topic and Key Points
   - Important Arguments and Evidence
   - Key Conclusions
   - Notable Quotes or Statistics

## Technical Implementation 🛠️

- **Frontend**: Built with Streamlit
- **LLM Integration**: Uses Groq API through LangChain
- **Text Processing**:
  - RecursiveCharacterTextSplitter (chunk_size=1000, overlap=100)
  - Custom prompt templates for different content types
  - Refine chain type for improved summary quality
- **Video Processing**: Uses yt-dlp for YouTube video information extraction
- **Web Scraping**: UnstructuredURLLoader with custom headers for article extraction

## Requirements 📋

- Python 3.7+
- streamlit
- langchain
- langchain-groq
- yt-dlp
- validators
- Groq API key

## Environment Setup 🔑

1. Create a `.streamlit/secrets.toml` file
2. Add your Groq API key:


## Usage 💡

1. Visit [Content Summarizer Pro](https://content-summarization-pro-app-az3qwm8zf8gcpkvkbbzhqd.streamlit.app/)
2. Select content type (YouTube Video or Web Article)
3. Paste the URL
4. Choose your preferred language model from the sidebar
5. Click "🚀 Generate Summary"
6. View the generated summary in a clean, formatted box
7. Download the summary as a text file if needed

## Error Handling ⚠️

The application includes robust error handling for:
- Invalid URLs
- Inaccessible YouTube videos
- API failures
- Content processing issues

## Styling 🎨

Custom CSS is implemented for:
- Responsive layout
- Clean button design
- Attractive summary display
- Professional typography

## Credits 👏

Created by Ojshav Saxena

---

Feel free to contribute or report issues!

![WhatsApp Image 2024-11-25 at 23 04 06_730a3c22](https://github.com/user-attachments/assets/24841527-de8e-45ff-be73-44ce2f5719b6)

![WhatsApp Image 2024-11-25 at 23 04 37_ae97da92](https://github.com/user-attachments/assets/cc92d9fc-9e0f-4baf-a8e6-63b70332c046)

![WhatsApp Image 2024-11-25 at 23 05 35_435adf8a](https://github.com/user-attachments/assets/193bc907-a2db-456f-a5bf-f45ba514f34d)

![WhatsApp Image 2024-11-25 at 23 05 49_6d1a7d8a](https://github.com/user-attachments/assets/5ea2c157-e809-42a7-b9c9-fc8a93a41f21)



