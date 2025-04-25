#pip install pandas object-detection

import pandas as pd
import requests
import os

csv_file = 'C:\\Users\\cheny\\CodeRepo\\AIrepo\\cv-valid-dev.csv'
audio_folder = 'C:\\Users\\cheny\\Downloads\\common_voice\\cv-valid-dev'  # Double backslashes


# FastAPI server URL for transcription
api_url = 'http://localhost:8001/asr'

# Load the CSV file containing the metadata
df = pd.read_csv(csv_file)

# Create a list to store the transcribed texts
generated_texts = []

# Iterate over each row in the CSV file
for index, row in df.iterrows():
    # Get the filename (relative path of the audio file)
    audio_file = os.path.join(audio_folder, row['filename'])
    
    # Check if the file exists
    if not os.path.exists(audio_file):
        print(f"Audio file not found: {audio_file}")
        generated_texts.append('Audio file not found')
        continue

    try:
        # Open the MP3 file and send it as part of the request to the API
        with open(audio_file, 'rb') as f:
            files = {'file': (row['filename'], f, 'audio/mp3')}
            
            # Send POST request to the FastAPI /asr endpoint
            response = requests.post(api_url, files=files)
            
            # Check if the response status is OK (200)
            if response.status_code == 200:
                transcription = response.json().get('transcription', '')
                print(f"Transcription for {row['filename']}: {transcription}")
                generated_texts.append(transcription)
            else:
                print(f"Error processing file {row['filename']}: {response.status_code}")
                generated_texts.append('Error transcribing')
    except Exception as e:
        print(f"An error occurred with file {row['filename']}: {e}")
        generated_texts.append('Error transcribing')

# Add the transcriptions as a new column in the DataFrame
df['generated_text'] = generated_texts

# Save the updated DataFrame with the transcriptions back to a new CSV file
output_csv_file = r'C:\Users\cheny\CodeRepo\AIrepo\cv-valid-dev-with-transcriptions.csv'
df.to_csv(output_csv_file, index=False)

print(f"Transcriptions saved to: {output_csv_file}")


#Commments: 
#run python cv-decode.py

