import os
import importlib
import inspect


def get_all_files(target_dir):
    files = []
    list_files = os.listdir(target_dir)
    for i in range(0, len(list_files)):
        path = os.path.join(target_dir, list_files[i])
        if os.path.isdir(path):
            files.extend(get_all_files(path))
        elif os.path.isfile(path):
            files.append(path)
    return files


class A:
    @classmethod
    def output(cls):
        print('----A----')

    @classmethod
    def get_subclass(cls, dir_path=None):
        current_path = os.path.dirname(os.path.abspath(__file__))
        # package = current_path.split('/')[-1]
        if dir_path is None:
            dir_path = current_path
        subclasses = []
        files = []
        for file in get_all_files(dir_path):
            if file.endswith('.py'):
                files.append(file.replace(current_path + '/', '').split('.')[0].replace('/', '.'))
        for file in files:
            module = importlib.import_module(file)
            module_info = inspect.getmembers(module)
            for name, subclass in module_info:
                # 判断是否为 class
                if inspect.isclass(subclass):
                    # 判断父类是否为 A
                    if subclass.__base__.__name__ == cls.__name__:
                        if subclass not in subclasses:
                            subclass.output()
                            subclasses.append(subclass)
        return subclasses


if __name__ == '__main__':
    print(A.get_subclass())
