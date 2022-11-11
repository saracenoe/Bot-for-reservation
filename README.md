# Welcome to Fly Me : flights booking chatbot

This project, part of the course regarding Artificial Intelligence engineering, contains the entire data to create, train and publish a bot using LUIS cognitive service and MS Azure.

Goal : use Azure Cognitive Services (LUIS), Azure Web App and Azure Application Insights, to build a flights booking chatbot, integrate it in a web application, and monitor its quality.

## Installation
  ### Prerequisites
  Python 3.8\
  Azure subscription\
  Azure Cognitive Service - LUIS
  
  ### Virtual environment
      
      conda create -n myflymebot python=3.8 -y
      conda activate myflymebot
      
  ### Dependencies    
      pip install -r requirements.txt
      
  
## Usage
  ### Data
  Download and extract the files from [Frames Dataset](https://www.microsoft.com/en-us/research/project/frames-dataset/download/).

  ### Exploratory Data Analysis
  The main notebook presents the results of the EDA
      
  ### Create a LUIS app in the LUIS portal
  Take a look in the official documentation 
      
  ### Train LUIS Model
  The luis notebook formats the data, run the LUIS training and test the model
      
  ### Test and debug with the emulator
   Run the bot locally. To do that:
   
    python app.py
   Copy the link you get into the emulator, adding "/api/messages" and the end of the URL and open the bot. 
      
 ## Author
 
 **Ezequiel Saraceno**
 
 ## Show your support

Give a ⭐️ if this project helped you!
 
      
  
