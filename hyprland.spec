Name:           hyprland
Version:        0.54.2
Release:        1%{?dist}
Summary:        A highly customizable dynamic tiling Wayland compositor

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/Hyprland
# We will use a locally generated tarball that includes the wlroots submodule
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  libxcb-devel
BuildRequires:  libX11-devel
BuildRequires:  pixman-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel
# gdb is a runtime preference for debugging, but not strictly needed for building the package.
# gemini-3.1-pro cooked this , not me , i'm too lazy.
%description
Hyprland is a dynamic tiling Wayland compositor that doesn't sacrifice on its looks.
This package is built with the required wlroots subprojects included.

%prep
# Extract the tarball
%autosetup -n Hyprland

%build
# The %meson macro replaces: meson _build
%meson

# The %meson_build macro replaces: ninja -C _build
%meson_build

%install
# The %meson_install macro replaces: sudo ninja -C _build install
# It safely installs to a temporary buildroot instead of your actual system
%meson_install

%files
# This section lists what files actually go into the RPM. 
# You may need to adjust this based on what the meson install actually outputs.
%license LICENSE
%{_bindir}/Hyprland
%{_bindir}/hyprctl
%{_datadir}/wayland-sessions/hyprland.desktop
%{_datadir}/hyprland/
# Catch any other binary or shared data
%{_bindir}/*
%{_datadir}/*

