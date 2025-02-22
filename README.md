# Tax Genie

## Authors - David Falekulo, Rakshith Puligundla, Fawaz Abdulwahab, Oluwatobiloba Lawuyi   

## Table of Contents

- [Project Fundamentals](#fundamentals)
- [Project Scope](#project_scope)
- [Core Functionality](#core_functionality)
- [Backend](#backend)
- [Frontend](#frontend)
- [API Integrations](#api_integrations)
- [Setup Instructions](#setup)
- [Future Enhancements](#future_enhancements)
- [License](#license)
- [Contact](#contact)

---

## Project Fundamentals <a name = "fundamentals"></a>

- **Problem Statement**: Tax filing can be confusing, especially for individuals with little to no experience in financial documentation. Tax Genie aims to simplify the tax filing process by providing AI-driven assistance tailored to user needs.
- **Target Audience**:
  - Low-income families seeking straightforward tax filing guidance.
  - Gen Z users with minimal experience in tax preparation.
  - Elderly individuals looking for a simplified approach to filing taxes.
- **Type of Project**: AI-driven tax filing assistant.

---

## Project Scope <a name = "project_scope"></a>

- **Main Functionality**
  - **Step-by-step Tax Filing Guidance**: Tax Genie provides clear instructions on filling out tax forms, understanding deductions, and checking eligibility.
  - **Voice Assistance**: Users can interact with Johny, the AI assistant, using voice commands.
  - **Privacy-Focused**: No personal data is stored, ensuring security.
- **Methodology**:
  - **Programming Languages**: Python for backend logic, JavaScript for frontend interaction.
  - **Tools & APIs**: OpenAI for text generation, Eleven Labs for text-to-speech, and Whisper for speech recognition.

---

## Core Functionality <a name = "core_functionality"></a>

### **Step-by-Step Guidance**
1. The user interacts with **Johny the Genie**, the AI assistant, via voice or text.
2. Genie provides explanations, breakdowns, and clarifications in simple terms.
3. The assistant ensures smooth navigation through tax forms and deductions.

### **Objection Handling**
- **Language & Comprehension**: Simplifies complex tax jargon and provides alternative explanations.
- **Trust & Privacy**: No personal data is stored, ensuring security.
- **Complexity**: Breaks down tax processes into manageable steps.
- **Time Constraints**: Allows users to pause and resume guidance as needed.

---

## Backend <a name = "backend"></a>

### **Backend Components**
- **app.py**: Handles API calls to OpenAI for text-to-speech conversion.
- **eleven.py**: Uses Eleven Labs API for high-quality speech synthesis.
- **final.py**: Captures user speech, converts it to text using Whisper, processes it through OpenAI, and generates a voice response using Eleven Labs.

### **System Workflow**
1. User speaks into the system.
2. The speech is converted into text via Whisper.
3. The text is sent to OpenAI for response generation.
4. The response is converted into speech using Eleven Labs.
5. The final voice output is saved as an MP3 file for playback.

---

## Frontend <a name = "frontend"></a>

### **Frontend Components**
- **index.html**: Webpage for interacting with tax documents via an AI assistant.
  - Features a sidebar for navigation and a main area for document upload and voice commands.
  - Uses a dark theme with black and gold colors.
  - Integrates PDF.js for document handling.
  - Utilizes OpenAI and ElevenLabs APIs for AI responses and text-to-speech functionality.

- **app.js**: JavaScript script managing file input events for PDFs and images.
  - Extracts text using PDF.js and Tesseract OCR libraries.
  - Converts text to speech using the ElevenLabs API.
  - Converts speech to text using the Web Speech API.
  - Handles different file types appropriately, providing interactive features for text processing and audio output in the web application.

---

## API Integrations <a name = "api_integrations"></a>

- **OpenAI API**: Used for natural language processing and response generation.
- **Eleven Labs API**: Converts generated text responses into high-quality speech.
- **Whisper API**: Transcribes user speech into text for processing.
- **PDF.js**: Enables rendering and interaction with PDF documents.
- **Tesseract OCR**: Extracts text from image-based files.
- **Web Speech API**: Enables speech-to-text conversion for user input.

---

## Setup Instructions <a name = "setup"></a>

### **Prerequisites**
- Python 3.8+
- Node.js for frontend dependencies (if needed)
- API keys for OpenAI and Eleven Labs

### **Installation Steps**
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/tax-genie.git
   cd tax-genie
   ```
2. Install backend dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Install frontend dependencies (if applicable):
   ```sh
   npm install
   ```
4. Set up API keys in a `.env` file:
   ```sh
   OPENAI_API_KEY=your_openai_key
   ELEVENLABS_API_KEY=your_elevenlabs_key
   ```
5. Run the backend:
   ```sh
   python final.py
   ```
6. Start the frontend (if applicable):
   ```sh
   npm start
   ```

---

## Future Enhancements <a name = "future_enhancements"></a>

- **Multilingual Support**: Expand to include multiple languages for broader accessibility.
- **Tax Form Auto-Fill**: Automate form completion based on user responses.
- **Mobile App Integration**: Develop a companion app for mobile users.

---

## License <a name = "license"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact <a name = "contact"></a>

For any questions or suggestions, please contact:

David Falekulo, davidthetech24@gmail.com
Rakshith Puligundla Venugopal, rakshithpuligundla@gmail.com
Fawaz Abdulwahad, fawazabdulwahab@gmail.com
Oluwatobiloba Lawuyi, lawuyioluwatobiloba@gmail.com
