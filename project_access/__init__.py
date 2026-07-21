from flask import Blueprint

project_bp = Blueprint(
    "project",
    __name__,
    template_folder="../templates"
)

from project_access import routes