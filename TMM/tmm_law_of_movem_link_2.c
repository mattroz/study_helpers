#include <stdio.h>

int main()
{
	float ac[13] = {0.0, 12.0, 20.8, 24.0, 20.8, 12.0, 0.0, -21.4, -139.5, -409.3, -721.2, -963.9, -1048.3};
	float ad[13] = {0.0, 87.4, 174.7, 262.1, 349.4, 436.8, 524.2, 611.5, 698.9, 786.2, 873.6, 961.0, 1048.3};
	int n = 13;
	int m = 10;

	for(int i = 0; i < n; i++)
	{
		printf("%d) %f\t%f\n", i+1, ac[i]/m, ad[i]/m);
	}

	return 0;
}
