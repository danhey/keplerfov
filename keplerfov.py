# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def keplerfov(ax=None, season='spring', xlabel='RA',
             ylabel='Dec', title=None,
             fill=False, grid=False, **kwargs):
    """ 
    Args:
        ax : `matplotlib.axes` object to plot onto.
            generated if none are supplied
        season: summer, autumn, winter, fall
        
    Returns:
        `matplotlib.axes` object
    """

    df2 = pd.read_csv('data/morc_2_ra_dec_4_seasons.csv')

    if ax is None:
        fig, ax = plt.subplots(figsize=[5,5])
    if ('color' not in kwargs) and (len(ax.lines) == 0):
        kwargs['color'] = 'blue'    
    for module in range(1,25):
        for channel in range(1,5):
            corner = df2[(df2['output']==channel) & (df2['module']==module)]
            ra = corner[season+'_ra'].values
            dec = corner[season+'_dec'].values
            if len(ra)>1:
                ra_corner = [ra[0],ra[1],ra[4],ra[3],ra[0]]
                dec_corner = [dec[0],dec[1],dec[4],dec[3],dec[0]]
                ax.plot(ra_corner, dec_corner, c=kwargs['color'], linewidth=0.5)
    
    if title is not None:
        ax.set_title(title)
    ax.grid(grid, alpha=0.3)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.invert_xaxis()
    
    return ax