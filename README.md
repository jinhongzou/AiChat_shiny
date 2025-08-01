# AI Chat Application

This is an AI chat application built with Python Shiny that integrates with OpenAI-compatible APIs, specifically configured to use the Qwen/Qwen2.5-7B-Instruct model hosted on the SiliconFlow platform.

## Features

- AI Chat Interface with real-time message streaming
- Integration with OpenAI-compatible APIs
- Support for multiple models and platforms
- Conversation history management
- Comprehensive error handling
- Responsive UI/UX design

## Prerequisites

- Python 3.9+ (Python 3.12+ recommended)
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AiChat_shiny
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Get an API key from SiliconFlow or another supported platform
2. In the application, enter your API key in the sidebar
3. Select the appropriate base URL and model name

## Running the Application

```bash
python src/app.py
```

The application will start on `http://localhost:8000`

## Usage

1. Enter your message in the input field at the bottom
2. Click "Send" or press Enter to send the message
3. View the AI response in the chat area
4. Adjust model parameters in the sidebar as needed

## Supported Platforms

- SiliconFlow (https://api.siliconflow.cn/v1)
- DeepSeek (https://api.deepseek.com/v1)
- OpenAI (https://api.openai.com/v1)

## Models

- Qwen/Qwen2.5-7B-Instruct (default)
- Other models can be specified in the model name field

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.