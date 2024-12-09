#ifndef BRAILLE_H
#define BRAILLE_H

#include <stdio.h>
#include <wchar.h>
#include <locale.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>
#include <fcntl.h>
#include <errno.h>
#include <stdlib.h>
#include <stdbool.h>

#define NUM_DOT 6

enum kor_syllable {ini, med, fin, abbr};
typedef struct
{
	wchar_t letter;
	enum kor_syllable status;
} LETTER;

LETTER br2kor(void);
wchar_t b2k(int fd, int braille, wchar_t *buf, wchar_t *word);
int get_braille(bool *dot);

#endif
