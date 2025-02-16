import numpy as np
from .helpers.global_kgd_solution import global_kgd_solution
from .helpers.kgd_local_solutions import kgd_k_solution, kgd_kt_solution, kgd_m_solution, kgd_mt_solution
from .material_parameters import MaterialParameters


class KgdFractureSolution:
    normalized_length: float
    normalized_width: np.ndarray
    normalized_pressure: np.ndarray
    normalized_coordinate: np.ndarray
    efficiency: float

    def __init__(self,
                 normalized_length,
                 normalized_width,
                 normalized_pressure,
                 normalized_coordinate,
                 efficiency):
        self.normalized_length = normalized_length
        self.normalized_width = normalized_width
        self.normalized_pressure = normalized_pressure
        self.normalized_coordinate = normalized_coordinate
        self.efficiency = efficiency


class KgdFracture:
    material_parameters: MaterialParameters

    def __init__(self, material_params: MaterialParameters):
        self.material_parameters = material_params

    def calculate_global_solution(self, grid_size: int) -> KgdFractureSolution:
        (normalized_length,
         normalized_width,
         normalized_pressure,
         normalized_coordinate,
         efficiency) = global_kgd_solution(
            self.material_parameters.youngs_modulus,
            self.material_parameters.fluid_viscosity,
            self.material_parameters.fracture_toughness,
            self.material_parameters.porosity,
            self.material_parameters.fluid_injection_rate /
            self.material_parameters.fracture_height,
            self.material_parameters.time,
            grid_size)
        return KgdFractureSolution(normalized_length,
                                   normalized_width,
                                   normalized_pressure,
                                   normalized_coordinate,
                                   efficiency)

    def calculate_local_solution(self, grid_size: int, propagation_regime: str) -> KgdFractureSolution:
        if propagation_regime == 'K':
            (normalized_length,
             normalized_width,
             normalized_pressure,
             normalized_coordinate,
             efficiency) = kgd_k_solution(
                self.material_parameters.youngs_modulus,
                self.material_parameters.fluid_viscosity,
                self.material_parameters.fracture_toughness,
                self.material_parameters.porosity,
                self.material_parameters.fluid_injection_rate /
                self.material_parameters.fracture_height,
                self.material_parameters.time,
                grid_size)
        elif propagation_regime == 'M':
            (normalized_length,
             normalized_width,
             normalized_pressure,
             normalized_coordinate,
             efficiency) = kgd_m_solution(
                self.material_parameters.youngs_modulus,
                self.material_parameters.fluid_viscosity,
                self.material_parameters.fracture_toughness,
                self.material_parameters.porosity,
                self.material_parameters.fluid_injection_rate /
                self.material_parameters.fracture_height,
                self.material_parameters.time,
                grid_size)
        elif propagation_regime == 'Kt':
            (normalized_length,
             normalized_width,
             normalized_pressure,
             normalized_coordinate,
             efficiency) = kgd_kt_solution(
                self.material_parameters.youngs_modulus,
                self.material_parameters.fluid_viscosity,
                self.material_parameters.fracture_toughness,
                self.material_parameters.porosity,
                self.material_parameters.fluid_injection_rate /
                self.material_parameters.fracture_height,
                self.material_parameters.time,
                grid_size)
        elif propagation_regime == 'Mt':
            (normalized_length,
             normalized_width,
             normalized_pressure,
             normalized_coordinate,
             efficiency) = kgd_mt_solution(
                self.material_parameters.youngs_modulus,
                self.material_parameters.fluid_viscosity,
                self.material_parameters.fracture_toughness,
                self.material_parameters.porosity,
                self.material_parameters.fluid_injection_rate /
                self.material_parameters.fracture_height,
                self.material_parameters.time,
                grid_size)
        else:
            return None

        return KgdFractureSolution(normalized_length,
                                   normalized_width,
                                   normalized_pressure,
                                   normalized_coordinate,
                                   efficiency)
