#include "psi_server_aided.h"

int server(int flag){
	clock_t time;
	size_t data_received = 0, data_sent = 0;
	
	int server_fd, valread, valread2, i=0;
	int new_socket[2];
	struct sockaddr_in address;
	int opt = 1;
	int addrlen = sizeof(address);
	char len[2][MAXCHAR], buffer[2][MAXCHAR];
	std::vector<std::string> data1, data2, data;

	// Creating socket file descriptor
	if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		perror("socket failed");
		exit(EXIT_FAILURE);
	}

	// Forcefully attaching socket to the port 8080
	if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
		perror("setsockopt");
		exit(EXIT_FAILURE);
	}
	address.sin_family = AF_INET;
	address.sin_addr.s_addr = INADDR_ANY;
	address.sin_port = htons(PORT);

	// Forcefully attaching socket to the port 8080
	if (bind(server_fd, (struct sockaddr*)&address,sizeof(address)) < 0) {
		perror("bind failed");
		exit(EXIT_FAILURE);
	}
	
	if (listen(server_fd, 3) < 0) {
		perror("listen");
		exit(EXIT_FAILURE);
	}
	
	if ((new_socket[0] = accept(server_fd, (struct sockaddr*)&address,(socklen_t*)&addrlen)) < 0) {
		perror("accept");
		exit(EXIT_FAILURE);
	}
	
	if ((new_socket[1] = accept(server_fd, (struct sockaddr*)&address,(socklen_t*)&addrlen)) < 0) {
		perror("accept");
		exit(EXIT_FAILURE);
	}
	
	time = clock();                       // to measure time
	
	data_received += recv(new_socket[0], len[0], MAXCHAR, 0);
	for(int i=0; i< std::stoi(len[0]); i++){
		data_received += recv(new_socket[0], buffer[0], MAXCHAR, 0);
		data_sent += send(new_socket[0], "ack", strlen("ack"), 0);
		data1.emplace_back(buffer[0]);
	}
	
	data_received += recv(new_socket[1], len[1], MAXCHAR, 0);
	for(int i=0; i< std::stoi(len[1]); i++){
		data_received += recv(new_socket[1], buffer[1], MAXCHAR, 0);
		data_sent += send(new_socket[1], "ack", strlen("ack"), 0);
		data2.emplace_back(buffer[1]);
	}

	data = interset(data1, data2);
	
	for(int i=0; i<data.size(); i++){
		data_sent += send(new_socket[0], data[i].c_str(), MAXCHAR,0);
		data_received += recv(new_socket[0], buffer[0], MAXCHAR, 0);
		
		data_sent += send(new_socket[1], data[i].c_str(), MAXCHAR,0);
		data_received += recv(new_socket[1], buffer[1], MAXCHAR, 0);
	}
	
	send(new_socket[0], "ack", MAXCHAR,0);	
	send(new_socket[1], "ack", MAXCHAR,0);
	
	if(flag==1){
		std::cout << "\nRequired time: " << (double)(clock() - time)/CLOCKS_PER_SEC << " s\n"; 
		std::cout << "Data exchanged: " << data_sent+data_received << " B\n";
	}

	// closing the connected socket
	close(new_socket[0]);
	close(new_socket[1]);
	// closing the listening socket
	shutdown(server_fd, SHUT_RDWR);
	
	return 0;
}
