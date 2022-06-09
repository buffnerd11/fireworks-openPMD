import numpy as np
import matplotlib.pyplot as plt
from openpmd_viewer import OpenPMDTimeSeries



class ChargeTracker(object):
    """
    An object that helps track the charge that has left the simulation.
    The idea is that this object will 
    (1) get the files with the positions and momenta 
    (and possibly with the E and B to push the momenta 
    before knowing what the positions and momenta are).
    (2) Get ejected charge as a function of theta and energy for each time.
    
    """

    def __init__(self, path_to_dir, ):
        """
        Initializes the ChargeTracker

        Get the openPMD files

        .. note:: 
            Blahblahblah blah 
        
        Parameters
        ----------
        path_to_dir: string
            The path to the directory where the openPMD files are.
        """
        # Create the OpenPMD Time Series object to hopefully access the data
        self.ts = OpenPMDTimeSeries(path_to_dir,check_all_files=False)
        self.data_list = [1]
        
        
    def firstfunction(self):
        """
        Does what it does. 

        Parameters
        ----------
        thing: float
        """
        self.data_list = self.ts.get_particle(plot=False)


    def main(self):
        print("This is main!")
