#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <wchar.h>
#include "report.h"

int main(void)
{
	char *filename;
	int fd = 0;
	filename = "/dev/hidg0";
	if ((fd = open(filename, O_RDWR, 0666)) == -1) {
		perror(filename);
		return 1;
	}
	for (int i = 0; i < 10; i++)
		write_kor(fd, L'ᅫ');
	sleep(1);
	remove_word(fd);
	close(fd);
	return 0;
}
