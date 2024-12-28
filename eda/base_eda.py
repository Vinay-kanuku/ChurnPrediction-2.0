from abc import ABC, abstractmethod
import pandas as pd 
import numpy as np
import logging
from typing import Tuple
from typing_extensions import Annotated

class BaseEDA(ABC):
    """ This class is an abstract class for EDA"""
    @abstractmethod
    def load_data(self, path:str) -> pd.DataFrame:
        """
        This method is used to load the data
        args: path: str
        returns: pd.DataFrame
        """
        pass

    @abstractmethod
    def analyse(self, df:pd.DataFrame) -> None:
        """
        This method is used to analyse the data 
        args: df: pd.DataFrame
        returns: None
        """
    @abstractmethod
    def visualize(self, df:pd.DataFrame) -> None:
        """
        This method is used to visualize the data
        args: df: pd.DataFrame
        returns: None
        """
        pass

