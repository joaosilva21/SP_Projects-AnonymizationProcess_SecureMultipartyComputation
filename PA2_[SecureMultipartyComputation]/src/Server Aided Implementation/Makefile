CC=g++
FLAGS=-std=c++11 -Wall
PROG=psi_server_aided
OBJS=server.o client.o psi_server_aided.o utils.o sha256.o

all: ${PROG}

clean:
		rm ${OBJS} *~ {PROG}
		
${PROG}: ${OBJS}
		${CC} ${FLAGS} ${OBJS} -lm -o $@
			
.c.o:
		${CC} ${FLAGS} $< -c -o $@
		
##########################################
psi_server_aided.o: psi_server_aided.cpp psi_server_aided.h sha256.h
server.o: server.cpp psi_server_aided.h sha256.h
client.o: client.cpp psi_server_aided.h sha256.h
utils.o: utils.cpp psi_server_aided.h sha256.h
sha256.o: sha256.cpp psi_server_aided.h sha256.h
