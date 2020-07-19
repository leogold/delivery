""" from flask_admin.contrib.sqla import ModelView

def format_user(self, request, user, *args):
    return user.email.split("@")[0]

class UserAdmin(ModelView):
    """interface admin de users"""

    column_formatters = {"email": format_user}

    column_list = ["email", "admin"]

    can_edit = False
    can_create = True
    can_delete = True """
