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
#define NUM_REC 3
#define SW_REC 

wchar_t buf[MAX_BUF] = L"";
wchar_t word[MAX_LEN] = L"";
extern int buf_cnt, word_cnt;

int correct_word(int fd)
{
	wchar_t corrected_word[MAX_LEN];
	int key;

	call_correct_spelling(word, corrected_word);
#ifdef DEBUG
	printf("corrected word : %S\n", corrected_word);
#endif

	key = scan_key();
	if (key != ENTER)
		return 0;
	if (send_backspace(fd) != 0)
		return 1;
	if (remove_word(fd, wcslen(word)) != 0)
		return 1;
	if (write_word(fd, corrected_word) != 0)
		return 1;
	if (send_space(fd) != 0)
		return 1;
	play_audio(corrected_word);
	wcscpy(buf + buf_cnt - wcslen(corrected_word), corrected_word);
	word_cnt = -1;
	return 0;
}

int recommend_word(int fd, wchar_t recommended_word[NUM_REC][MAX_LEN])
{
	int key;
	char tmp_ch[MAX_LEN] = "";
	wchar_t tmp[MAX_LEN] = L"";

	call_recommend_word(word, recommended_word);
#ifdef DEBUG
	printf("recommended word : %S, %S, %S\n", recommended_word[0],
			recommended_word[1], recommended_word[2]);
#endif
	snprintf(tmp_ch, sizeof(tmp_ch), "1번 %S, 2번 %S, 3번 %S", recommended_word[0],
			recommended_word[1], recommended_word[2]);
	ch2wch(tmp_ch, tmp);
	play_audio(tmp);
	key = scan_key();
	if (key < DOT1 || key > DOT3)
		return 0;
	if (remove_word(fd, wcslen(word)) != 0)
		return 1;
	if (write_word(fd, recommended_word[key]) != 0)
		return 1;
	play_audio(recommended_word[key]);
	wcscpy(buf + buf_cnt - wcslen(recommended_word[key]), recommended_word[key]);
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
	int fd;
	int key;
	int braille;
	bool dot[NUM_DOT] = {false};
	char tmp_ch[MAX_LEN] = "";
	wchar_t tmp[MAX_LEN] = L"";
	wchar_t recommended_word[NUM_ROW][MAX_LEN];

	if (pin_init() != 0)
		return 1;
	fd = hid_init();
	if (fd == -1)
		return 1;
	setlocale(LC_ALL, "ko_KR.UTF-8");
	setenv("PYTHONPATH", "srcs", 1);
	setenv("GOOGLE_API_KEY", "", 1);
	init_spell_coreprection();

	play_audio(L"안녕하세요");
	while (1) {
		key = scan_key();
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
				word_cnt--;
				buf_cnt--;
				break;
			case ENTER:
				play_audio(L"enter");
				if (send_enter(fd) != 0)
					return 1;
				memset(dot, 0, NUM_DOT);
				break;
			case SEND:
				braille = get_braille(dot);
				play_audio((wchar_t [2]){b2k(fd, braille, buf, word)});
				memset(dot, 0, NUM_DOT);
				if (braille == 0) {
					play_audio(L"공백");
					correct_word(fd);
				}
				break;
			case REC:
				play_audio(L"단어 추천");
#ifdef DEBUG
				printf("단어 추천");
#endif
				recommend_word(fd, recommended_word);
				memset(dot, 0, NUM_DOT);
		}
	}
	return 0;
}
