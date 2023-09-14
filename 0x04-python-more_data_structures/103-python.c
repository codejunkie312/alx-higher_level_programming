#include "Python.h"
#include <stdio.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints info about python bytes
 * @p: pointer to PyObject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *item;
	PyListObject *list_obj = (PyListObject *)p;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %zd\n", list_obj->allocated);

	for (i = 0; i < size; i++)
	{
		item = list_obj->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);

		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
		{
			print_python_bytes(item);
		}
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

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	bytes_content = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_content);

	if (size < 10)
		printf("  first %ld bytes: ", size + 1);
	else
		printf("  first 10 bytes: ");

	for (i = 0; i <= size && i < 10; i++)
	{
		printf("%02hhx", bytes_content[i]);
		if (i < 9 && i != size)
			printf(" ");
	}
	printf("\n");
}
