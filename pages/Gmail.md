# Getting Gmail to work with Python

## Environment set up
`conda create --name jarvis python=3.7`

`conda activate jarvis`

`conda install pandas`

`conda install -n jarvis nb_conda_kernels`

## Set up Google Gmail API

[Codes that Google has already written](https://developers.google.com/gmail/api/quickstart/python)
1. Enable Google API
2. Get OAuth 2.0 Credentials: Choose desktop, choose the right gmail scopes, download credential json
3. Prompt to enter your gmail. Ensure that you put your email in the test list of users. 
