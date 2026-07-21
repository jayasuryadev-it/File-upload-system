import os
import socket
import platform
from flask import render_template

from . import project_bp


@project_bp.route("/projects")
def projects():

    server_name = socket.gethostname()
    server_ip = socket.gethostbyname(server_name)

    project_path = os.path.abspath(os.getcwd())

    return render_template(
        "project_access.html",
        server_name=server_name,
        server_ip=server_ip,
        project_path=project_path,
        python_version=platform.python_version()
    )