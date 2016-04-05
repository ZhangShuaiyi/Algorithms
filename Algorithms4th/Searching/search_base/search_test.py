import os


class SearchTest():
    """docstring for SearchTest"""

    cls = None

    def setUp(self):
        self.data_path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.data_path = os.path.join(self.data_path, 'algs4-data')

        self.datas = [{'input': 'tinyTale.txt',
                       'tests': [{'key': 'it', 'num': 10},
                                 {'key': 'the', 'num': 10}]},
                      {'input': 'tale.txt',
                       'tests': [{'key': 'business', 'num': 122},
                                 {'key': 'defarge', 'num': 280}]}]

    def test_search(self):
        self.assertIsNotNone(self.cls)
        st = self.cls()
        for data in self.datas:
            input = os.path.join(self.data_path, data['input'])
            print(input)
            with open(input, 'r') as f:
                for line in f.readlines():
                    for word in line.split():
                        val = st.get(word)
                        if val is None:
                            st.put(word, 1)
                        else:
                            st.put(word, val + 1)
            for test in data['tests']:
                self.assertEqual(st.get(test['key']), test['num'])
