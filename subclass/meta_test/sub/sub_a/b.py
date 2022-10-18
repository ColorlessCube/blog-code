from subclass.meta_test.sub import A


class B(A):
    @classmethod
    def output(cls):
        print('----B----')
