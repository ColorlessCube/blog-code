from subclass.meta_test.sub import A


class E(A):
    @classmethod
    def output(cls):
        print('----E----')
