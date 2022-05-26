class params:

    def __init__(self):
        self._caseno = None
        self._casename = None
        self._testname = None
        self._apipath = None
        self.__params = None
        self._expectresult = None
        self._actualresult = None
        self._requestmethod = None

    @property
    def caseno(self):
        """I'm the 'x' property."""
        return self._caseno

    @caseno.setter
    def caseno(self, value):
        self._caseno = value

    @property
    def casename(self):
        """I'm the 'x' property."""
        return self._casename

    @casename.setter
    def casename(self, value):
        self._casename = value

    @property
    def testname(self):
        """I'm the 'x' property."""
        return self._testname

    @testname.setter
    def testname(self, value):
        self._testname = value

    @property
    def apipath(self):
        """I'm the 'x' property."""
        return self._apipath

    @apipath.setter
    def apipath(self, value):
        self._apipath = value

    @property
    def params(self):
        """I'm the 'x' property."""
        return self._params

    @params.setter
    def params(self, value):
        self._params = value

    @property
    def expectresult(self):
        """I'm the 'x' property."""
        return self._expectresult

    @expectresult.setter
    def expectresult(self, value):
        self._expectresult = value


    @property
    def actualresult(self):
        return self._actualresult

    @actualresult.setter
    def actualresult(self, value):
        self._actualresult = value

    @property
    def requestmethod(self):
        return self._requestmethod

    @requestmethod.setter
    def requestmethod(self, value):
        self._requestmethod = value

