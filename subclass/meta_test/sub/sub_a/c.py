from subclass.meta_test.sub import A


class C(A):
    @classmethod
    def output(cls):
        print('----C----')
