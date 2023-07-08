# SP_Project-Secure_Multiparty_Computation

- [x] Finished

## Index:
- [Description](#description)
- [To run this project](#to-run-this-project)
- [Notes important to read](#notes-important-to-read)

## Description:
The main objective here is to explore the concepts of Secure Multiparty Computation, especially PSI(Private Set Intersection) protocols. So the work done is basically assess a set of implementations for this type of protocols

## To run this project:
The datasets used to benchmark the different implementations are artificially generated using the code "generate_dataset.py". To run this use the following command:
 ```shellscript
  [your-disk]:[name-path]> python generate_dataset.py [flag]
 ```

Because the server aided implementation is somehow broken, was asked to find a solution to it, so we decide to implement out server aided PSI protocol. To compile it:
 ```shellscript
  [your-disk]:[name-path]> make 
 ```

To run it you will need 3 terminals, 1 for a server and 2 for the two clients:
[Server]
 ```shellscript
  [your-disk]:[name-path]> ./psi_server_aided -r 0 
 ```

[Client]
 ```shellscript
  [your-disk]:[name-path]> ./psi_server_aided -r 1 -ip [server_ip_address] -f [dataset_to_be_used]
 ```

## Notes important to read
- To understand what are and how the commands work see the statement and the report files
- To run python code "addnames.py" see the report or read code before, because there are some flags to be used.
- To run python code "logistic_regression.py" it's recommend to use a Linux system.
- NEVER use our implementation in any real scenario, because is super inefficient xD
- The dataset "songs_normalize.csv" is from: https://www.kaggle.com/code/keremkarayaz/spotify-song-list/input
