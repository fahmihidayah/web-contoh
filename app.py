def cetak(*args):
    for item in args:
        print(item)


def cetak_lain(**kwargs):
    for key in kwargs.keys():
        print('key ' + key + ' value ' + kwargs[key])


test = {'nama':'fahmi'}


cetak('fahmi', 'budi')


cetak_lain(nama='fahmi', nama_lain='fahmi lain')