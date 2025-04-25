#pip install fastapi uvicorn transformers pydub torch numpy python-multipart requests

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from pydub import AudioSegment
import torch
import numpy as np
import io
import traceback

# FastAPI instance
app = FastAPI()

# Load model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.post("/asr")
async def asr(file: UploadFile = File(...)):
    try:
        file_content = await file.read()
        print(f"Received file: {file.filename}, Size: {len(file_content)} bytes")

        # Load and convert MP3 to mono 16kHz WAV using pydub
        audio = AudioSegment.from_file(io.BytesIO(file_content), format="mp3")
        audio = audio.set_channels(1).set_frame_rate(16000)

        # Convert audio to numpy array
        samples = np.array(audio.get_array_of_samples()).astype(np.float32) / 32768.0
        waveform = torch.tensor(samples).unsqueeze(0)  # [1, N]
        sample_rate = 16000
        duration_sec = len(samples) / sample_rate

        # Tokenize and transcribe
        input_values = tokenizer(waveform.squeeze(), return_tensors="pt").input_values
        with torch.no_grad():
            logits = model(input_values).logits

        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = tokenizer.batch_decode(predicted_ids)[0].strip()

        return JSONResponse(content={
            "transcription": transcription,
            "duration": f"{duration_sec:.1f} seconds"
        })

    except Exception as e:
        error_message = traceback.format_exc()
        print(f"Error occurred:\n{error_message}")
        return JSONResponse(status_code=500, content={"error": error_message})




    #Comments:
    #Key in Visual Studio Code terminal: uvicorn asr_api:app --host 0.0.0.0 --port 8001
    #Key in new terminal window & "C:\Windows\System32\curl.exe" -F 'file=@C:\Users\cheny\CodeRepo\AIrepo\mary.mp3' http://localhost:8001/asr
 

