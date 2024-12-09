#ifndef JAMO_H
#define JAMO_H

#include <stdio.h>
#include <wchar.h>
#include <locale.h>
#include <stdlib.h>

static int buf_cnt = -1;

unsigned int ch2wch(const char *input, wchar_t* output);
unsigned int wch2ch(const wchar_t *input, char* output);
void jamo(wchar_t* wstr, wchar_t* output);

#endif
