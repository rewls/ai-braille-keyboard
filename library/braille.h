#ifndef BRAILLE_H
#define BRAILLE_H

wchar_t br2kor(void);
int b2k(int braille, wchar_t *buf, wchar_t *word);
void send_keycode(int braille);

#endif
