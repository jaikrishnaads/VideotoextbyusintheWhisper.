# 📦 Batch Video Transcriber (Offline AI)

A simple **offline batch video transcription tool** built with **Streamlit** and **OpenAI Whisper**.
Upload multiple video files, let the AI transcribe them **locally**, and download all transcripts as a single ZIP file.

No cloud APIs.
No internet dependency *after model download*.
No nonsense.

---

## ✨ Features

* 🎥 Upload **multiple videos at once**
* 🧠 Uses **Whisper (base model)** for speech-to-text
* 📴 Runs **fully offline** after setup
* 📄 Generates **separate `.txt` transcript** for each video
* 📦 Downloads all transcripts as a **ZIP file**
* 📊 Progress bar for batch processing
* 🧼 Automatic cleanup of temporary files

---

## 🧠 How It Works (Concept)

1. User uploads multiple video files
2. Each video is temporarily stored
3. Audio is extracted internally by Whisper
4. Speech is transcribed into text
5. Each transcript is saved as a `.txt`
6. All text files are packed into a ZIP for download

Everything runs **locally on your machine**.

---

## 🛠 Tech Stack

* **Python**
* **Streamlit** – UI
* **OpenAI Whisper** – Offline speech recognition
* **FFmpeg** – Audio extraction (required by Whisper)

---

## 📦 Supported Video Formats

* `.mp4`
* `.mkv`
* `.mov`
* `.avi`

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jaikrishnaads/VideotoextbyusintheWhisper..git
cd batch-video-transcriber
```

### 2️⃣ Create a Virtual Environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install streamlit openai-whisper
```

### 4️⃣ Install FFmpeg (Required)

Whisper **will not work without FFmpeg**.

* **Windows**:
  Download from [https://ffmpeg.org](https://ffmpeg.org)
  Add `ffmpeg/bin` to PATH

* **Linux**:

```bash
sudo apt install ffmpeg
```

* **macOS**:

```bash
brew install ffmpeg
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open the shown local URL in your browser.

---

## 📁 Project Structure

```
.
├── app.py              # Main Streamlit app
├── README.md           # Documentation
└── requirements.txt    # (optional)
```

---

## ⚠️ Notes & Limitations

* First run will download the Whisper model (~140MB)
* Processing speed depends on:

  * CPU power
  * Video length
  * Audio clarity
* Long videos may take time (this is offline AI, not cloud magic)

---

## 🔒 Privacy

* All processing is done **locally**
* No data is uploaded anywhere
* Videos and audio are deleted after transcription

Your data stays yours.

---

## 🌱 Future Improvements

* Language selection
* Speaker diarization
* Export to PDF / SRT
* Desktop app version
* Android APK wrapper

---

## 📜 License

This project is open-source and free to use for learning and personal projects.
Check Whisper’s license for commercial usage.

---

## 🧪 Built For

Vibe coders.
Offline enjoyers.
People who hate API keys.

---

If you want, next we can:

* Convert this into a **desktop EXE**
* Wrap it into an **Android APK**
* Add a **local transcript library**
* Or rewrite this in **pure offline mobile logic**

This README already smells like a real project.
