import fitz  # PyMuPDF
import pyttsx3

def pdf_to_audio(pdf_path, output_audio="output.mp3"):
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        text = ""

        # Extract text from each page
        for page in doc:
            text += page.get_text("text") + "\n"

        if not text.strip():
            print("No text found in the PDF.")
            return

        # Initialize text-to-speech engine
        engine = pyttsx3.init()

        # Adjust voice properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1.0)  # Volume level

        # Speak the text
        engine.save_to_file(text, output_audio)
        engine.runAndWait()
        
        print(f"Audio saved as {output_audio}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
pdf_to_audio("sample.pdf", "output.mp3")
