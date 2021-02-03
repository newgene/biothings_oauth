from wtforms import (
    # Field types
    StringField, TextAreaField, SelectField, SelectMultipleField,
    # Other
    Form, validators
)

from auth.models import ClientType, Api, ClientApi


class ApiForm(Form):
    """
    API model form.
    """
    name = StringField(
        'Name', [validators.Length(max=256)], render_kw={"maxlength": 256}
    )
    identifier = StringField(
        'Identifier',
        [validators.Length(max=256), validators.DataRequired()],
        render_kw={"maxlength": 256}
    )
    description = TextAreaField(
        'Description',
        [validators.Length(max=512)],
        render_kw={"maxlength": 512}
    )


class ClientForm(Form):
    """
    Client model form.
    """

    def _set_apis_field_choices(self, db):
        """
        Sets choices for 'apis' field.

        :param db: SqlAlchemy Database session instance.
        """

        self.apis.choices = [
            (api.id, api.name)
            for api in db.query(Api).order_by(Api.name).all()
        ]

    def populate_obj(self, obj):
        """
        Populates an object with form's data.

        :param obj: Object to be populated.
        """

        self.apis.data = [
            ClientApi(client_id=obj.id, api_id=api_id)
            for api_id in self.apis.data
        ]
        return super(ClientForm, self).populate_obj(obj)

    def __init__(self, db, **kwargs):
        super(ClientForm, self).__init__(**kwargs)

        self._set_apis_field_choices(db)
        if "obj" in kwargs:
            self.apis.process_data(
                [client_api.api_id for client_api in kwargs["obj"].apis]
            )

    name = StringField(
        'Name',
        [validators.Length(max=256), validators.DataRequired()],
        render_kw={"maxlength": 256}
    )
    type = SelectField(
        "Type",
        [validators.DataRequired()],
        choices=[(choice.name, choice.value) for choice in ClientType]
    )
    apis = SelectMultipleField(
        "APIs",
        choices=[],  # This is dynamically set in form's creation.
        coerce=int
    )

    # user = todo