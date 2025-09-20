# Językowy AI Czat 💬

A Streamlit-based language learning chatbot application that helps users learn foreign languages through interactive conversations with AI tutors.

## Features

- **Multi-language support**: Learn English, French, or Italian
- **Personalized tutoring**: Choose between different tutor styles (Friend, Girlfriend, Professor)
- **Adaptive learning**: AI adapts to your proficiency level (A1/A2, B1/B2, C1/C2)
- **Interactive games**: Language learning through fun games like Guess Who?, Scattergories, etc.
- **Custom tutor images**: Upload your own tutor image
- **OpenAI GPT integration**: Powered by GPT-3.5 and GPT-4 models

## Requirements

- Python 3.7+
- Streamlit
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/norbertkocon94/chatbot_ai.git
cd chatbot_ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run streamlit_app.py
```

## Usage

1. **Configure your learning preferences**:
   - Select the language you want to learn
   - Choose your proficiency level
   - Pick a tutor style that suits you
   - Enter your tutor's name
   - Select GPT model (3.5 or 4)

2. **Enter your OpenAI API key**:
   - You need a valid OpenAI API key to use the chatbot
   - Get your key from: https://platform.openai.com/overview

3. **Start learning**:
   - Type messages to interact with your AI tutor
   - The tutor will adapt to your language and learning style
   - Try the suggested language games for fun learning

## File Structure

- `streamlit_app.py` - Main application file with UI and chatbot logic
- `ai_config.py` - Configuration file with tutor descriptions and image paths
- `requirements.txt` - Python dependencies
- `Images/` - Directory containing tutor and team member images

## Configuration

The application supports three tutor styles:

- **Kolega (Friend)**: Casual, informal conversation style for beginners
- **Przyjaciółka (Girlfriend)**: Cheerful, optimistic style for intermediate learners  
- **Profesor (Professor)**: Formal, academic style for advanced learners

## Team

- **Norbert**: AI Researcher, Data Scientist at NorthGravity
- **Dagmara**: Business Analyst, CEO at AI Chat
- **Alicja**: Data Scientist Candidate, Digitalisation Methods and Tools Engineer at Technip Energies

## Important Notes

- **Paid service**: Using the chatbot requires OpenAI API credits
- **Privacy**: Your conversations are processed through OpenAI's API
- **Languages**: Currently supports English, French, and Italian learning

## License

This project is for educational and demonstration purposes.