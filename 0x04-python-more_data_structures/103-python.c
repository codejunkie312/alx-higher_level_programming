#include "Python.h"
#include <stdio.h>

/**
 * print_python_list - prints info about python bytes
 * @p: pointer to PyObject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes.
 * @p: Pointer to PyObject
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *bytes_content;

	printf("[*] Python bytes\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	bytes_content = PyBytes_AsString(p);
	printf("[*] Size of the Python Bytes = %ld\n", size);
	printf("[*] Trying string: %s\n", bytes_content);

	if (size < 10)
		printf("[*] First %ld bytes: ", size);
	else
		printf("[*] First 10 bytes: ");

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", bytes_content[i]);
		if (i < 9 && i < size - 1)
			printf(" ");
	}
	printf("\n");
}
