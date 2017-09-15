#include <stdio.h>

int main()
{
	float mps[13] = {24.0, 20.8, 12.0, 0.0, -12.0, -20.8, -24.0, -74.3, -419.9, -596.7, -562.7, -334.8, 24.0};
	int n = 13;
	int m = 10;

	for(int i = 0; i < n; i++)
	{
		printf("%d) %f\t%f\n", i+1, mps[i]/m, 166.8/m);
	}

	return 0;
}
