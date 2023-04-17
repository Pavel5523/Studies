class Countries:
    @staticmethod
    def add_data(**kwargs):
        with open('file_data.txt', 'w') as f:
            f.write(**kwargs)


a = {'saa': 2}
Countries.add_data(a)
