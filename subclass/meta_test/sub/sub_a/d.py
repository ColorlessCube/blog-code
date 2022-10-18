from subclass.meta_test.sub import A


class D(A):
    @classmethod
    def output(cls):
        print('----D----')
