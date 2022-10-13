CC = g++

CFLAGS = -O2 -Wall -I. -I./nlohmann

TARGET = a.out

SRCS = main.cpp compare.cpp compare2.cpp readfile.cpp eval.cpp output.cpp

OBJS = $(SRCS:.cpp=.o)

$(TARGET): $(OBJS)
	$(CC) -o $@ $^

$(OBJS): $(SRCS)
	$(CC) $(CFLAGS) -c $(SRCS)