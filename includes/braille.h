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

static int pre_br = 0;
static int cur_br = 0;
static int flag_table[4] = {0,0,0,0};
static int buf_cnt = 0;
static int word_cnt = 0;
static int cjj[] = {-1,-1,0};
static wchar_t cho,jung,jong,ret;

enum kor_syllable {ini, med, fin, abbr};
typedef struct
{
	wchar_t letter;
	enum kor_syllable status;
} LETTER;

LETTER br2kor(void);
void b2k(int fd, int braille, wchar_t *buf, wchar_t *word);
void send_keycode(int fd, wchar_t* s);
void charsend(int fd, char* input);

#endif
