# 📰 News Research Tool  

## 📌 Description  
The News Research Tool is a Streamlit-based chatbot that helps users interactively explore and analyze news articles. By entering article URLs, users can ask questions and receive AI-generated answers, along with references to the original content.  

## 🚀 Features  
- Input up to **3 news article URLs**.  
- Automatic text extraction, cleaning, and chunking.  
- Semantic embeddings with **HuggingFace MiniLM-L6-v2**.  
- Vector search using **FAISS**.  
- Q&A with **Google Gemini (via LangChain)**.  
- Displays both answers and source excerpts.  

## 🛠 Tech Stack  
- **Python**  
- **Streamlit** – for the web interface  
- **LangChain** – for retrieval & LLM chaining  
- **Google Gemini (via langchain_google_genai)** – for question answering  
- **HuggingFace Embeddings** – for semantic vectorization  
- **FAISS** – for efficient similarity search  
- **dotenv** – for API key management  

## ⚙️ Installation & Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/news-research-tool.git
   cd news-research-tool
   ```

2. **Create a virtual environment (recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   Create a `.env` file in the project root:  
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```

5. **Run the Streamlit app**  
   ```bash
   streamlit run app.py
   ```

## 💡 Usage  
1. Open the Streamlit app in your browser.  
2. Enter up to 3 news article URLs in the sidebar.  
3. Click **Process URLs** to load and embed the content.  
4. Ask questions in the input box.  
5. View AI-generated answers with source excerpts.  

## 🔮 Future Improvements  
- Support for more than 3 URLs.  
- Save conversation history.  
- Add multi-language support.  
- Deploy on cloud (e.g., Streamlit Cloud, Heroku).  

## 📜 License  
This project is licensed under the MIT License.  
