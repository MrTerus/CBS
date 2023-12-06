from django.core.serializers.json import DjangoJSONEncoder
from CBS_manage.models import User


class UserEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {"name": obj.first_name, "age": obj.last_name}
            # return obj.__dict__
        return super().default(obj)