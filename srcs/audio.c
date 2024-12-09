#include "audio.h"

#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>

#include "jamo.h"
#include "key.h"

#define MAX_LEN 100

void play_audio(const wchar_t *text)
{
	char command[MAX_LEN];
	snprintf(command, sizeof(command), "espeak -v ko \"%S\" --stdout | "
			"aplay", text);
#ifdef DEBUG
	printf("%s\n", command);
#endif
	system(command);
}
