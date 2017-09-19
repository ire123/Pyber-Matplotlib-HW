# Dependencies
import matplotlib.pyplot as plt

import numpy as np



x_lim = 2 * np.pi

x_axis = np.arange(0, x_lim, 0.1)



sin = np.sin(x_axis)

cos = np.cos(x_axis)



# Create 2 rows, each with one plot

# this creates one subplot with one column, containing two plots, each occupying a single row.

# returns a tuple containing a figure and axes objects. 

fig, axes = plt.subplots(2)



axes[0].plot(x_axis, sin)

axes[0].set_title("Sine")

axes[0].set_xlim(0, x_lim)

axes[0].set_ylim(-1, 1)



axes[1].plot(x_axis, cos, color="red")

axes[1].set_title("Cosine")

axes[1].set_xlim(0, x_lim)

axes[1].set_ylim(-1, 1)



#fixes spacing issues:

plt.tight_layout()
plt.savefig("TEST.png")
plt.show()

				

 





						
						





		

	

		



 
			

		
										
						
			
		
		
		

		

				
		
		
		
	

				


	
			

	
				

				
										
