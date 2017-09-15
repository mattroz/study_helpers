#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n = 13;
	float dt[13] = {0.0, 99.3, 195.5, 286.0, 370.2, 448.8, 524.2, 590.1, 559.3, 376.9, 152.4, -3.0, 0.0};
	float dt1[13] = {-22.9, 41.9, 82.0, 164.7, 288.5, 409.5, 501.2, 550.8, 477.7, 255.6, 39.0, -60.4, -22.9};
	int m = 10;	

	puts("dT");
	for(int i = 0; i < n; i++)
	{
		printf("%d) %f\t%f\n", i+1, (dt[i] / m), (dt1[i] / m));
	}
	
	return 0;
}
