import json

from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnDict


class CustomRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response', None)

        if response is not None and response.status_code >= 400:
            if isinstance(data, (ReturnDict, dict)):
                for k in data:
                    if not type(data[k]) is list:
                        data[k] = [data[k]]
            data = {"errors": data}
            return json.dumps(data)

        return super(CustomRenderer, self).render(data, accepted_media_type=accepted_media_type,
                                                  renderer_context=renderer_context)
