#include "jamo.h"

#define HANGUL_START L'가'
#define HANGUL_END L'힣'
#define CHO(wc) (((wc) - HANGUL_START) / (21 * 28))
#define JUNG(wc) ((((wc) - HANGUL_START) % (21 * 28)) / 28)
#define JONG(wc) (((wc) - HANGUL_START) % 28)

unsigned int ch2wch(const char *input, wchar_t* output)
{
	size_t len = mbstowcs(NULL, input, 0) + 1;
	mbstowcs(output, input, len);
	return len - 1;
}

unsigned int wch2ch(const wchar_t *input, char* output)
{
	size_t len = wcstombs(NULL, input, 0) + 1;
	wcstombs(output, input, len);
	return len - 1;
}

void jamo(wchar_t* wstr, wchar_t* output)
{
	int index = 0;

	while (*wstr) {
		if (*wstr >= HANGUL_START && *wstr <= HANGUL_END) {
			output[index++] = CHO(*wstr) + 0x1100;
			output[index++] = JUNG(*wstr) + 0x1161;
			if (JONG(*wstr) != 0)
				output[index++] = JONG(*wstr) + 0x11a7;
		}
		else 
			output[index++] = *wstr;
		wstr++;
	}
	output[index] = L'\0';
}
