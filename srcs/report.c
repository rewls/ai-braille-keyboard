#include "report.h"

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <wchar.h>

#define ID(c) ((c) - ('a' - 0x04))
#define LEFT_CONTROL 0x01
#define LEFT_SHIFT 0x02
#define BACKSPACE 0x2A
#define RIGHT 0x4f
#define SPACEBAR 0x2c
#define ENTER 0x28

static char initial[][REPORT_BYTE] = {
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

static char medial[][REPORT_BYTE] = {
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

static char final[][REPORT_BYTE] = {
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
	{[2] = ID('c')},			// ᆾ
	{[2] = ID('z')},			// ᆿ
	{[2] = ID('x')},			// ᇀ
	{[2] = ID('v')},			// ᇁ
	{[2] = ID('g')},			// ᇂ
};

static int send_report(int fd, char report[REPORT_BYTE])
{
	if (write(fd, report, REPORT_BYTE) != REPORT_BYTE) {
		perror(__FUNCTION__);
		return 1;
	}
	return 0;
}

int kor2report(char report[REPORT_BYTE], wchar_t c)
{
	if (c >= L'ᄀ' && c <= L'ᄒ')
		memcpy(report, initial[c - L'ᄀ'], REPORT_BYTE);
	else if (c >= L'ᅡ' && c <= L'ᅵ')
		memcpy(report, medial[c - L'ᅡ'], REPORT_BYTE);
	else if (c >= L'ᆨ' && c <= L'ᇂ')
		memcpy(report, final[c - L'ᆨ'], REPORT_BYTE);
	else if (c == L'^')
	{
		char temp[REPORT_BYTE] = {[2] = SPACEBAR, [3] = BACKSPACE};
		memcpy(report, temp, REPORT_BYTE);
	}
	else
		return 1;
	return 0;
}

void write_kor(int fd, wchar_t c)
{
	char report[REPORT_BYTE];

	if (kor2report(report, c) != 0)
		close(fd);
	send_report(fd, report);
	memset(report, 0x0, sizeof(report));
	send_report(fd, report);
}

void remove_word(int fd)
{
	char report[REPORT_BYTE] = {[0] = LEFT_CONTROL, [2] = BACKSPACE};
	send_report(fd, report);
	memset(report, 0x0, sizeof(report));
	send_report(fd, report);
}

void remove_letter(int fd)
{
	char report[REPORT_BYTE] = {[2] = BACKSPACE};
	send_report(fd, report);
	memset(report, 0x0, sizeof(report));
	send_report(fd, report);
}


void write_space(int fd)
{
	char report[REPORT_BYTE] = {[2] = SPACEBAR};
	send_report(fd, report);
	memset(report, 0x0, sizeof(report));
	send_report(fd, report);
}

void write_enter(int fd)
{
	char report[REPORT_BYTE] = {[2] = ENTER};
	send_report(fd, report);
	memset(report, 0x0, sizeof(report));
	send_report(fd, report);
}