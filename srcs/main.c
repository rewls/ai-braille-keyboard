#include <stdbool.h>
#include <stdio.h>
#include <unistd.h>

#include <wiringPi.h>

#include "audio.h"
#include "braille.h"
#include "call-python.h"
#include "jamo.h"
#include "key.h"
#include "report.h"

#define MAX_BUF 1000
#define MAX_LEN 100

wchar_t buf[MAX_BUF] = L"";
wchar_t word[MAX_LEN] = L"";

int correct_word(int fd, const int *row, const int *col)
{
	wchar_t corrected_word[MAX_LEN];
	int flag;

	call_correct_spelling(word, corrected_word);
#ifdef DEBUG
	printf("corrected word : %S\n", corrected_word);
#endif

	flag = -1;
	digitalWrite(col[1], HIGH);
	while (flag == -1) {
		if (digitalRead(row[3]) == HIGH)
			flag = 1;
		else
			flag = 0;
		usleep(100 * 10);
	}
	digitalWrite(col[1], LOW);

	if (flag == 0)
		return 0;
	if (send_backspace(fd) != 0)
		return 1;
	if (remove_word(fd, wcslen(word)) != 0)
		return 1;
	if (write_word(fd, corrected_word) != 0)
		return 1;
	if (send_space(fd) != 0)
		return 1;
	play_audio(correct_word);
	wcscpy(buf + buf_cnt - wcslen(corrected_word), corrected_word);
	return 0;
}

void print_dot(bool *dot)
{
	printf("dot states:");
	for (int i = 0; i < NUM_DOT; i++)
		printf(" %d", dot[i]);
	putchar('\n');
}

int main(void)
{
	// WirintPi number
	const int col[NUM_COL] = {0, 2, 3};
	const int row[NUM_ROW] = {4, 5, 6, 7};

	int fd;
	int key;
	int braille;
	bool dot[NUM_DOT] = {false};
	char tmp_ch[MAX_LEN] = "";
	wchar_t tmp[MAX_LEN] = L"";

	if (pin_init(row, col) != 0)
		return 1;
	fd = hid_init();
	if (fd == -1)
		return 1;
	setlocale(LC_ALL, "ko_KR.UTF-8");
	setenv("PYTHONPATH", "srcs", 1);
	init_spell_coreprection();

	play_audio(L"안녕하세요");
	while (1) {
		key = scan_key(row, col);
		switch (key) {
			case DOT1: case DOT2: case DOT3:
			case DOT4: case DOT5: case DOT6:
				if (dot[key] == false)
					play_audio((wchar_t [2]){'1' + key});
				else {
					snprintf(tmp_ch, sizeof(tmp_ch), "%d 취소", key + 1);
					ch2wch(tmp_ch, tmp);
					play_audio(tmp);
				}
				dot[key] = !dot[key];
#ifdef DEBUG
				print_dot(dot);
#endif
				break;
			case DELETE:
				play_audio(L"delete");
				if (send_backspace(fd) != 0)
					return 1;
				memset(dot, 0, NUM_DOT);
				break;
			case ENTER:
				play_audio(L"enter");
				if (send_enter(fd) != 0)
					return 1;
				memset(dot, 0, NUM_DOT);
				break;
			case SEND:
				braille = get_braille(dot);
				;
				play_audio((wchar_t [2]){b2k(fd, braille, buf, word)});
				memset(dot, 0, NUM_DOT);
				if (braille == 0) {
					play_audio(L"공백");
					correct_word(fd, row, col);
				}
		}
	}
	return 0;
}
