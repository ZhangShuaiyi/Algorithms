import os

class UnionFindTest():
    """docstring for UnionFindTest"""

    cls = None

    def setUp(self):
        print('Using ', self.cls)
        self.data_path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.data_path = os.path.join(self.data_path, 'algs4-data')
        self.datas = [{'uf': 'tinyUF.txt', 'count': 2},
                    {'uf': 'mediumUF.txt', 'count': 3}]

    def test_union_find(self):
        self.assertIsNotNone(self.cls)
        for data in self.datas:
            fileUF = os.path.join(self.data_path, data['uf'])
            print('filename:', fileUF)
            with open(fileUF, 'r') as f:
                n = int(f.readline())
                uf = self.cls(n)
                for line in f.readlines():
                    p, q = [int(x) for x in line.split()]
                    if uf.connected(p, q):
                        continue
                    uf.union(p, q)
            self.assertEqual(uf.get_count(), data['count'])
        
