from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

# https://pythonhosted.org/Flask-Inputs/#module-flask_inputs
# https://json-schema.org/understanding-json-schema/
user_schema = {
    'type': 'object',
    'properties': {
        'username': {
            'type': 'string',
        },
        'firstName': {
            'type': 'string',
        },
        'lastName': {
            'type': 'string',
        },
        'email': {
            'type': 'string',
        },
        'phone': {
            'type': 'string',
        }
    },
    'required': ['username', 'firstName', 'lastName', 'email', 'phone']
}


class UserInputs(Inputs):
    json = [JsonSchema(schema=user_schema)]


def validate_user(request):
    inputs = UserInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors
