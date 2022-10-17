from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test for seeing api views"""
    def get(self, request, format=None):
        """return some things """
        return Response("yay you have done what you use to do before")