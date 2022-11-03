# Locust Load Testing Tool

## 1. Installing
`pip install -Ur requirements.txt` or `pip install locust`

## 2. Configuration
Edit the locust.conf file. More options can be found [here](https://docs.locust.io/en/stable/configuration.html).

## 3. Credentials
Populate the passwords for Dev and UAT, from 1Password, for local use only.
Take care never to commit credentials!

## 4. Test Data
Obtain a list of valid fund IDs for the relevant environment and add them to the `FUND_IDS` list, within the testdata.py file.

## 5. Execution
Once all the above is correct and complete, run `locust` from the command line.
Results can be viewed live from http://localhost:8089/ and report downloaded on completion.
More options can be added to locust.conf or via command line, as per the configuration document above.