from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView, filters
from flask_admin.actions import action
from delivery.ext.db import db
from delivery.ext.db.models import User, Address, Category, Store, Order
from flask import flash, Markup

admin = Admin()

def init_app(app):
    admin.name = "Mr Cheese cake"
    admin.template_mode = "bootstrap2"
    admin.init_app(app)
    
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(ModelView(Address, db.session))
    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Store, db.session))
    admin.add_view(ModelView(Order, db.session))


""" def format_user(self, request, user, *args):
    return user.email.split("@")[0] """

class UserAdmin(ModelView):
    """interface admin de users"""

    #column_formatters = {"email": format_user}
    column_formatters = {
        "email": lambda s, r, u, *a: Markup(f'<b>{u.email.split("@")[0] + "@****"}</b>')
    }

    column_list = ["email", "admin"]

    column_searchable_list = ["email"]

    column_filters = [
        "email",
         "admin",
         filters.FilterLike(
             User.email,
             "Dominio",
             options=(("gmail", "Gmail"), ("uol", "Uol"))
         )
    ]

    can_edit = False
    can_create = True
    can_delete = True

    @action(
        'toggle_admin',
        'Toggle admin status',
        'Are you sure?'
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users: 
            user.admin = not user.admin
        db.session.commit()
        flash(f" {len(users)} usuários alterados com sucesso!", "sucess")

    @action(
        'send_email',
        'Send email to selected users',
        'Are you sure?'
    )
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        # 1) redirect para um form para escrever a mensagem
        # 2) enviar o email
        flash(f" {len(users)} emails enviados com sucesso!", "sucess")