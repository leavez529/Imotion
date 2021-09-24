## Imotion
##### Imotion is a project created during UTokyo Research Hackathon 2021

##### The project involves three different steps -
- Obtaining image description from the input image
- Predicting the emotion conveyed by the image description
- Displaying simulation of swarm of robots based on the predicted emotion

##### How to run the code -
- Clone the code repository
- Download source code of Artemis from https://github.com/optas/artemis  and `pip install -e .`  in the main folder to install dependency (better to perform the installation process in virtual environment.)
- Download the model from  https://drive.google.com/file/d/1MvEBUqFCDflL-Y8TllzYUe_-rivb8bmF/view?usp=sharing. The model should be put in a folder named checkpoints situated inside the server directory.
- Run the command `flask run` in the main directory.
- Open the URL displayed on the terminal in a web browser.
- And you will be able to see the application!
