#ifndef REPORT_H
#define REPORT_H

#include <wchar.h>

#define REPORT_BYTE 8

enum kor_syllable {ini, med, fin};

int kor2report(char report[REPORT_BYTE], wchar_t c, enum kor_syllable s);
void write_kor(int fd, wchar_t c, enum kor_syllable s);
void remove_word(int fd);

#endif
