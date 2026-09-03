# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- API keys for AI services:
  - OpenAI API key (for ChatGPT)
  - Google Gemini API key (optional)
  - Anthropic Claude API key (optional)

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mutingwendeanashestella-commits/AI-Productivity-Assistant.git
cd AI-Productivity-Assistant
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

```bash
# Copy the example configuration file
cp config/api_keys.env.example config/api_keys.env

# Edit the file and add your API keys
# Open config/api_keys.env and replace placeholder values with your actual keys
```

**Getting API Keys:**

- **OpenAI**: Visit https://platform.openai.com/api-keys
- **Google Gemini**: Visit https://makersuite.google.com/app/apikey
- **Anthropic**: Visit https://console.anthropic.com/

### 5. Verify Installation

```bash
# Test the installation
python main.py
```

You should see the main menu of the AI Productivity Assistant.

## Troubleshooting

### ModuleNotFoundError
If you get `ModuleNotFoundError`, ensure:
- Virtual environment is activated
- All dependencies are installed: `pip install -r requirements.txt`

### API Key Issues
If you get API authentication errors:
- Verify API keys are correctly set in `config/api_keys.env`
- Ensure the `.env` file is in the root directory
- Check that you have sufficient API credits/quotas

### OpenAI API Errors
- Verify your API key is valid
- Check your OpenAI account has available credits
- Ensure you're using the correct API endpoint

## Usage

Run the application:

```bash
python main.py
```

Choose from the menu:
1. Email Generation
2. Meeting Summarization
3. Task Planning
4. Research Assistance
5. Productivity Chatbot
6. Exit

## Next Steps

- Read the [USAGE_GUIDE.md](USAGE_GUIDE.md) for detailed feature documentation
- Check [PROMPT_ENGINEERING.md](PROMPT_ENGINEERING.md) for prompt optimization tips
- Review the project structure in [README.md](../README.md)
