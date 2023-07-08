#include <arpa/inet.h>
#include <iostream>
#include <fstream>
#include <functional>
#include <netinet/in.h>
#include "sha256.h"
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <vector>

#include <time.h> 

#define PORT 8080
#define MAXCHAR 65

int server(int flag);
int client(char const* ip, char const* filename);
void error(char const* progname, int e);
std::vector<std::string> interset(std::vector<std::string> part1, std::vector<std::string> part2);
std::vector<std::string> reverse(std::vector<std::string> original, std::vector<std::string> part);
