class FileSaver:
    def __init__(self, username):
        self.__prefix_file_name = username

    def save_to_file(self, comment_data):
        with open("{0}_comments.txt".format(self.__prefix_file_name), 'w', encoding='utf-8') as f:
            for data in comment_data:
                f.write("{0} {1}: {2}  \r\n".format(data.vote, data.date, data.value))
