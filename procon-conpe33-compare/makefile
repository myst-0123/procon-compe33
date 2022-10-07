CC = g++

CFLAGS = -O3 -mtune=native -march=native -mfpmath=both

TARGET = a.out

SRCS = main.cpp compare.cpp readfile.cpp

OBJS = $(SRCS:.cpp=.o)

$(TARGET): $(OBJS)
	$(CC) -o $@ $^

$(OBJS): $(SRCS)
	$(CC) $(CFLAGS) -c $(SRCS)