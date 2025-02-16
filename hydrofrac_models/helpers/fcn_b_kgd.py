import scipy.special as sp
from .fcn_delta_p import fcn_delta_p
from .fcn_lam_kgd import fcn_lam_kgd

def fcn_b_kgd(Kh, Ch, alp):
  """
  Describe this function

  Calculates B based on Kh, Ch, and alp.
  This function seems to be related to some physical model (KGD).

  Args:
    Kh: (float) -  Likely a parameter related to hydraulic conductivity or similar.
    Ch: (float) - Likely a dimensionless parameter, possibly related to heterogeneity.
    alp: (float) - Likely a parameter, potentially related to a power law exponent.

  Returns:
    B: (float) - The calculated value based on the formula.
  """

  p = 0.0  # parameter for delta calculation

  delta_val = (1 + fcn_delta_p(Kh, Ch, p)) / 2

  lam = fcn_lam_kgd(Kh, Ch, alp) # Calculate lambda

  # Define B0 as a lambda function (anonymous function in Python)
  # beta function in scipy.special is sp.beta
  # incomplete beta function in scipy.special is sp.betainc (regularized)
  # We need to use the regular beta function and regularized incomplete beta function
  # and adjust to match the Matlab beta and betainc behavior if needed.

  B0 = lambda x, p1, p2: sp.beta(p1, p2) * (1 - sp.betainc(p1, p2, x))

  # Calculate B
  # beta function in scipy.special is sp.beta
  B = 2**(1 + delta_val) * B0(0.5, lam + 1, 1 + delta_val) + Ch * alp**(3/2) * sp.beta(alp, 3/2)

  return B