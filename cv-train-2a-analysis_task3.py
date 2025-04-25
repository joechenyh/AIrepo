import pandas as pd
import jiwer
import numpy as np  # for NaN handling

# Load the updated CSV file with transcriptions
output_csv_file = r'C:\Users\cheny\CodeRepo\AIrepo\cv-valid-dev-with-transcriptions.csv'
df = pd.read_csv(output_csv_file)

# Initialize a list to store WER values
wer_values = []
print("Starting WER calculation...")

# Iterate over each row to calculate WER
for index, row in df.iterrows():
    # Get the ground truth transcription and the generated transcription
    ground_truth = row['text']
    generated_text = row['generated_text']
    
    # Skip row if either 'text' or 'generated_text' is NaN
    if pd.isna(ground_truth) or pd.isna(generated_text):
        wer_values.append(np.nan)  # Append NaN for skipped rows
        continue  # Skip the current row if any text is NaN
    
    # Calculate the WER using jiwer
    wer = jiwer.wer(ground_truth, generated_text)
    
    # Append the WER to the list
    wer_values.append(wer)

# Add the WER values as a new column to the DataFrame
df['wer'] = wer_values

# Calculate min, max, and average WER
# Remove NaN values before calculating min, max, and average
wer_values_clean = [wer for wer in wer_values if not pd.isna(wer)]

min_wer = min(wer_values_clean)
max_wer = max(wer_values_clean)
average_wer = sum(wer_values_clean) / len(wer_values_clean)

# Print the results
print(f"Minimum WER: {min_wer}")
print(f"Maximum WER: {max_wer}")
print(f"Average WER: {average_wer}")

# Save the updated DataFrame with WER values to a new CSV file
output_wer_csv = r'C:\Users\cheny\CodeRepo\AIrepo\cv-valid-dev-with-wer.csv'
df.to_csv(output_wer_csv, index=False)
