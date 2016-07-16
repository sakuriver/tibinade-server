from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView, SingleObjectTemplateResponseMixin
from .models import GameServerSetting

class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class GameApiView(JSONResponseMixin, SingleObjectTemplateResponseMixin, BaseDetailView):
    """
    ゲームAPI用
    """
    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        setting = GameServerSetting.get_view_status()
        result = {'STATUS': setting, 'result': context}
        return result


class AdminApiView(JSONResponseMixin, SingleObjectTemplateResponseMixin, BaseDetailView):
    """
    管理ツールAPI用
    """
    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        setting = GameServerSetting.get_view_status()
        result = {'STATUS': setting, 'result': context}
        return result
