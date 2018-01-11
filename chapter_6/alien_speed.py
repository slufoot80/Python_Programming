alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
print("Original x-position: " + str(alien_0['x_position']))

#Move to the right
#Determine how far to move the alien based on speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 4

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
 
