# main.py
#
# Copyright 2025 Ardox
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi
import subprocess
import os
import threading
import json
import pathlib
import shutil
import shlex
import time

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import SleexSettingsWindow

# Get script path
pathname = os.path.dirname(sys.argv[0])

#The main application singleton class.
class SleexSettingsApplication(Adw.Application):

    path_name = pathname # Path of Application
    homeFolder = os.path.expanduser('~') # Path to home folder
    sleex_config_dir = homeFolder + "/.sleex/"
    config_file = "/usr/share/sleex/modules/.configuration/default_config.json"

    def __init__(self):
        super().__init__(application_id='com.axos-project.sleex-settings',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS)
        self.create_action('quit', lambda *_: self.quit(), ['<primary>q'])
        self.create_action('about', self.on_about_action)
        
            
    # Called when the application is activated.
    def do_activate(self):
        self.win = self.props.active_window
        if not self.win:
            self.win = SleexSettingsWindow(application=self)


        self.win.present()

    # Callback for the app.about action.
    def on_about_action(self, *args):
        about = Adw.AboutDialog(
            application_name="Sleex Settings App",
            developer_name="Ardox",
            version="0.1.0",
            website="https://github.com/axos-project/",
            issue_url="https://github.com/axos-project/",
            support_url="https://github.com/axos-project/",
            copyright="© 2025 Ardox",
            license_type=Gtk.License.GPL_3_0_ONLY
        )
        about.present(self.props.active_window)

    # Add an application action.
    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)

# The application's entry point.
def main(version):
    app = SleexSettingsApplication()
    return app.run(sys.argv)
