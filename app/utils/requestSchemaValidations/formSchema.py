from marshmallow import Schema, fields

class FormSchema(Schema):
    name = fields.String(required=True)
    location = fields.String(required=True)
    phone = fields.Number(required=True)

# class ExtendedSchema(BaseSchema):
#     # have a look at the examples in the Marshmallow docs for more complex data structures, such as nested fields.
#     IL6 = fields.String()
#     PCT = fields.String()
#     CRP = fields.String()