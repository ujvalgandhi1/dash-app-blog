# dash-app-blog
Publishing a dash app to Azure
This repo allows you to publish a Python Dash dashboard to Azure Web App from a Windows Environment and without using Dockers/Github

**Main Reference articles**
https://medium.com/microsoftazure/deploying-dash-to-azure-without-using-docker-7d9c9e942ac4
https://www.codegrepper.com/code-examples/python/python+create+venv+in+current+directory


**Step 1** : Develop a Python dash application locally and test it out on a local browser.. The connectivity with Azure SQL Server via pyodbc is somewhat tricky so I ended up using the output of the SQL processes to a set of csv files hosted on the Azure Storage Account

**Step 2**. Start a Python virtual environment. **Note** : This is critical because there is a step to incorporate a requirements file and without the virtual environment, each and every package you have will be packaged. This can introduce a lot of comptability errors 
              pip install virtualenv # install first
              cd projectfolder # go to project folder
              python -m venv ./venv # Create a virtual environment named venv
              Activate.ps1 # (powershell) start the file  to start the environment
              activate.bat # (cmd) start the file  to start the environment
              # if it worked you'll see a (venv) in front of your cursor path
              
**Step 3**. go to the scripts folder using your cmd and run mkdir dash-az there

**Step 4**. Put your application.py file inside the dash-az folder (One that has been testing locally)

**Step 5**. Now make sure you are on the dash-az folder using your Virtual Environment and run $pip freeze > requirements.txt

**Creating the Azure Web App**

Follow instructions via screenshots laid out here

[Azure Web App Creation Screen](https://github.com/ujvalgandhi1/dash-app-blog/tree/main/assets/AzureWebAppCreation_1.PNG?raw=true)
[Azure Web App Creation Screen](https://github.com/ujvalgandhi1/dash-app-blog/tree/main/assets/AzureWebAppCreation_2.PNG?raw=true)
