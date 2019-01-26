from main.FileSaver import FileSaver
from main.commentscripter import CommentScripter


def main(url, username):
    saver = FileSaver(username)
    cp = CommentScripter(url)
    cp.get_comment_data()
    saver.save_to_file(cp.comment_data)
