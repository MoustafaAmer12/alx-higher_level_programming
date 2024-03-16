#include <Python.h>

/**
 * print_python_list_info - prints some information related to pyhton list
 * @p: PyObject containing the list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i = 0;
	Pyobject *list;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] allocated = %d\n", alloc);

	for (; i < size; i++)
	{
		printf("Element %d: ", i);
		list = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(list)->tp_name);
	}
}
