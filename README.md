## Simple Chatbot Project

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create a `.env` File**
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=<your-google-api-key>
     ```

3. **Run the Backend Server**
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Start the backend server:
     ```bash
     python main.py
     ```
   The server will run at `http://localhost:8000`.

4. **Open the Chatbot Interface**
   - Open `index.html` in your web browser.
   - Interact with the chatbot by typing messages.

### Project Structure

- **`index.html`**: Chat interface.
- **`script.js`**: Handles user interactions and API requests.
- **`styles.css`**: Styles the chat interface.
- **`main.py`**: Backend API implementation using FastAPI.
- **`.env`**: Stores configuration variables (e.g., API keys).

### Notes

- Keep your Google API key secure and do not expose it publicly.
- Customize chatbot behavior by editing `main.py` and `script.js`.
- For production, secure the backend and consider user authentication.
