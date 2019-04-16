from time import time as timmer
import sys
import os
from IPython.display import display, Javascript

def _genStr(it, total, eta, time_it, length_bar=20):
    outstr = str(it)+'/'+str(total)+'  ['
    perc_it = it/total * length_bar

    for i in range(length_bar):
        if i < perc_it:
            outstr = outstr + chr(9608)
        else:
            outstr = outstr + ' '
    outstr = outstr + '] \t\t '

    min_eta = round(eta//60)
    sec_eta = round(eta - 60 * min_eta)

    if min_eta > 0:
        outstr = outstr+'\t eta: '+str(min_eta)+' min \t'+str(sec_eta)+' sec'
    else:
        outstr = outstr+'\t eta: '+str(sec_eta)+' sec'
        
    outstr = outstr+'\t ('+str(round(time_it,6))+' secs/it)'


    outstr = outstr.ljust(100)

    return outstr
    
def _ema(x, mu, alpha=0.8):
    return (alpha * x) + (1 - alpha) * mu

def foo():
    
    js = """

    require(
        ["base/js/dialog"], 
        function(dialog) {
            dialog.modal({
                title: 'Completed !',
                body: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam pretium nulla at nisl hendrerit, sit amet facilisis erat ultrices. Integer ac mauris eget sem egestas tempus sit amet a neque. In nec gravida arcu. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque non velit eu lectus feugiat gravida. Duis vitae dui non quam bibendum bibendum eget eu orci. Sed eget dui sed sapien mattis tempus id in nisl. Duis sagittis lectus ante. Praesent id imperdiet ipsum. Ut nec fermentum ante. Donec nec tortor lorem. Quisque condimentum sapien eget lacus varius, id mattis mauris molestie. Curabitur pharetra feugiat sem, eget faucibus tortor rutrum nec.',
            });
        }
    );

    """

    display(Javascript(js))

class syncedPB():
    def __init__(self, target, file=sys.stderr, popup=False):
        self.__popup = popup
        self.__file = file
        self.__target = target
        self.tick = timmer()
        self.it = 0
        self.time_it = 0
        self.elapsed = timmer()
    
    def __len__(self):
        return len(self.__target)

    def __getitem__(self, i):
        
        if self.it > 0.1*len(self):
            self.time_it = _ema(timmer() - self.tick, self.time_it)
        else:
            self.time_it = _ema(timmer() - self.tick, self.time_it, alpha=1)
            
        eta = int((len(self) - self.it)*self.time_it)
        
        print(_genStr(self.it, len(self), eta, self.time_it), file=self.__file, end='\r')
        self.tick = timmer()
        self.it += 1
        
        if i == len(self)-1 and self.__popup:
            foo()
        
        return self.__target[i]
