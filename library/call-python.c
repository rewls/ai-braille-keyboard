#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define NUM_WORD 3
#define MAX_LEN 100

char **call_recommend_word(char *argument)
{
	char *pythonfile = "word_recommendation";
	char *funcname = "recommend_word";
	PyObject *pName, *pModule, *pFunc;
	PyObject *pArgs, *pValue;
	char **word_list;
	int i;

	word_list = malloc(NUM_WORD * sizeof(char *));
	for (i = 0; i < NUM_WORD; i++)
		word_list[i] = malloc(MAX_LEN);

	Py_Initialize();
	pName = PyUnicode_FromString(pythonfile);
	/* Error checking of pName left out */

	pModule = PyImport_Import(pName);
	Py_DECREF(pName);

	if (pModule != NULL) {
		pFunc = PyObject_GetAttrString(pModule, funcname);
		/* pFunc is a new reference */

		if (pFunc && PyCallable_Check(pFunc)) {
			pArgs = PyTuple_New(1);
			for (i = 0; i < 1; ++i) {

				pValue = PyUnicode_FromString(argument);
				if (!pValue) {
					Py_DECREF(pArgs);
					Py_DECREF(pModule);
					fprintf(stderr, "Cannot convert argument\n");
					return NULL;
				}
				/* pValue reference stolen here: */
				PyTuple_SetItem(pArgs, i, pValue);
			}
			pValue = PyObject_CallObject(pFunc, pArgs);
			Py_DECREF(pArgs);
			if (pValue != NULL) {
				PyObject *pWord;
				for (i = 0; i < NUM_WORD; i++) {
					pWord = PyList_GetItem(pValue, i);
					strcpy(word_list[i], PyUnicode_AsUTF8(pWord));
					Py_DECREF(pValue);
					Py_DECREF(pWord);
				}
				return word_list;
			}
			else {
				Py_DECREF(pFunc);
				Py_DECREF(pModule);
				PyErr_Print();
				fprintf(stderr,"Call failed\n");
				return NULL;
			}
		}
		else {
			if (PyErr_Occurred())
				PyErr_Print();
			fprintf(stderr, "Cannot find function \"%s\"\n", funcname);
		}
		Py_XDECREF(pFunc);
		Py_DECREF(pModule);
	}
	else {
		PyErr_Print();
		fprintf(stderr, "Failed to load \"%s\"\n", pythonfile);
		return NULL;
	}
	if (Py_FinalizeEx() < 0) {
		return NULL;
	}
	return NULL;
}

int main(void)
{
	char **word_list = call_recommend_word("안");
	for (int i = 0; i < NUM_WORD; i++)
		printf("%s\n", word_list[i]);
	return 0;
}
