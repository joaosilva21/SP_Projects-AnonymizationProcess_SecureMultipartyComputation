#include "psi_server_aided.h"

int main(int argc, char const* argv[]){
	if(argc < 3){
		error(argv[0], 0);
		return 1;
	}
	else{
		if(argc == 3 && !strcmp(argv[1],"-r") && !strcmp(argv[2],"0")){
			server(0);
		}
		else if(argc == 4 && !strcmp(argv[1],"-r") && !strcmp(argv[2],"0") && !strcmp(argv[3], "-t")){
			server(1);
		}
		else if(argc == 7 && !strcmp(argv[1],"-r") && !strcmp(argv[2],"1") && !strcmp(argv[3],"-ip") && !strcmp(argv[5],"-f")){
			client(argv[4], argv[6]);
		}
		else{
			error(argv[0], 1);
		}
	}
}
