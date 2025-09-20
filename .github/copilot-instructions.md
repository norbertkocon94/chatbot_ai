# Language Learning AI Chatbot (Językowy AI Czat)

A Polish-language Streamlit web application for learning English, French, and Italian through interactive AI conversations with three distinct tutor personalities powered by OpenAI GPT models.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Bootstrap and Dependencies
- Install Python dependencies:
  - `pip install -r requirements.txt` -- installs streamlit==1.27.2 and openai==1.3.5 plus all dependencies
  - Installation takes 30-60 seconds depending on network speed
- **NEVER CANCEL**: Dependency installation may take up to 2 minutes on slower connections

### Build and Run
- **No build step required** -- this is a pure Python Streamlit application
- Run the application:
  - `streamlit run streamlit_app.py` -- starts on http://localhost:8501
  - `streamlit run streamlit_app.py --server.port 8501 --server.headless true` -- for headless/server environments
- **Application startup time**: 5-8 seconds. NEVER CANCEL before 15 seconds minimum
- **Health check**: Application responds with HTTP 200 on http://localhost:8501 when ready

### Testing and Validation
- **No automated test suite exists** -- validation is manual only
- **MANUAL VALIDATION REQUIREMENT**: Always test the following complete user scenario after making changes:
  1. Start the application with `streamlit run streamlit_app.py`
  2. Verify the sidebar loads with all 5 configuration options:
     - Language selection (Angielski/Francuski/Włoski)
     - Level selection (A1/A2, B1/B2, C1/C2)
     - Tutor selection (Kolega/Przyjaciółka/Profesor)
     - Tutor name input field
     - GPT model selection (GPT 3.5/GPT 4)
  3. Verify API key input field appears and is of type "password"
  4. Verify image upload widget works (accepts PNG, JPG, JPEG up to 200MB)
  5. Verify "Zatwierdź" (Confirm) and "Resetuj" (Reset) buttons are functional
  6. Expand the welcome section and verify all 3 tutor personality cards display with images
  7. Expand "O nas" (About us) section and verify all 3 team member profiles display
  8. **Without API key**: Verify error message appears requesting OpenAI API key
  9. **With valid API key**: Verify chat interface appears and can accept messages

### Dependencies and Environment
- **Python version**: Tested with Python 3.12+, requires 3.8+ minimum
- **Required packages** (see requirements.txt):
  - streamlit==1.27.2 (web framework)
  - openai==1.3.5 (GPT API client)
- **External API requirement**: OpenAI API key required for chat functionality
- **Network ports**: Application serves on port 8501 by default

## Key Architecture

### File Structure
- `streamlit_app.py` -- Main application entry point, UI, and chat logic
- `ai_config.py` -- Configuration for tutor personalities and image paths
- `requirements.txt` -- Python dependencies
- `Images/` -- Directory containing tutor and team member images (6 PNG files)
- `.devcontainer/` -- VS Code development container configuration

### Core Components
- **Sidebar**: User configuration form (language, level, tutor, API key)
- **Main area**: Welcome information, tutor descriptions, team profiles
- **Chat interface**: Appears after API key validation, supports OpenAI GPT-3.5 and GPT-4
- **Session management**: Maintains chat history with configurable window size (MAX_EXCHANGES = 3)

### Critical Configuration
- **Tutor personalities**: 3 distinct AI tutors with different conversation styles
  - Kolega (Friend): Informal, beginner-friendly
  - Przyjaciółka (Girl Friend): Dynamic, optimistic, intermediate
  - Profesor (Professor): Formal, academic, advanced
- **Language support**: Teaching English, French, Italian through Polish interface
- **Image dependencies**: App expects 6 PNG files in Images/ directory

## Common Tasks

### Starting Development
- `cd /path/to/chatbot_ai`
- `pip install -r requirements.txt`
- `streamlit run streamlit_app.py`
- Open http://localhost:8501 in browser

### Modifying Tutor Personalities
- Edit personality descriptions in `ai_config.py`
- Modify SYSTEM_PROMPT in `streamlit_app.py` around line 120-140
- Always test with actual API key to verify conversation behavior

### Adding New Languages
- Update language dropdown options in `streamlit_app.py` line ~13
- Modify SYSTEM_PROMPT to include new language instruction
- Test with all tutor personalities

### Debugging Connection Issues
- Verify port 8501 is available: `netstat -an | grep 8501`
- Check firewall settings for local development
- Use `--server.port` flag to specify different port if needed

## File Reference (Output from `ls -la`)
```
total 40
drwxr-xr-x 5 runner runner 4096 Sep 20 10:05 .
drwxr-xr-x 3 runner runner 4096 Sep 20 10:04 ..
drwxrwxr-x 2 runner runner 4096 Sep 20 10:05 .devcontainer
drwxrwxr-x 7 runner runner 4096 Sep 20 10:05 .git
drwxrwxr-x 2 runner runner 4096 Sep 20 10:05 Images
-rw-rw-r-- 1 runner runner  593 Sep 20 10:05 README.md
-rw-rw-r-- 1 runner runner    0 Sep 20 10:05 __init__.py
-rw-rw-r-- 1 runner runner  961 Sep 20 10:05 ai_config.py
-rw-rw-r-- 1 runner runner   32 Sep 20 10:05 requirements.txt
-rw-rw-r-- 1 runner runner 7813 Sep 20 10:05 streamlit_app.py
```

### Images Directory Contents
```
total 6796
-rw-rw-r-- 1 runner runner 1096041 Sep 20 10:05 Alicja.png
-rw-rw-r-- 1 runner runner 1158988 Sep 20 10:05 Dagmara.png
-rw-rw-r-- 1 runner runner  875198 Sep 20 10:05 Norbert.png
-rw-rw-r-- 1 runner runner  639312 Sep 20 10:05 friend.png
-rw-rw-r-- 1 runner runner 1492926 Sep 20 10:05 przyjaciolka.png
-rw-rw-r-- 1 runner runner 1679011 Sep 20 10:05 teacher.png
```

## Important Notes

### API Key Security
- Application expects OpenAI API key as user input (not environment variable)
- API key field is password-type (hidden input)
- No default API key -- users must provide their own
- **Cost warning**: Application displays billing warnings about OpenAI usage costs

### Language and Localization
- **Interface language**: Polish (all UI text, labels, buttons)
- **Teaching languages**: English, French, Italian
- **Target audience**: Polish speakers learning foreign languages

### No CI/CD or Linting
- **No automated linting** -- manually review code style
- **No automated testing** -- always perform manual validation
- **No build pipeline** -- direct deployment of Python source code
- **No dependency vulnerability scanning** -- manually update requirements.txt when needed

### Limitations
- **No offline mode** -- requires internet for OpenAI API calls
- **No chat history persistence** -- chat resets on page refresh
- **No user authentication** -- single-session application
- **No database** -- all state in Streamlit session