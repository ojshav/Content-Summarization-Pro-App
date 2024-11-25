# Content Summarizer Pro 📝

A powerful Streamlit application that generates comprehensive summaries of YouTube videos and web articles using advanced language models.

## Features 🌟

- **Dual Content Support**: Summarizes both YouTube videos and web articles
- **Multiple LLM Options**: Choose between different language models:
  - Gemma-7b-it
  - mixtral-8x7b-32768
  - llama2-70b-4096
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
  - RecursiveCharacterTextSplitter for chunking large texts
  - Custom prompt templates for different content types
  - Refine chain type for improved summary quality

## Requirements 📋

- Python 3.7+
- Streamlit
- LangChain
- yt-dlp
- validators
- Groq API key

## Environment Setup 🔑

1. Create a `.streamlit/secrets.toml` file
2. Add your Groq API key:


## Usage 💡

1. Select content type (YouTube Video or Web Article)
2. Paste the URL
3. Choose your preferred language model
4. Click "Generate Summary"
5. View the generated summary
6. Download the summary if needed

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
