import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class LLM:
    """
    A factory class to provide the LLM for a LangGraph workflow.
    Designed to easily swap between Gemini, GigaChat, or others.
    """
    def __init__(self, provider: str = "gemini", model_name: str = "gemini-2.5-flash"):
        self.provider = provider.lower()
        self.model_name = model_name
        self.client = self._initialize_llm()

    def _initialize_llm(self):
        if self.provider == "gemini":
            from langchain_google_genai import ChatGoogleGenerativeAI
            
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("GOOGLE_API_KEY not found in .env file.")
            
            # Returns a standard LangChain BaseChatModel
            return ChatGoogleGenerativeAI(
                model=self.model_name,
                api_key=api_key,
                temperature=0.0 # Standard for agentic workflows, adjust if needed
            )
            
        elif self.provider == "gigachat":
            # For later: pip install gigachat
            # from langchain_community.chat_models import GigaChat
            
            # credentials = os.getenv("GIGACHAT_CREDENTIALS")
            # return GigaChat(credentials=credentials, verify_ssl_certs=False)
            raise NotImplementedError("GigaChat is not fully set up yet.")
            
        else:
            raise ValueError(f"Unsupported LLM provider: {self.provider}")
    def get_embedding_model(self, model_name: str = "gemini-embedding-001"):
        """Returns the Embedding Model"""
        if self.provider == "gemini":
            from langchain_google_genai import GoogleGenerativeAIEmbeddings
            return GoogleGenerativeAIEmbeddings(
                model=model_name,
                google_api_key=os.getenv("GOOGLE_API_KEY"),
                
            )
        elif self.provider == "gigachat":
            # from langchain_community.embeddings.gigachat import GigaChatEmbeddings
            # return GigaChatEmbeddings(credentials=os.getenv("GIGACHAT_CREDENTIALS"), verify_ssl_certs=False)
            raise NotImplementedError("GigaChat Embeddings not configured.")
        
    def get_model(self):
        """
        Returns the LangChain model instance to be used in LangGraph nodes.
        """
        return self.client

# ==========================================
# Example Usage in your LangGraph workflow:
# ==========================================
if __name__ == "__main__":
    # 1. Initialize with Gemini
    llm_manager = LLM(provider="gemini")
    chat_model = llm_manager.get_model()
    embedding_model = llm_manager.get_embedding_model()
    
    # Test the model
    # response = chat_model.invoke("Hello, who are you?")
    # print(response.content)
    embedding = embedding_model.embed_query("HEllo")
    print(embedding)
    
    # Later, when you want to switch to GigaChat, you just do:
    # llm_manager = LLM(provider="gigachat")
    # chat_model = llm_manager.get_model()