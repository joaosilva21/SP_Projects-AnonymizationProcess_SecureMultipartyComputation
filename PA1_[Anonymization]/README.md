# SP_Project-Anonymization_of_datasets

- [x] Finished

## Index:
- [Description](#description)
- [To run this project](#to-run-this-project)
- [Notes important to read](#notes-important-to-read)

## Description:
The main objective here is to conduct a detailed anonymization process to a dataset and then do privacy, utility and risk analysis. Before that, it's essential to sanitize the dataset.

## To run this project:
Almost all of the work here is done using ARX programm, that apply some privacy models like K-Anonymity, L-Diversity, T-Closeness and others. To know more about our analysis read the report (that is in portuguese .-.).
To sanitize the original dataset ("cardio_train.csv") we run the following script with the following command:
 ```shellscript
  [your-disk]:[name-path]> python addnames.py
 ```

In the final steps of this project we analyse the utility of the privacy models choosed, for that we implement the prediction model Logistic Regression. To run the script created we run the following command:
 ```shellscript
  [your-disk]:[name-path]> python logistic_regression.py
 ```

## Notes important to read
- To understand what are and how the commands work see the statement and the report files
- To run python code "addnames.py", the file "cardio_train.csv" must be in the same folder
- To run python code "logistic_regression.py", the file "TREINO_MIX.csv" must be in the same folder. This file is the initial dataset anonymized by the ARX.
- The dataset "cardio_train.csv" is from: https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset
