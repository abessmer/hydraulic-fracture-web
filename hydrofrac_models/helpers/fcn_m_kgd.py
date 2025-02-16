def fcn_m_kgd(rho, s):
    """
    TODO describe this function

    Args:
        rho: (float or numpy.ndarray) -  
        s: (float or numpy.ndarray) - 

    Returns:
        M: (float or numpy.ndarray) - 
                                    Will be of the same type and shape as inputs if inputs are arrays,
                                    or a float if inputs are floats.
    """
      
    return s / (s**2 - rho**2)