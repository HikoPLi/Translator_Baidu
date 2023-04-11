# Translator_Baidu
This program is used as a translator.  
API is from Baidu Translator.  

# How to request an API and ID
Firstly, you need to register an account with an app id and secret code.  
  
The entrance URL is :

    https://fanyi-api.baidu.com/

And you can get:

    APP ID： *****************
    密钥：   ******************

# How to use it
This program can only run on Mac because of the path.   
 But I'll write one for the Windows version.  


 To download this program, you can get access to github.com.
 You may type this command to clone the repo from GitHub:  

        git clone https://github.com/HikoPLi/Translator_Baidu

Or you may get access to the repo:  

        https://github.com/HikoPLi/Translator_Baidu

And download the .zip file.  
(Also you want to do some stupid. You can open all the files to copy and paste. LOL)  

If you want to run this program successfully, you need to install the Python library.  
For MacOS users, you may run the following command in your terminal:  

        pip install python

After you install this library, you can use your terminal to get into the folder and type the following command to run this program:   

        python main.py

If you get the app id and secret code successfully, you can open the loginCD.json to put in them.

    [
        {
        "appid": "*****************",
        "secretKey": "******************"
        }
    ]
But an original one wihch was registered by me has been put in.

    [
        {
        "appid": "20230410001636585",
        "secretKey": "L_RILBnzNGqKjDsfvG5C"
        }
    ]  