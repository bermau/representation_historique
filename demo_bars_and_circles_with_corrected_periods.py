import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
OUTPUT_REP = r"./produced_images"

# The very begining of this code is from
#  https://stackoverflow.com/questions/48937397/how-to-sort-a-historical-timeline-written-with-python-matplotlib


# Correct too short periods : (In the following example Colomb period is too short compared with other periods.
# It can't be represented directly and must be represented as a date of as an enlarged period
def correct_narrow_periods(begin, end, threshold=15):
    rep_end = []
    for i in range(len(begin)):
        if end[i] - begin[i] > threshold:
            rep_end.append(end[i])
        else:
            rep_end.append(threshold)
    return rep_end

def histo_scatter(fig, ax, years, datas, names=None,  factor = 10000, text_shift= None, **kwargs):
    height = 1
    i = 0
    datas_unit = 1000000
    # factor = 1000000
    path_collection_lst = []
    for (year, data) in zip(years, datas):
        path_collection_lst.append(plt.scatter(year, height, s = data/factor, alpha = 0.5))
        if names.any():
            # Force the position of a label. The label is designated by its index or its event name.
            force_position = text_shift.get(i, 0) + text_shift.get(names[i], 0)
            if force_position :
                hauteur = height * (1 + force_position)
            else:
                hauteur = height * 1.1
            plt.text(year, hauteur, names[i])
        plt.text(year, hauteur*0.9, str(data/datas_unit))
        i += 1
    ymax = kwargs.get('year_max', max(years) * 1.1)
    plt.xlim(0, ymax)
    plt.ylim(0, height *2 )
    return path_collection_lst

def demo_circles():

    epi_df = pd.read_csv('data_epidemie.csv')
    fig,ax = plt.subplots(1, figsize= (13,5))
    # Shift for text : points are designated by their index or their event name
    decalages = { 2 : -0.2, 3:+0.1, "Peste noire":-0.3, 5:0.3, 6:-0.2}
    AA = histo_scatter(fig,ax, epi_df.year, epi_df.deaths, names = epi_df.event,
                  factor=20000,  text_shift=decalages
                  # , year_max = 1800
                 )
    ax.set_title("Grandes épidémies\n (million de morts)")
    ax.set_yticks([])  # no y labels
    plt.savefig(os.path.join(OUTPUT_REP,"mortalis.svg"))

def demo_historic_graph_1(begin, end):
    end_rep = correct_narrow_periods(begin, end)
    plt.barh(range(len(begin)), end_rep-begin, left=begin, align='center')
    plt.yticks(range(len(begin)), event)
    plt.xlim(-3500, 2000)


class Paleo_period():
    """A class to manage paleontological times"""

    def __init__(self, name, begin, end=None, description=None, image=None, classif_lst=[]):
        self.name = name
        self.description = description
        self._begin = begin
        self._end = end
        self._image = image
        self.classif_lst = classif_lst

    @property
    def begin(self):
        return self._begin

    @property
    def end(self):
        return self._end

    @property
    def image(self):
        return self._image


if __name__ == '__main__':
    event = np.array(['Antiquity', 'Egypt', 'W.R.Empire', 'E.R.Empire', 'Writing', 'C.Colomb', 'Middle Ages'])
    begin = np.array([-3400, -3150, 285, 330, -3400, 1492, 476])
    end = np.array([476, 30, 476, 1453, -3300, 1493, 1492])
    demo_historic_graph_1(begin, end)

    plt.show()
    demo_circles()
    plt.savefig(os.path.join(OUTPUT_REP,"periods.svg"))
