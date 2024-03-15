import matplotlib.pyplot as plt
import numpy as np

# The very begining of this code is from
#  https://stackoverflow.com/questions/48937397/how-to-sort-a-historical-timeline-written-with-python-matplotlib
event = np.array(['Antiquity', 'Egypt', 'W.R.Empire', 'E.R.Empire', 'Writing', 'C.Colomb', 'Middle Ages'])
begin = np.array([-3400, -3150, 285, 330, -3400, 1492, 476])
end = np.array([476, 30, 476, 1453, -3300, 1493, 1492])


# Correct too short periods : (for example Colomb period is too short compared with other period. Can't be represented.
# Must be represented as a date oa as an enlarged period


def correct_narrow_pediods(begin, end, threshold=15):
    rep_end = []
    for i in range(len(begin)):
        if end[i] - begin[i] > threshold:
            rep_end.append(end[i])
        else:
            rep_end.append(threshold)
    return rep_end


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


end_rep = correct_narrow_pediods(begin, end)

plt.barh(range(len(begin)), end_rep - begin, left=begin, align='center')

plt.yticks(range(len(begin)), event)
plt.xlim(-3500, 2000)

plt.show()
