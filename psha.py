from typing import Protocol
import pandas as pd
from math import sqrt, log, exp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm




class Magnitude(Protocol):
    @property
    def m_min(self) -> float:
        ...

    @property
    def m_max(self) -> float:
        ...

    @property
    def beta(self) -> float:
        ...

    def __str__(self) -> str:
        ...




class Gutenberg_Richter(Magnitude):

    def __init__(self, m_min:float, m_max:float, b:float):
        self._m_min = m_min
        self._m_max = m_max
        self._beta = log(10) * b

    @property
    def m_min(self) -> float:
        return self._m_min

    @property
    def m_max(self) -> float:
        return self._m_max

    @property
    def beta(self) -> float:
        return self._beta

    def probability_density_func(self, magnitudes:np.ndarray):
        pdf = self.beta * np.exp(-self.beta * (magnitudes - self.m_min)) / (1 - np.exp(-self.beta * (self.m_max - self.m_min)))
        pdf[(magnitudes < self.m_min) | (magnitudes > self.m_max)] = 0
        return pdf

    def cumulative_distribution_func(self, magnitudes:np.ndarray):
        cdf = (1 - np.exp(-self.beta * (magnitudes - self.m_min))) / (1 - np.exp(-self.beta * (self.m_max - self.m_min)))
        cdf[(magnitudes < self.m_min)] = 0
        cdf[(magnitudes > self.m_max)] = 1
        return cdf

    def probability_of_occurrence(self, magnitudes:np.ndarray) -> np.ndarray:
        midpoints = (magnitudes[:-1] + magnitudes[1:]) / 2
        mags_lower = np.pad(midpoints, (1,0), mode='constant', constant_values= magnitudes[0] - (magnitudes[1] - magnitudes[0]) / 2)
        mags_upper = np.pad(midpoints, (0,1), mode='constant', constant_values= magnitudes[-1] + (magnitudes[-1] - magnitudes[-2]) / 2)
        return self.cumulative_distribution_func(mags_upper) - self.cumulative_distribution_func(mags_lower)

    def rate_of_occurrence(self, rupture_annual_activity_rate:float, magnitudes:np.ndarray) -> np.ndarray:
        return rupture_annual_activity_rate * self.probability_of_occurrence(magnitudes)

    def rate_of_exceedance(self, rupture_annual_activity_rate:float, magnitudes:np.ndarray) -> np.ndarray:
        return np.flipud(np.flipud(self.rate_of_occurrence(rupture_annual_activity_rate, magnitudes)).cumsum())

    def __str__(self) -> str:
        return f"Gutenburg-Richter [M_min: {self.m_min}, M_max: {self.m_max}, beta: {self.beta:.2f}]"
    
    
    
    
    
def generate_magnitudes(m_min:float, m_max:float, step:0.01):
    return np.arange(m_min + step/2, m_max - step/2, step)





class Rupture():

    def __init__(self, rup_type:str, magnitude_dist:Magnitude, annual_activity_rate:float):
        self.rup_type = rup_type
        self.magnitude = magnitude_dist
        self.annual_activity_rate = annual_activity_rate

    def __str__(self) -> str:
        return f"{self.rup_type} rupture, rate: {self.annual_activity_rate}, {self.magnitude}"





class Site():

    def __init__(self, shear_velocity_m_sec:float):
        self.shear_velocity = shear_velocity_m_sec # Vs
        self.ruptures = []
        self.rup_dists = []

    @property
    def m_min(self):
        if len(self.ruptures) == 0:
            return None
        return np.min([rup.magnitude.m_min for rup in self.ruptures])

    @property
    def m_max(self):
        if len(self.ruptures) == 0:
            return None
        return np.max([rup.magnitude.m_max for rup in self.ruptures])

    def add_rupture(self, rupture:Rupture, distance_km:float):
        self.ruptures.append(rupture)
        self.rup_dists.append(distance_km)

    def __str__(self) -> str:
        rup_str = "\n".join([f"@ {dist}km -> {rup}" for rup, dist in zip(self.ruptures, self.rup_dists)])
        return f"Site: Vs {self.shear_velocity}\nRuptures:\n{rup_str if rup_str else 'None'}"
    
    
    
    
    
