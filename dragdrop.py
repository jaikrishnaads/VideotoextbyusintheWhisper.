import streamlit as st
import whisper
import os
import tempfile
import zipfile
from io import BytesIO

# Page configuration
st.set_page_config(page_title="Batch AI Transcriber", page_icon="📦")
st.title("📦 Batch Video Transcriber")
st.markdown("Drag and drop **multiple videos** here. The AI will transcribe them all in the background and give you a ZIP file with all the TXT results.")

# 1. Load the Whisper model (cached)
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# 2. Multi-File Uploader
uploaded_files = st.file_uploader("Choose video files", type=["mp4", "mkv", "mov", "avi"], accept_multiple_files=True)

if uploaded_files:
    st.info(f"Loaded {len(uploaded_files)} videos. Ready to process.")
    
    if st.button("Start Batch Transcription"):
        all_transcripts = {} # To store filename: text
        progress_bar = st.progress(0)
        
        for i, uploaded_file in enumerate(uploaded_files):
            # Update status for the user
            st.write(f"Transcribing ({i+1}/{len(uploaded_files)}): {uploaded_file.name}")
            
            # Create a temporary file for the video
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
                temp_video.write(uploaded_file.read())
                video_path = temp_video.name

            try:
                # Transcribe (This happens in the background, no need to watch video)
                result = model.transcribe(video_path)
                transcript_text = result["text"].strip()
                
                # Store the result
                txt_filename = f"{os.path.splitext(uploaded_file.name)[0]}.txt"
                all_transcripts[txt_filename] = transcript_text
                
            except Exception as e:
                st.error(f"Error processing {uploaded_file.name}: {e}")
            
            finally:
                if os.path.exists(video_path):
                    os.remove(video_path)
            
            # Update progress
            progress_bar.progress((i + 1) / len(uploaded_files))

        st.success("All videos processed!")

        # 3. Create a ZIP file in memory for download
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zf:
            for filename, text in all_transcripts.items():
                zf.writestr(filename, text)

        # 4. Final Download Button
        st.download_button(
            label="🎁 Download All Transcripts (ZIP)",
            data=zip_buffer.getvalue(),
            file_name="all_transcripts.zip",
            mime="application/zip"
        )