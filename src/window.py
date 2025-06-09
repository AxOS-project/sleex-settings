# window.py
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

from gi.repository import Adw
from gi.repository import Gtk
import sys
import os
import json

@Gtk.Template(resource_path='/com/axos-project/sleex-settings/window.ui')
class SleexSettingsWindow(Adw.PreferencesWindow):
    __gtype_name__ = 'SleexSettingsWindow'

    # Get script path
    pathname = os.path.dirname(sys.argv[0])

    path_name = pathname # Path of Application
    homeFolder = os.path.expanduser('~') # Path to home folder
    sleex_settings_path = homeFolder + "/.sleex/"

    with open("/usr/share/sleex/modules/.configuration/default_config.json", "r") as f:
        settings = json.load(f)

    def replace_json_field(self, field_root, new_value):
        try:
            with open("/usr/share/sleex/modules/.configuration/default_config.json", 'r+') as file:
                data = json.load(file)
                current = data
                for key in field_root.split('.')[:-1]:
                    current = current[key]
                current[field_root.split('.')[-1]] = new_value
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
            return True
        except Exception as e:
            print(f"Error updating JSON: {e}")
            return False

    timeformats = [
        "%H:%M",
        "%I:%M",
        "%I:%M %p"
    ]

    dateformats = [
        "%Od %b",             # 09 juin
        "%a %Od %b",          # lun. 09 juin
        "%Od %B %Y",          # 09 juin 2025
        "%Y-%Om-%Od",         # 2025-06-09
        "%A %Od",             # lundi 09
        "%b %Od, %Y",         # juin 09, 2025
        "%Od · %b",           # 09 · juin
        "%Odᵉ %B",            # 9ᵉ juin (si rendu possible)
    ]

    timeformat = ""
    dateformat = ""

    # AI settings
    ai_default_gpt_provider = Gtk.Template.Child()
    ai_default_temperature = Gtk.Template.Child()
    ai_enhancements = Gtk.Template.Child()
    ai_use_history = Gtk.Template.Child()
    ai_safety = Gtk.Template.Child()
    
    # Animation settings
    animations_choreography_delay = Gtk.Template.Child()
    animations_duration_small = Gtk.Template.Child()
    animations_duration_large = Gtk.Template.Child()
    
    # Appearance settings
    appearance_auto_dark_mode = Gtk.Template.Child()
    appearance_keyboard_use_flag = Gtk.Template.Child()
    appearance_layer_smoke = Gtk.Template.Child()
    appearance_show_monitor = Gtk.Template.Child()
    appearance_show_time_date = Gtk.Template.Child()
    appearance_show_win_title = Gtk.Template.Child()
    appearance_show_workspace = Gtk.Template.Child()
    
    # Apps settings
    apps_bluetooth = Gtk.Template.Child()
    apps_image_viewer = Gtk.Template.Child()
    apps_network = Gtk.Template.Child()
    apps_settings = Gtk.Template.Child()
    apps_task_manager = Gtk.Template.Child()
    apps_terminal = Gtk.Template.Child()
    
    # Battery settings
    battery_low = Gtk.Template.Child()
    battery_critical = Gtk.Template.Child()
    battery_suspend_threshold = Gtk.Template.Child()
    
    # Overview settings
    overview_scale = Gtk.Template.Child()
    overview_num_of_rows = Gtk.Template.Child()
    overview_num_of_cols = Gtk.Template.Child()
    
    # Search 
    search_enable_actions = Gtk.Template.Child()
    search_enable_commands = Gtk.Template.Child()
    search_enable_maths = Gtk.Template.Child()
    search_enable_directory = Gtk.Template.Child()
    search_enable_ai = Gtk.Template.Child()
    search_enable_web = Gtk.Template.Child()
    search_engine_base_url = Gtk.Template.Child()
    
    # Time settings
    time_format = Gtk.Template.Child()
    time_interval = Gtk.Template.Child()
    time_date_format = Gtk.Template.Child()
    
    # Weather settings
    weather_preferred_unit = Gtk.Template.Child()
    
    # Workspace settings
    workspaces_shown = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_callbacks()

        # Initialize UI elements with values from settings
        self.ai_default_gpt_provider.set_text(self.settings.get('ai', {}).get('defaultGPTProvider', 'openai'))
        self.ai_default_temperature.set_value(self.settings.get('ai', {}).get('defaultTemperature', 0.9))
        self.ai_enhancements.set_active(self.settings.get('ai', {}).get('enhancements', False))
        self.ai_use_history.set_active(self.settings.get('ai', {}).get('useHistory', True))
        self.ai_safety.set_active(self.settings.get('ai', {}).get('safety', True))

        self.animations_choreography_delay.set_value(self.settings.get('animations', {}).get('choreographyDelay', 35))
        self.animations_duration_small.set_value(self.settings.get('animations', {}).get('durationSmall', 110))
        self.animations_duration_large.set_value(self.settings.get('animations', {}).get('durationLarge', 180))

        self.appearance_auto_dark_mode.set_active(self.settings.get('appearance', {}).get('autoDarkMode', {}).get('enabled', False))
        self.appearance_keyboard_use_flag.set_active(self.settings.get('appearance', {}).get('keyboardUseFlag', False))
        self.appearance_layer_smoke.set_active(self.settings.get('appearance', {}).get('layerSmoke', False))
        self.appearance_show_monitor.set_active(self.settings.get('appearance', {}).get('showMonitor', True))
        self.appearance_show_time_date.set_active(self.settings.get('appearance', {}).get('showTimeDate', True))
        self.appearance_show_win_title.set_active(self.settings.get('appearance', {}).get('showWinTitle', True))
        self.appearance_show_workspace.set_active(self.settings.get('appearance', {}).get('showWorkspace', True))

        self.apps_bluetooth.set_text(self.settings.get('apps', {}).get('bluetooth', 'blueberry'))
        self.apps_image_viewer.set_text(self.settings.get('apps', {}).get('imageViewer', 'loupe'))
        self.apps_network.set_text(self.settings.get('apps', {}).get('network', 'sleex-control'))
        self.apps_settings.set_text(self.settings.get('apps', {}).get('settings', 'sleex-control'))
        self.apps_task_manager.set_text(self.settings.get('apps', {}).get('taskManager', 'gnome-usage'))
        self.apps_terminal.set_text(self.settings.get('apps', {}).get('terminal', 'foot'))

        self.battery_low.set_value(self.settings.get('battery', {}).get('low', 20))
        self.battery_critical.set_value(self.settings.get('battery', {}).get('critical', 10))
        self.battery_suspend_threshold.set_value(self.settings.get('battery', {}).get('suspendThreshold', 3))

        self.overview_scale.set_value(self.settings.get('overview', {}).get('scale', 0.18))
        self.overview_num_of_rows.set_value(self.settings.get('overview', {}).get('numOfRows', 2))
        self.overview_num_of_cols.set_value(self.settings.get('overview', {}).get('numOfCols', 5))

        self.search_enable_actions.set_active(self.settings.get('search', {}).get('enableFeatures', {}).get('actions', True))
        self.search_enable_commands.set_active(self.settings.get('search', {}).get('enableFeatures', {}).get('commands', True))
        self.search_enable_maths.set_active(self.settings.get('search', {}).get('enableFeatures', {}).get('mathResults', True))
        self.search_enable_directory.set_active(self.settings.get('search', {}).get('enableFeatures', {}).get('directorySearch', True))
        self.search_enable_ai.set_active(self.settings.get('search', {}).get('enableFeatures', {}).get('aiSearch', True))
        self.search_enable_web.set_active(self.settings.get('search', {}).get('enableFeatures', {}).get('webSearch', True))
        self.search_engine_base_url.set_text(self.settings.get('search', {}).get('engineBaseUrl', 'https://www.google.com/search?q='))

        time_format = self.settings.get('time', {}).get('format', "%H:%M")
        self.time_format.set_selected(self.timeformats.index(time_format) if time_format in self.timeformats else 0)
        
        self.time_interval.set_value(self.settings.get('time', {}).get('interval', 5000))
        
        date_format = self.settings.get('time', {}).get('dateFormat', "%d/%m")
        self.time_date_format.set_selected(self.dateformats.index(date_format) if date_format in self.dateformats else 0)


        unit = self.settings.get('weather', {}).get('preferredUnit', 'C')
        self.weather_preferred_unit.set_selected(0 if unit == 'C' else 1)

        self.workspaces_shown.set_value(self.settings.get('workspaces', {}).get('shown', 10))
        
        
    def setup_callbacks(self):
        # === AI ===
        self.ai_default_gpt_provider.connect("notify::text", self.on_text("ai.defaultGPTProvider"))
        self.ai_default_temperature.connect("notify::value", self.on_spin("ai.defaultTemperature"))
        self.ai_enhancements.connect("notify::active", self.on_toggle("ai.enhancements"))
        self.ai_use_history.connect("notify::active", self.on_toggle("ai.useHistory"))
        self.ai_safety.connect("notify::active", self.on_toggle("ai.safety"))

        # === Animations ===
        self.animations_choreography_delay.connect("notify::value", self.on_spin("animations.choreographyDelay"))
        self.animations_duration_small.connect("notify::value", self.on_spin("animations.durationSmall"))
        self.animations_duration_large.connect("notify::value", self.on_spin("animations.durationLarge"))

        # === Appearance ===
        self.appearance_show_time_date.connect("notify::active", self.on_toggle("appearance.showTimeDate"))
        self.appearance_show_workspace.connect("notify::active", self.on_toggle("appearance.showWorkspace"))
        self.appearance_auto_dark_mode.connect("notify::active", self.on_toggle("appearance.autoDarkMode.enabled"))
        self.appearance_keyboard_use_flag.connect("notify::active", self.on_toggle("appearance.keyboardUseFlag"))
        self.appearance_layer_smoke.connect("notify::active", self.on_toggle("appearance.layerSmoke"))
        self.appearance_show_monitor.connect("notify::active", self.on_toggle("appearance.showMonitor"))
        self.appearance_show_win_title.connect("notify::active", self.on_toggle("appearance.showWinTitle"))

        # === Apps ===
        self.apps_bluetooth.connect("notify::text", self.on_text("apps.bluetooth"))
        self.apps_image_viewer.connect("notify::text", self.on_text("apps.imageViewer"))
        self.apps_network.connect("notify::text", self.on_text("apps.network"))
        self.apps_settings.connect("notify::text", self.on_text("apps.settings"))
        self.apps_task_manager.connect("notify::text", self.on_text("apps.taskManager"))
        self.apps_terminal.connect("notify::text", self.on_text("apps.terminal"))

        # === Battery ===
        self.battery_low.connect("notify::value", self.on_spin("battery.low"))
        self.battery_critical.connect("notify::value", self.on_spin("battery.critical"))
        self.battery_suspend_threshold.connect("notify::value", self.on_spin("battery.suspendThreshold"))

        # === Overview ===
        self.overview_scale.connect("notify::value", self.on_spin("overview.scale"))
        self.overview_num_of_rows.connect("notify::value", self.on_spin("overview.numOfRows"))
        self.overview_num_of_cols.connect("notify::value", self.on_spin("overview.numOfCols"))

        # === Search ===
        self.search_enable_actions.connect("notify::active", self.on_toggle("search.enableFeatures.actions"))
        self.search_enable_commands.connect("notify::active", self.on_toggle("search.enableFeatures.commands"))
        self.search_enable_maths.connect("notify::active", self.on_toggle("search.enableFeatures.mathResults"))
        self.search_enable_directory.connect("notify::active", self.on_toggle("search.enableFeatures.directorySearch"))
        self.search_enable_ai.connect("notify::active", self.on_toggle("search.enableFeatures.aiSearch"))
        self.search_enable_web.connect("notify::active", self.on_toggle("search.enableFeatures.webSearch"))
        self.search_engine_base_url.connect("notify::text", self.on_text("search.engineBaseUrl"))

        # === Time ===
        self.time_interval.connect("notify::value", self.on_spin("time.interval"))
        self.time_format.connect("notify::selected", self.on_combo("time.format", self.timeformats))
        self.time_date_format.connect("notify::selected", self.on_combo("time.dateFormat", self.dateformats))

        # === Weather ===
        self.weather_preferred_unit.connect("notify::selected", self.on_combo_value("weather.preferredUnit", ["C", "F"]))

        # === Workspaces ===
        self.workspaces_shown.connect("notify::value", self.on_spin("workspaces.shown"))

    def update(self, key, value):
        self.replace_json_field(key, value)

    def on_toggle(self, key):
        return lambda widget, _: self.update(key, widget.get_active())

    def on_spin(self, key):
        return lambda spin, _: self.update(key, spin.get_value_as_int())

    def on_combo(self, key, values):
        return lambda combo, _: self.update(key, values[combo.get_selected()])

    def on_combo_value(self, key, value_list):
        return lambda combo, _: self.update(key, value_list[combo.get_selected()])

    def on_text(self, key):
        return lambda entry, _: self.update(key, entry.get_text())
