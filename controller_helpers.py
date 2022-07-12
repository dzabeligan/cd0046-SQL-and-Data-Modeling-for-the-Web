from flask import flash


def validate_form(form, table_type):
    if form.state.data and not form.state.validate(form):
        flash('Invalid state provided. ' + table_type +
              ' could not be listed.')
        return False

    if form.phone.data and not form.phone.validate(form):
        flash('Invalid phone number provided. ' +
              table_type + ' could not be listed.')
        return False

    if len(form.genres.data) > 0 and not form.genres.validate(form):
        flash('Invalid gerne selected. ' + table_type +
              ' could not be listed.')
        return False

    if form.facebook_link.data and not form.facebook_link.validate(form):
        flash('Invalid facebook link provided. ' +
              table_type + ' could not be listed.')
        return False

    if form.website_link.data and not form.website_link.validate(form):
        flash('Invalid website provided. ' + table_type +
              ' could not be listed.')
        return False

    return True
