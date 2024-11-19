#ifndef REPORT_H
#define REPORT_H

#include <wchar.h>

#define REPORT_BYTE 8

int kor2report(char report[REPORT_BYTE], wchar_t c);
void write_kor(int fd, wchar_t c);
void remove_word(int fd);
void remove_letter(int fd);
void write_space(int fd);
#endif
