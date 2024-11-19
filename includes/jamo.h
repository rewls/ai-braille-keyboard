#ifndef JAMO_H
#define JAMO_H

#include <stdio.h>
#include <wchar.h>
#include <locale.h>
#include <stdlib.h>

unsigned int ch2wch(char *input, wchar_t* output);
void jamo(wchar_t* wstr, wchar_t* output);

#endif
