import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main.model import user, blacklist, picture, gallery
from app.main import create_app, db

app = create_app(os.getenv("BOILERPLATE_ENV") or "dev")
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)


@manager.command
def run():
    app.run()


if __name__ == "__main__":
    manager.run()
