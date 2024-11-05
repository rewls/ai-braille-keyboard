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
	write_kor(fd, L'ᄀ');
	sleep(1);
	remove_word(fd);
	close(fd);
	return 0;
}
