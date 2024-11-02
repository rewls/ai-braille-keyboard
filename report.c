#include <wchar.h>
#include <string.h>
#include <stdio.h>

#define REPORT_BYTE 8
#define ID(c) ((c) - ('a' - 0x04))
#define LEFT_CONTROL 0x01
#define LEFT_SHIFT 0x02

enum kor_syllable {ini, med, fin};

char initial[][8] = {
	{[2] = ID('r')},			// ᄀ
	{[0] = LEFT_SHIFT, [2] = ID('r')},	// ᄁ
	{[2] = ID('s')},			// ᄂ
	{[2] = ID('e')},			// ᄃ
	{[0] = LEFT_SHIFT, [2] = ID('e')},	// ᄄ
	{[2] = ID('f')},			// ᄅ
	{[2] = ID('a')},			// ᄆ
	{[2] = ID('q')},			// ᄇ
	{[0] = LEFT_SHIFT, [2] = ID('q')},	// ᄈ
	{[2] = ID('t')},			// ᄉ
	{[0] = LEFT_SHIFT, [2] = ID('t')},	// ᄊ
	{[2] = ID('d')},			// ᄋ
	{[2] = ID('w')},			// ᄌ
	{[0] = LEFT_SHIFT, [2] = ID('w')},	// ᄍ
	{[2] = ID('c')},			// ᄎ
	{[2] = ID('z')},			// ᄏ
	{[2] = ID('x')},			// ᄐ
	{[2] = ID('v')},			// ᄑ
	{[2] = ID('g')},			// ᄒ
};

char medial[][8] = {
	{[2] = ID('k')},			// ᅡ
	{[2] = ID('o')},			// ᅢ
	{[2] = ID('i')},			// ᅣ
	{[0] = LEFT_SHIFT, [2] = ID('o')},	// ᅤ
	{[2] = ID('j')},			// ᅥ
	{[2] = ID('p')},			// ᅦ
	{[2] = ID('u')},			// ᅧ
	{[0] = LEFT_SHIFT, [2] = ID('p')},	// ᅨ
	{[2] = ID('h')},			// ᅩ
	{[2] = ID('h'), [3] = ID('k')},		// ᅪ
	{[2] = ID('h'), [3] = ID('o')},		// ᅫ
	{[2] = ID('h'), [3] = ID('l')},		// ᅬ
	{[2] = ID('y')},			// ᅭ
	{[2] = ID('n')},			// ᅮ
	{[2] = ID('n'), [3] = ID('j')},		// ᅯ
	{[2] = ID('n'), [3] = ID('p')},		// ᅰ
	{[2] = ID('n'), [3] = ID('l')},		// ᅱ
	{[2] = ID('b')},			// ᅲ
	{[2] = ID('m')},			// ᅳ
	{[2] = ID('m'), [3] = ID('l')},		// ᅴ
	{[2] = ID('l')},			// ᅵ
};

char final[][8] = {
	{[2] = ID('r')},			// ᆨ
	{[0] = LEFT_SHIFT, [2] = ID('r')},	// ᆩ
	{[2] = ID('r'), [3] = ID('t')},		// ᆪ
	{[2] = ID('s')},			// ᆫ
	{[2] = ID('s'), [3] = ID('w')},		// ᆬ
	{[2] = ID('s'), [3] = ID('g')},		// ᆭ
	{[2] = ID('s')},			// ᆮ
	{[2] = ID('f')},			// ᆯ
	{[2] = ID('f'), [3] = ID('r')},		// ᆰ
	{[2] = ID('f'), [3] = ID('a')},		// ᆱ
	{[2] = ID('f'), [3] = ID('q')},		// ᆲ
	{[2] = ID('f'), [3] = ID('t')},		// ᆳ
	{[2] = ID('f'), [3] = ID('x')},		// ᆴ
	{[2] = ID('f'), [3] = ID('v')},		// ᆵ
	{[2] = ID('f'), [3] = ID('g')},		// ᆶ
	{[2] = ID('a')},			// ᆷ
	{[2] = ID('q')},			// ᆸ
	{[2] = ID('q'), [3] = ID('t')},		// ᆹ
	{[2] = ID('t')},			// ᆺ
	{[0] = LEFT_SHIFT, [2] = ID('t')},	// ᆻ
	{[2] = ID('d')},			// ᆼ
	{[2] = ID('w')},			// ᆽ
	{[2] = ID('w')},			// ᆾ
	{[2] = ID('z')},			// ᆿ
	{[2] = ID('x')},			// ᇀ
	{[2] = ID('v')},			// ᇁ
	{[2] = ID('g')},			// ᇂ
};

int kor2report(char report[REPORT_BYTE], wchar_t c, enum kor_syllable s)
{
	if (s == ini && c >= L'ᄀ' && c <= L'ᄒ')
		memcpy(report, initial[c - L'ᄀ'], REPORT_BYTE);
	else if (s == med && c >= L'ᅡ' && c <= L'ᅵ')
		memcpy(report, medial[c - L'ᅡ'], REPORT_BYTE);
	else if (s == fin && c >= L'ᆨ' && c <= L'ᇂ')
		memcpy(report, final[c - L'ᆨ'], REPORT_BYTE);
	else
		return -1
	return 8;
}

int send_report(wchar_t c)
{
	int fd = 0;
	char report[8];
	int to_send = 8;

	if ((fd = open("/dev/hidg0", O_RDWR, 0666)) == -1) {
		perror(filename);
		return 1;
	}
	if (to_send = kor2report(report, L'ᆨ', fin) == -1) {
		close(fd);
		return 0;
	}
	if (write(fd, report, to_send) != to_send) {
		perror(filename);
		return 2;
	}

	for (int i = 0; i < 8; i++)
		printf("%d ", report[i]);

	close(fd);
	return 0;
}
