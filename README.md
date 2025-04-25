These codes were run locally on a predator helios 300 laptop with Nvidia GPU and developed in Visual Studio and Jupyter Notebook.
Both were running on Python 3.11 

For the codes on Jupyter Notebook, by running "nvidia-smi" in command prompt, find out the CU version and install the compatible torch, torchvision and torchaudio versions accordingly, if you encounter difficulties running the code on your version of Jupyter notebook. 

Replace folder/file paths for location of CSV files and sample audio files accordingly. 

Due to time constraints, the training jupyter notebook was not able to complete its processing/training but the rest of the codes were submitted and expected to run with no issues. 

For requirements.txt, these only apply to the codes that are not in the Jupyter Notebook. 

For task 5b, the threshold can be further increased to make the difference between 'True' and 'False' for similarity. 
The current threshold is 0.6 
