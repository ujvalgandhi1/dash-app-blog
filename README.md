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

**Step 4a.** Run the packages you need via the pip install command. Note that the pandas/numpy in case you need them are somehow not supported if you just do pip install pandas and pip install numpy. As of this writing (June 2022), I had to do pip install pandas==1.3.5 and pip install numpy==1.21.6 to make the applicatation work 

**Step 5**. Now make sure you are on the dash-az folder using your Virtual Environment and run $pip freeze > requirements.txt

**Creating the Azure Web App**

Follow instructions via screenshots laid out here

[Azure Web App Creation Screen-Main](https://github.com/ujvalgandhi1/dash-app-blog/tree/main/assets/AzureWebAppCreation_1.PNG?raw=true)

[Azure Web App Creation Screen-ComputeSize](https://github.com/ujvalgandhi1/dash-app-blog/tree/main/assets/AzureWebAppCreation_2.PNG?raw=true)

**Deploying the Web App**
Remain on the cmd and in the dash-az folder, run the following command
az webapp up --location <your region> --name <your Azure Web App> --resource-group <Your Resource Group>
  
Replace the <region> with values of your region eg az web app up --location eastus
Similarly, replace the <your Azure Web App> and <Your Resource Group> with the names of your Azure Web App and your resource group respectively. 

Click Enter and wait for the deployment to go through. It *might* take some time.. Once deployed, you should be able to navigate to the URL (provided on the window OR via the portal) and check your Dash App !
