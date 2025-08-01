import os
from typing import Dict, List, Any
import openai
from shiny import App, ui, render, reactive
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# App UI
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.h4("Model Parameters"),
        ui.input_select(
            "base_url",
            "Base URL:",
            {
                "https://api.siliconflow.cn/v1": "SiliconFlow",
                "https://api.deepseek.com/v1": "DeepSeek",
                "https://api.openai.com/v1": "OpenAI",
            },
            selected="https://api.siliconflow.cn/v1"
        ),
        ui.input_text("model_name", "Model Name:", value="Qwen/Qwen2.5-7B-Instruct"),
        ui.input_password("api_key", "API Key", value=""),
        width=300
    ),
    ui.page_fluid(
        ui.h1("AI Chat Interface"),
        ui.card(
            ui.chat_ui("chat")  # Chat UI component
        )
    )
)

# App Server
def server(input, output, session):
    # Initialize the chat
    chat = ui.Chat(
        id="chat",
        messages=[
            "Hello! I'm an AI assistant. I'm configured to use the Qwen/Qwen2.5-7B-Instruct model on SiliconFlow. How can I help you today?"
        ]
    )
    
    @reactive.effect
    @reactive.event(input.api_key, input.base_url, input.model_name)
    def update_api_config():
        """Update the API configuration when parameters change"""
        if input.api_key():
            # This effect runs when any of the input values change
            pass
    
    @chat.on_user_submit
    async def handle_user_input():
        """Handle user input and generate AI response"""
        user_message = chat.user_input()
        logger.info(f"User: {user_message}")
        
        # Get API configuration
        api_key = input.api_key()
        base_url = input.base_url()
        model_name = input.model_name()
        
        # Validate API configuration
        if not api_key:
            await chat.append_message("Please enter your API key in the sidebar.")
            return
            
        try:
            # Create OpenAI client
            client = openai.OpenAI(
                api_key=api_key,
                base_url=base_url
            )
            
            # Prepare messages for API call (including conversation history)
            messages = chat.messages()
            
            # Make API call with streaming
            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                stream=True
            )
            
            # Stream the response
            await chat.append_message_stream(response)
            
        except openai.APIError as e:
            error_msg = f"API Error: {str(e)}"
            logger.error(error_msg)
            await chat.append_message(error_msg)
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            logger.error(error_msg)
            await chat.append_message(error_msg)

# Create the app
app = App(app_ui, server)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)