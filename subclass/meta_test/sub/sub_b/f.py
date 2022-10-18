from subclass.meta_test.sub import A


class F(A):
    @classmethod
    def output(cls):
        print('----F----')
