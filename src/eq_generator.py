import matplotlib.pyplot as plt

class MediumEq():
    
    def __init__(self, dpi=192, width=1400, height=100):
        
        self.dpi = dpi
        self.width = width
        self.height = height
        
    def __call__(self, eq: str, fontsize=16, **kwargs):
        
        figsize = (self.width/self.dpi, self.height/self.dpi)
        
        fig = plt.figure(figsize=figsize, dpi=self.dpi)
        ax = fig.add_subplot()
        ax.axis('off')
        ax.annotate(eq, 
                    xy=(0.5,0.5), 
                    fontsize=fontsize, 
                    xycoords='axes fraction',
                    ha='center', 
                    va='center', 
                    usetex=True,
                    **kwargs)
            
        return fig, ax
