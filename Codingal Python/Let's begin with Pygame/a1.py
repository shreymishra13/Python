# Import Necessary Libraries
import pygame  
  
# Initialize required modules
pygame.init()  

# Setup window geometry
screen = pygame.display.set_mode((500,500))  


  
while True: 

	# Clear the event queue
	for event in pygame.event.get():  
		if event.type == pygame.QUIT:  
			pygame.quit()
	