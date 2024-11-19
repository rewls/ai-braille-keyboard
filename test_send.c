#include <stdio.h>
#include <wchar.h>
#include <locale.h>
#include <pthread.h>
#include <string.h>
#include <ctype.h>
#include <fcntl.h>
#include <errno.h>
#include <stdlib.h>
#include <unistd.h>

#include "jamo.h"
#include "report.h"
#include "braille.h"

int main()
{	
    int braille_list[4] = {35, 18, 9, 59};
    for(int i=0; i<4; i++)
    {
        send_keycode(braille_list[i]);
        sleep(1);
    }
	return 0;
}
