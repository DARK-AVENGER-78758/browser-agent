# Agentic Browser Backend

A powerful AI-powered web automation system that can perform various tasks including desktop automation, web login, form filling, data extraction, and messaging.

## Features

- 🤖 **AI-Powered Task Recognition**: Understands natural language commands
- 🌐 **Web Automation**: Login, form filling, data extraction, navigation
- 💻 **Desktop Automation**: Open applications, create files
- 🔐 **Secure Credential Management**: Store and manage login credentials
- 📸 **Screenshot Capture**: Visual verification of actions
- 🛡️ **Error Handling**: Robust error recovery and logging
- 📊 **Intent Analysis**: Smart detection of user intentions

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Playwright Browsers

```bash
playwright install chromium
```

### 3. Set Up Environment Variables

Create a `.env` file in the backend directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 4. Start the Server

```bash
python main.py
```

The server will start on `http://127.0.0.1:8000`

## API Endpoints

### Chat with AI
```http
POST /chat
Content-Type: application/json

{
  "messages": [
    {"role": "user", "content": "Open Notepad for me"}
  ]
}
```

### Execute Task Directly
```http
POST /tasks/execute
Content-Type: application/json

{
  "task_type": "OPEN_NOTEPAD",
  "parameters": {}
}
```

### Store Credentials
```http
POST /credentials/store
Content-Type: application/json

{
  "service_name": "gmail",
  "credentials": {
    "username": "user@example.com",
    "password": "password123"
  }
}
```

### Get Available Services
```http
GET /credentials/services
```

### Health Check
```http
GET /health
```

## Usage Examples

### Desktop Automation

```python
import requests

# Open Notepad
response = requests.post("http://127.0.0.1:8000/chat", json={
    "messages": [{"role": "user", "content": "Open Notepad"}]
})

# Open Calculator
response = requests.post("http://127.0.0.1:8000/chat", json={
    "messages": [{"role": "user", "content": "Open Calculator"}]
})
```

### Web Automation

#### 1. Store Credentials First
```python
# Store Gmail credentials
requests.post("http://127.0.0.1:8000/credentials/store", json={
    "service_name": "gmail",
    "credentials": {
        "username": "your_email@gmail.com",
        "password": "your_password"
    }
})
```

#### 2. Login to Website
```python
# Login to Gmail
response = requests.post("http://127.0.0.1:8000/chat", json={
    "messages": [{"role": "user", "content": "Log into Gmail"}]
})
```

#### 3. Fill Forms
```python
# Fill out a contact form
response = requests.post("http://127.0.0.1:8000/tasks/execute", json={
    "task_type": "WEB_FILL_FORM",
    "parameters": {
        "form_data": {
            "name": "John Doe",
            "email": "john@example.com",
            "message": "Hello, this is a test message"
        },
        "selectors": {
            "name": "input[name='name']",
            "email": "input[name='email']",
            "message": "textarea[name='message']"
        }
    }
})
```

#### 4. Extract Data
```python
# Extract data from a website
response = requests.post("http://127.0.0.1:8000/tasks/execute", json={
    "task_type": "WEB_EXTRACT_DATA",
    "parameters": {
        "url": "https://example.com",
        "extraction_rules": {
            "title": "h1",
            "description": ".description",
            "price": ".price"
        }
    }
})
```

#### 5. Send Messages
```python
# Send a message
response = requests.post("http://127.0.0.1:8000/tasks/execute", json={
    "task_type": "WEB_SEND_MESSAGE",
    "parameters": {
        "message": "Hello, this is an automated message",
        "message_selector": "textarea[placeholder='Type your message']"
    }
})
```

## Supported Task Types

### Desktop Tasks
- `OPEN_NOTEPAD` - Open Windows Notepad
- `OPEN_CALCULATOR` - Open Windows Calculator
- `OPEN_BROWSER` - Open default browser
- `CREATE_FILE` - Create a text file

### Web Tasks
- `WEB_LOGIN` - Login to websites
- `WEB_FILL_FORM` - Fill out web forms
- `WEB_EXTRACT_DATA` - Extract data from web pages
- `WEB_CLICK` - Click elements on web pages
- `WEB_SEND_MESSAGE` - Send messages through web interfaces

## Configuration

### Browser Settings

You can modify browser behavior in `playwright_automation.py`:

```python
class BrowserAutomation:
    def __init__(self, headless: bool = False, slow_mo: int = 100):
        # headless: Run browser in background (True) or visible (False)
        # slow_mo: Delay between actions in milliseconds
```

### Screenshot Directory

Screenshots are saved to the `screenshots/` directory by default. You can change this in the `BrowserAutomation` class.

## Testing

Run the test suite to verify everything works:

```bash
python test_automation.py
```

This will test:
- Health check
- Desktop automation
- Credential management
- AI chat functionality
- Intent analysis

## Troubleshooting

### Common Issues

1. **Playwright not installed**
   ```bash
   playwright install chromium
   ```

2. **OpenRouter API key not set**
   - Make sure you have a `.env` file with `OPENROUTER_API_KEY=your_key`

3. **Browser automation fails**
   - Check if the website is accessible
   - Verify selectors are correct
   - Check screenshots in the `screenshots/` directory

4. **Credentials not found**
   - Store credentials first using `/credentials/store`
   - Check available services with `/credentials/services`

### Debug Mode

Enable debug logging by modifying the logging level in `main.py`:

```python
logging.basicConfig(level=logging.DEBUG)
```

### Screenshots

Screenshots are automatically taken during automation tasks. Check the `screenshots/` directory for visual verification of actions.

## Security Considerations

- Credentials are stored in memory (not persistent)
- In production, use encrypted database storage
- Never log sensitive information
- Implement proper authentication for production use

## Development

### Adding New Task Types

1. Add the task to the `execute_task()` function in `main.py`
2. Implement the automation logic in `playwright_automation.py`
3. Update the intent analysis in `analyze_user_intent()`
4. Add test cases to `test_automation.py`

### Extending Browser Automation

The `BrowserAutomation` class is designed to be extensible. You can add new methods for specific automation needs:

```python
def custom_automation(self, parameters):
    # Your custom automation logic here
    pass
```

## License

This project is part of the Agentic Browser system. See the main project license for details. 