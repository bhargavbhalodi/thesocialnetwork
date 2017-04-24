from server_interface import ServerInterface
import json
import requests
base_url = 'http://nsommer.wooster.edu/social'


class PostMessageInterface(ServerInterface):
    """
    This class uses the ServerInterface class
    to deal with all services that are related
    to posting messages.
    """
    def __init__(self):
        pass

    def post_status(self, uid, content, token):
        """
        This method posts a status that the user has
        :param uid: the integer id of the user
        :param content: the content a user will post
        :param token: unique authentication for the user
        :return: the post id
        """
        response = requests.post(base_url+ '/posts', data={'uid': uid,
                                                           'parentid': -1,
                                                           'content': content,
                                                           'token': token})

        return json.loads(response.text)

    def get_posts(self, limit, tag):
        """

        :param limit:
        :param tag:
        :return:
        """
        response = requests.get(base_url+ '/posts')
        json_info = json.loads(response)

    def edit_post(self, uid, token, post_id, content):
        """
        This method is used to edit a post
        that the user makes.
        :param uid: the integer id of the user
        :param token:  unique authentication for the user
        :param post_id: the integer id of the post
        :param content: the content a user will edit
        :return: ID of the edited post
        """
        response = requests.patch(base_url+ '/posts',data={'uid': uid,
                                                           'token': token,
                                                           'post_id': post_id,
                                                           'content': content})
        return json.loads(response.text)

    def delete_post(self, uid, token, postid):
        """
        This method is used to delete posts
        :param uid: the integer id of the user
        :param token:  unique authentication for the user
        :param postid: the integer id of the post
        :return: ID of the deleted post
        """
        response = requests.delete(base_url+ '/posts', data={'uid': uid,
                                                             'token': token,
                                                             'postid': postid})
        return json.loads(response.text)

    def post_id(self, id):
        pass

    def get_id(self):
        pass

    def send_message(self, to, subject, body):
        pass

    def rate_post(self):
        pass

    def get_message(self, id):
        pass


if __name__ == "__main__":
    user = PostMessageInterface()
    print user.post_status(21, 'Hello!', 'sguwsicp')