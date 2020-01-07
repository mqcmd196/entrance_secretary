from servomotor import Servomotor

class Autokey:
    """
    Expected to use sg92r, 13Croom
    """
    def __init__(self, port=23, state='neutral'):
        self._sg92r = Servomotor(port)
        self.state = state

    def open(self):
        self._sg92r.changedegree(90)
        self.state = 'opened'

    def lock(self):
        self._sg92r.changedegree(-90)
        self.state = 'locked'

    def neutral(self):
        self._sg92r.changedegree(0)
        self.state = 'neutral'