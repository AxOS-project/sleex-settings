# Sleex Settings

Sleex Settings is a simple GTK4/Libadwaita application for configuring the Sleex environment. It provides a graphical interface to adjust various system, appearance, AI, and workspace settings for Sleex.

## Features
- Configure AI provider and behavior
- Adjust animation timings
- Change appearance options (dark mode, workspace, monitor, etc.)
- Set default applications for common tasks
- Manage battery thresholds
- Customize overview layout
- Enable/disable search features
- Set time and date formats
- Choose weather units
- Configure number of workspaces

> [!IMPORTANT]
> Sleex settings is currently under developement, there is no package yet

## Build and Install
To build and install Sleex Settings, run:
```sh
meson setup build
ninja -C build
sudo ninja -C build install
```

## TODO

- [] Make a proper icon
- [] More options
- [] Stability test

# License

This project is licensed under the GPL-3.0-or-later. See the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) for details.