class Ground_Motion_Model(Protocol):
    def load_data(self, **kwargs) -> pd.DataFrame:
        ...

    @property
    def periods(self) -> np.ndarray:
        ...

    def median(self, shear_velocity_m_sec:float, magnitudes:np.ndarray, rup_type:str, dist_km:float)->np.ndarray:
        ...

    def standard_deviation(self)->np.ndarray:
        ...





class Boore_1997(Ground_Motion_Model):

    def __init__(self) -> None:
        """
          Boore et al. 1997 coefficients
          Reference: https://iisee.kenken.go.jp/eqflow/reference/1_2.htm
        """
        self.df: pd.DataFrame = self.load_data()


    def load_data(self, path:str='Boore_et_al_1997.csv', index_col:str='Period')->pd.DataFrame:
        """Load GMM data from CSV."""
        df = pd.read_csv(path, header=0, index_col=index_col)
        df.drop([0], axis=0, inplace=True)
        df.index.name = index_col
        return df

    @property
    def periods(self)->np.ndarray:
        return self.df.index.values

    def median(self, shear_velocity_m_sec:float, magnitudes:np.ndarray, rup_type:str, dist_km:float)->np.ndarray:

        m = magnitudes.reshape(1,-1)
        r = np.sqrt(dist_km**2 + self.df['h']**2).to_numpy().reshape(-1,1)

        b2 = self.df['B2'].to_numpy().reshape(-1,1)
        b3 = self.df['B3'].to_numpy().reshape(-1,1)
        b5 = self.df['B5'].to_numpy().reshape(-1,1)
        bv = self.df['BV'].to_numpy().reshape(-1,1)
        va = self.df['VA'].to_numpy().reshape(-1,1)

        if rup_type.lower() == 'strike-slip':
            b1 = self.df['B1SS'].to_numpy().reshape(-1,1)
        elif rup_type.lower() == 'reverse-slip':
            b1 = self.df['B1RV'].to_numpy().reshape(-1,1)
        else:
            b1 = self.df['B1ALL'].to_numpy().reshape(-1,1)

        return np.exp(b1 + b2*(m-6) + b3*(m-6)**2 + b5*np.log(r) + bv*np.log(shear_velocity_m_sec/va))

    def standard_deviation(self)->np.ndarray:
        return self.df['slnY'].to_numpy()
    
    
    
    
def probability_of_exceedance(site:Site, spectral_accelerations:np.ndarray, magnitudes:np.ndarray, gmm:Ground_Motion_Model):
    probabilities = np.zeros((len(gmm.periods), len(magnitudes),len(spectral_accelerations),len(site.ruptures)))
    for i in range(len(site.ruptures)):
        rup = site.ruptures[i]
        dist = site.rup_dists[i]
        proba = np.zeros((len(gmm.periods), len(magnitudes),len(spectral_accelerations)))
        medians = gmm.median(site.shear_velocity, magnitudes, rup.rup_type, dist).reshape(len(gmm.periods),-1,1)
        stds = gmm.standard_deviation().reshape(len(gmm.periods),1,1)
        probabilities[:,:,:,i] = 1 - norm.cdf(np.log(spectral_accelerations), loc=np.log(medians), scale=0.52)#stds)
    return probabilities




def annual_rate_of_exceedance(site:Site, probability_of_exceedance:np.ndarray, magnitudes:np.ndarray, sum_magnitudes=False, sum_ruptures=False):
    rates = np.zeros(probability_of_exceedance.shape)
    for i in range(len(site.ruptures)):
        rup = site.ruptures[i]
        rates[:,:,:,i] = probability_of_exceedance[:,:,:,i] * rup.magnitude.rate_of_occurrence(rup.annual_activity_rate, magnitudes).reshape(1,-1,1)

    if sum_ruptures:
        rates = np.sum(rates, axis=3)

    if sum_magnitudes:
        rates = np.sum(rates, axis=1)

    return rates