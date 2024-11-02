#include <stdio.h>
#include <wchar.h>
#include <locale.h>

static int pre_br = 0;
static int cur_br = 0;
static int flag_table[4] = { 0,0,0,0 };
static int buf_cnt = 0;
static int word_cnt = 0;
static int cjj[] = { -1, -1, 0 };
static wchar_t cho, jung, jong, ret;

enum kor_syllable {ini, med, fin};

typedef struct
{
	wchar_t letter;
	enum kor_syllable status;
} LETTER;

LETTER br2kor(void)
{
	LETTER output;
	wchar_t kor_table[][2] = { {L' '}, {0x11a8}, {0x11af}, {0x11b8},
		{0x11ba}, {0x11bd}, {0x11be}, {0xc0ac, L' '},
		{0x1100,0x1101}, {0x1102}, {0x1103, 0x1104}, {0x110f},
		{0x1168, 0x11bb}, {0x116e, 0x1171}, {0x1165}, {0x116f, 0x1170},
		{0x1105}, {0x1106}, {0x11ab}, {0x1110},
		{0x11ae}, {0x1175}, {0x11bf}, {0x1162},
		{0x1107, 0x1108}, {L' '}, {0x1112}, {0xc6b4},
		{0x1163, 0x1164}, {0x1166}, {0xc4bc}, {0xc778},
		{0x1109, 0x110a}, {0xc5f0}, {0x11b7}, {0x1161},
		{L'-'}, {0x1169}, {0x11c0}, {0x116a, 0x116b},
		{0x110c, 0x110d}, {0x1172}, {0x1173}, {0xac00},
		{0x116d}, {0xc625}, {0xc744}, {0xc6b8},
		{0x110e}, {0x1167}, {0x11c1}, {0xc5f4},
		{0x11c2}, {0xc740}, {0x11bc}, {0xc628},
		{L' '}, {0xc5b5}, {0x1174}, {0xc601},
		{L' '}, {0x116c}, {0xc5b8}, {0xc639} };

	int j = 0;
	int br_type = 0;
	int flag_cho = 0;
	int flag_jung = 0;
	int flag_jong = 0;
	int flag_word = 0;
	int flag_sol = 0;

	if ((cur_br >= 8 && cur_br <= 11) || cur_br == 16 || cur_br == 17 || cur_br == 19 ||
		cur_br == 24 || cur_br == 26 || cur_br == 32 || cur_br == 40 || cur_br == 48) br_type = 1;
	else if ((cur_br >= 12 && cur_br <= 15) || cur_br == 21 || cur_br == 23 || cur_br == 28 || cur_br == 29 || cur_br == 35 ||
		cur_br == 37 || cur_br == 39 || cur_br == 41 || cur_br == 42 || cur_br == 44 || cur_br == 49 || cur_br == 58 || cur_br == 61) br_type = 2;
	else if ((cur_br >= 1 && cur_br <= 6) || cur_br == 18 || cur_br == 20 || cur_br == 22 ||
		cur_br == 34 || cur_br == 38 || cur_br == 50 || cur_br == 52 || cur_br == 54) br_type = 3;
	else if (cur_br == 0 || cur_br == 25 || cur_br == 36 || cur_br == 56 || cur_br == 60) br_type = 0;
	else br_type = 4;

	switch (br_type) {
	case 1:
		if (pre_br == 32 && (cur_br == 8 || cur_br == 10 || cur_br == 24 || cur_br == 32 || cur_br == 40)) j = 1;		
		else j = 0;
		flag_cho = 1;
		output.status = ini;
		break;
	case 2:
		if (pre_br == 23 && (cur_br == 28 || cur_br == 39 || cur_br == 15 || cur_br == 13)) j = 1;		
		else if (pre_br == 63) flag_sol = 1;		
		else if (cur_br == 12 && flag_table[1] == 1) j = 1;		
		else j = 0;
		flag_jung = 1;
		output.status = med;
		break;
	case 3:
		if (pre_br == 63 || pre_br == 56) flag_sol = 1;		
		flag_jong = 1;
		output.status = fin;
		break;
	case 4:
		if ((cur_br == 7 || cur_br == 34) && pre_br == 32) j = 1;		
		flag_word = 1;
		break;
	default:
		break;
	}

	flag_table[0] = flag_cho;
	flag_table[1] = flag_jung;
	flag_table[2] = flag_jong;
	flag_table[3] = flag_word;
	output.letter = kor_table[cur_br][j];
	
	return output;
}

void b2k(int braille, wchar_t* buf, wchar_t* word)
{
	setlocale(LC_ALL, "");

	cur_br = braille;
	ret = br2kor();
	pre_br = cur_br;

	if (flag_table[3] == 1)
	{
		cho = (ret - 0xac00) / (21 * 28);
		jung = ((ret - 0xac00) % (21 * 28)) / 28;
		jong = ((ret - 0xac00) % (21 * 28)) % 28;

		//printf("1\n");
		if (cjj[1] != -1)
		{
			buf[++buf_cnt] = ret;
			word[++word_cnt] = ret;
			cjj[0] = cho;
			cjj[1] = jung;
			cjj[2] = jong;
		}
		else if (cjj[0] != -1)
		{
			buf[buf_cnt] = cjj[0] * 21 * 28 + cjj[1] * 28 + cjj[2] + 0xac00;
			word[word_cnt] = cjj[0] * 21 * 28 + cjj[1] * 28 + cjj[2] + 0xac00;
			cjj[1] = jung;
			cjj[2] = jong;
		}
	}
	else if (flag_table[2] == 1)
	{
		cjj[2] = ret - 0x11a7;
		//printf("2\n");
	}
	else if (flag_table[1] == 1)
	{
		if (!(buf[buf_cnt] >= 0x1100 && buf[buf_cnt] <= 0x11FF))
		{
			buf_cnt++;
			cjj[0] = 0x110b - 0x1100;
			cjj[2] = 0;
			//printf("3_2\n");
		}
		cjj[1] = ret - 0x1161;
		//printf("3\n");
	}
	else if (flag_table[0] == 1)
	{
		if (buf[buf_cnt] >= 0x1100 && buf[buf_cnt] <= 0x1112)
		{
			buf[buf_cnt] = cjj[0] * 21 * 28 + 0xac00;
		}
		cjj[0] = ret - 0x1100;
		cjj[1] = -1;
		cjj[2] = 0;
		buf[++buf_cnt] = ret;
		word[++word_cnt] = ret;
		//printf("4\n");
	}

	if (cjj[1] != -1){
		buf[buf_cnt] = cjj[0] * 21 * 28 + cjj[1] * 28 + cjj[2] + 0xac00;
		word[word_cnt] = buf[buf_cnt];
	}
	
	if (braille == 0)
	{	
		word[++word_cnt] = '\0';
		word_cnt = 0;
		buf[++buf_cnt] = ret;
	}
	printf("output : %lc\n", ret);
	printf("output : %S\n", buf + 1);

}

