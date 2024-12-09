#ifndef REPORT_H
#define REPORT_H

#include <wchar.h>

int hid_init(void);
void write_kor(int fd, wchar_t c);
int write_jamo(int fd, wchar_t c);
int write_word(int fd, wchar_t *s);
int remove_word(int fd, int len);
int send_backspace(int fd);
int send_space(int fd);
int send_enter(int fd);

#endif
