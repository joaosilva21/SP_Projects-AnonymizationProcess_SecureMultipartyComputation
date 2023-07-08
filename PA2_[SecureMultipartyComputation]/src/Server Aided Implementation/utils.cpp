#include "psi_server_aided.h"

void error(char const* progname, int e){
	if(e == 0){
		std::cout << "Missing arguments. Usage:\n"; 
	}
	else{
		std::cout << "Wrong arguments. Usage:\n";
	}
	
	std::cout << "\t" << progname << " -r <0|1> -ip <ipaddress> -f <filename> [FOR CLIENTS]\n";
	std::cout << "\t" << progname << " -r <0|1> [FOR SERVER]\n\n";
}

std::vector<std::string> interset(std::vector<std::string> part1, std::vector<std::string> part2){
	std::vector<std::string> intset;
	
	for(std::string p1 : part1){
		for(std::string p2 : part2){
			if(!strcmp(p1.c_str(), p2.c_str())){
				intset.emplace_back(p1);
				break;
			}
		}
	}

	return intset;
}

std::vector<std::string> reverse(std::vector<std::string> original, std::vector<std::string> part){
	std::vector<std::string> rev;
	
	for(std::string p : part){
		for(std::string o : original){
			if(!strcmp(sha256(o.c_str()).c_str(), p.c_str())){
				rev.emplace_back(o);
				break;
			}
		}
	}

	return rev;
}
