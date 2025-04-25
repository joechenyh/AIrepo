These codes were run locally on a predator helios 300 laptop with Nvidia GPU and developed in Visual Studio and Jupyter Notebook. Both were running on Python 3.11 

For requirements.txt, these only apply to the codes that are not in the Jupyter Notebook. 
For the codes on Jupyter Notebook, by running "nvidia-smi" in command prompt, find out the CU version and install the compatible torch, torchvision and torchaudio versions accordingly, if you encounter difficulties running the code on your version of Jupyter notebook. For reference, the pip install ran were: 
#!pip install numpy<2.0
#!pip install torch==2.1.0+cu121 torchvision==0.16.0+cu121 torchaudio --index-url https://download.pytorch.org/whl/cu121

Replace folder/file paths for location of CSV files and sample audio files accordingly. 

Due to time constraints, the cv-train-2a training jupyter notebook was not able to complete its processing/training but the rest of the codes were submitted and expected to run with no issues. This would be updated in this repo once the code has finished processing/training. 

For task 5b, the threshold can be further increased to make the difference between 'True' and 'False' for similarity. 
The current threshold is 0.6 
