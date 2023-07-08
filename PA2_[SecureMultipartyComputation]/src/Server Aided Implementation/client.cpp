#include "psi_server_aided.h"

int client(char const* ip, char const* filename){
	int status, valread, client_fd;
	struct sockaddr_in serv_addr;
	std::vector<std::string> data, hash; 
	std::string music;
	std::ifstream file;
	char len[MAXCHAR], buffer[MAXCHAR];
	
	file.open(filename, std::ios::in);
  	if (file){
    	while(getline(file, music)){
    		data.emplace_back(music);
    	}
    	file.close();
  	}
  	else{
  		std::cout << "File doesn't exist\n";
  	}
  	
	
	if ((client_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		printf("\n Socket creation error \n");
		return 1;
	}

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(PORT);

	// Convert IPv4 and IPv6 addresses from text to binary
	// form
	if (inet_pton(AF_INET, ip, &serv_addr.sin_addr) <= 0) {
		printf("\nInvalid address/ Address not supported \n");
		return 1;
	}

	if ((status = connect(client_fd, (struct sockaddr*)&serv_addr, sizeof(serv_addr))) < 0) {
		printf("\nConnection Failed \n");
		return 1;
	}
	
	send(client_fd, std::to_string(data.size()).c_str(), MAXCHAR,0);
	for(int i=0; i< data.size(); i++){
		send(client_fd, sha256(data[i]).c_str(), MAXCHAR,0);
		recv(client_fd, buffer, MAXCHAR, 0);
	}

	while(1){
		recv(client_fd, buffer, MAXCHAR, 0);
		if(strcmp(buffer,"ack")==0){
			break;
		}
		
		send(client_fd, "ack", strlen("ack"), 0);
		hash.emplace_back(buffer);
	}
	
	hash = reverse(data, hash);
	std::cout << "Found " << hash.size() << " intersections\n";
	for(int i=0; i<hash.size(); i++){
		std::cout << hash[i] << "\n";
	}
	
	// closing the connected socket
	close(client_fd);
	return 0;
}

//sendto(client_fd, data.c_str(), MAXCHAR,0,(struct sockaddr *) &serv_addr, sizeof(serv_addr));
//recvfrom(client_fd, buffer, MAXCHAR,0,(struct sockaddr *)&serv_addr, (socklen_t*)&len);
