def eat_ghost(power_pellet_active, touching_ghost): # The function should return True only if Pac-Man has a power pellet active and is touching a ghost.
    """ Verify that pacman can eat ghost if the power pellet is active and touching a ghost

    Args:
        power_pellet_active (bool): determine if the player has an active power pellet 
        touching_ghost (bool): determine if pacman touchig the ghost or not

    Returns:
        bool - can a ghost be eaten
    
    """
    return power_pellet_active and touching_ghost



def score(touching_power_pellet, touching_dot): #The function should return True if Pac-Man is touching a power pellet or a dot.
    """Verify that pacman has scored when a power pellet is active or dot has bee eaten

    Args:
        touching_power_pellet (bool): is pacman touching power pellet?
        touching_dot (bool): is pacman touchig dot

    Returns:
        bool - has the playered score or not
    
    """
    return touching_power_pellet or touching_dot



def lose(power_pellet_active, touching_ghost): # The function should return True if Pac-Man is touching a ghost and does not have a power pellet active.
    """Determine if pacman lose

    Args:
        power_pellet_active (bool): is the power pellet active?
        touching_ghost (bool): is pacman touchign ghost


    Returns:
        bool - is pacman lose?
    
    """
    return not power_pellet_active and touching_ghost



def win(has_eaten_all_dots, power_pellet_active, touching_ghost): #The function should return True if Pac-Man has eaten all of the dots and has not lost based on the parameters defined in part 3.
    """Determine if pacman wins

    Args:
        has_eaten_all_dots (bool): is pacman eaten all dots?
        power_pellet_active (bool): is power pellet active?
        touching_ghost (bool): is pacman touchig ghost

    Returns:
        bool - is pacman winns?
    
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)