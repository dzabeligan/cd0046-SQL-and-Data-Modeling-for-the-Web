from wtforms.validators import ValidationError


class AnyOfInList:
    """
    Compares the incoming data of type 'list' to a sequence of valid inputs.

    :param values:
        A sequence of valid inputs.
    :param message:
        Error message to raise in case of a validation error. `%(values)s`
        contains the list of values.
    :param values_formatter:
        Function used to format the list of values in the error message.
    """

    def __init__(self, values, message=None, values_formatter=None):
        self.values = values
        self.message = message
        if values_formatter is None:
            values_formatter = self.default_values_formatter
        self.values_formatter = values_formatter

    def __call__(self, form, field):
        message = self.message
        for data in field.data:
            if data not in self.values:
                raise ValidationError(
                    "Invalid value, must be one of: %(values)s.")

        if message is None:
            message = field.gettext(
                "Invalid value, must be one of: %(values)s.")

        return

    @staticmethod
    def default_values_formatter(values):
        return ", ".join(str(x) for x in values)
