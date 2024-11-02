CC = gcc
CFLAGS = $(shell python3-config --cflags --embed) $(includes)
LDFLAGS = $(shell python3-config --ldflags --embed) -lwiringPi

name = main
src_dir = srcs
includes = -I includes
srcs = $(wildcard $(src_dir)/*.c)
python_srcs = $(wildcard $(src_dir)/*.py)
objs = $(srcs:.c=.o)

all: $(name)

$(name): $(objs)
	$(CC) $? -o $@ $(LDFLAGS)

clean:
	rm -f $(objs)

fclean: clean
	rm -f $(name)

re: fclean all

.PHONY: all clean fclean re
