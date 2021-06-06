# genderAgeEmotionRace
# genderAgeEmotionRace with DeepFace
## Model is pretrained with different images
### Introduction

DeepFace is a Facebook research group's deep learning facial recognition technology. In digital photos, it recognises human faces. A nine-layer neural network is used in the application. Rather of using traditional convolutional layers, this deep network uses many locally linked layers without weight sharing, resulting in almost 120 million parameters. As a result, we trained it on the world's largest facial dataset to date, a four-million-image identity-labeled dataset with over 4,000 identities.


### Requirements for model and flask deployment
* numpy~=1.19.2
* Flask==2.0.0
* Pillow==8.2.0
* tensorflow-cpu==2.5.0rc1
* Werkzeug==2.0.0
* gunicorn==20.0.4


### Installation
* pip install deepface
* pip install pandas
* pip install matplotlib


## Features

- DeepFace is the facial recognition system used by Facebook for tagging images.
- We can also use deepface for real-time video.
- This approach focuses on alignment and representation of facial images. 
- Humans can achieve a score of 97.53 percent on facial recognition tasks, whereas this ensemble method achieves a score of 98.57 percent accuracy.
- The DeepFace interface's stream function will access your webcam and do face recognition and facial attribute analysis. 
- A database folder containing face photos is expected by the Stream function.
- In modern face recognition there are 4 steps:

* Detect
* Align
* Represent
* Classify


### Troubleshooting

Pre-trained weights of custom models will be downloaded from Google Drive source to your environment once. Download limit of my Google Drive account might be exceeded sometimes. In this case, you might have an exception like "Too many users have viewed or downloaded this file recently. Please try accessing the file again later". You can still download the pre-trained weights from Google Drive manually.
