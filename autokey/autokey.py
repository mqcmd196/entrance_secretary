try:
    from servomotor import Servomotor
except RuntimeError:
    pass

class Autokey:
    """
    Expected to use sg92r, 13Croom
    """
    def __init__(self, port=23, state='neutral'):
        try:
            self._sg92r = Servomotor(port)
        except NameError:
            pass
        self.state = state

    def open(self):
        try:
            self._sg92r.changedegree(90)
        except:
            pass
        self.state = 'unlocked'

    def lock(self):
        try:
            self._sg92r.changedegree(-90)
        except:
            pass
        self.state = 'locked'

    def neutral(self):
        try:
            self._sg92r.changedegree(0)
        except:
            pass
        self.state = 'neutral'