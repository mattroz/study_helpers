#include <stdio.h>

int main()
{
	float l = 209;
	float n = 12;
	float s = 0;
	for(int i = 0; i < n; i++)
	{
		s += (l/n);
		printf("%f\n", s);
	}

	return 0;
}
