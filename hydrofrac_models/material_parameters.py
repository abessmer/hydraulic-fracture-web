import numpy as np


class MaterialParameters:
    def __init__(self,
                 youngs_modulus,
                 fluid_viscosity,
                 fracture_toughness,
                 fluid_injection_rate,
                 fracture_height,
                 time,
                 porosity):
        self.youngs_modulus = youngs_modulus  # Ep, GPa
        self.fluid_viscosity = fluid_viscosity  # mup, Pa s
        self.fracture_toughness = fracture_toughness  # Kp, MPa*m^(1/2)
        self.fluid_injection_rate = fluid_injection_rate  # Q0, [m^3/s]*10^-3
        self.fracture_height = fracture_height  # H, m
        self.time = time  # t, seconds
        self.porosity = porosity  # Cp, Compressibility parameter

    @staticmethod
    def get_k_regime():
        return MaterialParameters(
            9.5 / (1 - 0.2**2),  # GPa
            12 * 3e-3,         # Pa s
            4 * (2 / np.pi)**0.5 * 1,  # MPa*m^(1/2)
            0.0005 * 1e3,       # [m^3/s]*10^-3
            50,                  # m
            1000,                # s (Time)
            2 * 3 * 1e-7 * 1e3    # Compressibility parameter
        )

    @staticmethod
    def get_m_regime():
        return MaterialParameters(
            15 / (1 - 0.2**2),  # GPa
            12 * 0.2,          # Pa s
            4 * (2 / np.pi)**0.5 * 1,  # MPa*m^(1/2)
            0.001 * 1e3,        # [m^3/s]*10^-3
            50,                  # m
            1000,                # s (Time)
            2 * 3 * 1e-7 * 1e3    # Compressibility parameter
        )

    @staticmethod
    def get_kt_regime():
        return MaterialParameters(
            3 / (1 - 0.2**2),   # GPa
            12 * 3 * 1e-3,      # Pa s
            4 * (2 / np.pi)**0.5 * 1,  # MPa*m^(1/2)
            0.02 * 1e3,         # [m^3/s]*10^-3
            50,                  # m
            1000,                # s (Time)
            2 * 5 * 1e-4 * 1e3    # Compressibility parameter
        )

    @staticmethod
    def get_mt_regime():
        return MaterialParameters(
            15 / (1 - 0.2**2),  # GPa
            12 * 0.01,         # Pa s
            4 * (2 / np.pi)**0.5 * 1,  # MPa*m^(1/2)
            0.01 * 1e3,         # [m^3/s]*10^-3
            50,                  # m
            1000,                # s (Time)
            2 * 1e-4 * 1e3      # Compressibility parameter
        )

    @staticmethod
    def get_intermediate_regime():
        return MaterialParameters(
            15 / (1 - 0.2**2),  # GPa
            12 * 0.02,         # Pa s
            4 * (2 / np.pi)**0.5 * 1,  # MPa*m^(1/2)
            0.0004 * 1e3,       # [m^3/s]*10^-3
            50,                  # m
            1000,                # s (Time)
            2 * 3 * 1e-6 * 1e3    # Compressibility parameter
        )
