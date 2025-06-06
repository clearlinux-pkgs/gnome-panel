#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v25
# autospec commit: 9594167
#
Name     : gnome-panel
Version  : 3.56.0
Release  : 97
URL      : https://download.gnome.org/sources/gnome-panel/3.56/gnome-panel-3.56.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-panel/3.56/gnome-panel-3.56.0.tar.xz
Summary  : libgnome-panel
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gnome-panel-bin = %{version}-%{release}
Requires: gnome-panel-data = %{version}-%{release}
Requires: gnome-panel-lib = %{version}-%{release}
Requires: gnome-panel-license = %{version}-%{release}
Requires: gnome-panel-locales = %{version}-%{release}
Requires: gnome-panel-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-xlib)
BuildRequires : pkgconfig(dconf)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gdm)
BuildRequires : pkgconfig(geocode-glib-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gweather4)
BuildRequires : pkgconfig(libecal-2.0)
BuildRequires : pkgconfig(libedataserver-1.2)
BuildRequires : pkgconfig(libgnome-menu-3.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libwnck-3.0)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xrandr)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# About
This repository contains the GNOME Panel of the GNOME Flashback project. It consists of the `gnome-panel` binary,
the `libpanel-applet` library and several applets.

%package bin
Summary: bin components for the gnome-panel package.
Group: Binaries
Requires: gnome-panel-data = %{version}-%{release}
Requires: gnome-panel-license = %{version}-%{release}

%description bin
bin components for the gnome-panel package.


%package data
Summary: data components for the gnome-panel package.
Group: Data

%description data
data components for the gnome-panel package.


%package dev
Summary: dev components for the gnome-panel package.
Group: Development
Requires: gnome-panel-lib = %{version}-%{release}
Requires: gnome-panel-bin = %{version}-%{release}
Requires: gnome-panel-data = %{version}-%{release}
Provides: gnome-panel-devel = %{version}-%{release}
Requires: gnome-panel = %{version}-%{release}

%description dev
dev components for the gnome-panel package.


%package doc
Summary: doc components for the gnome-panel package.
Group: Documentation
Requires: gnome-panel-man = %{version}-%{release}

%description doc
doc components for the gnome-panel package.


%package lib
Summary: lib components for the gnome-panel package.
Group: Libraries
Requires: gnome-panel-data = %{version}-%{release}
Requires: gnome-panel-license = %{version}-%{release}

%description lib
lib components for the gnome-panel package.


%package license
Summary: license components for the gnome-panel package.
Group: Default

%description license
license components for the gnome-panel package.


%package locales
Summary: locales components for the gnome-panel package.
Group: Default

%description locales
locales components for the gnome-panel package.


%package man
Summary: man components for the gnome-panel package.
Group: Default

%description man
man components for the gnome-panel package.


%prep
%setup -q -n gnome-panel-3.56.0
cd %{_builddir}/gnome-panel-3.56.0
pushd ..
cp -a gnome-panel-3.56.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1745854167
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1745854167
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-panel
cp %{_builddir}/gnome-panel-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-panel/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/gnome-panel-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/gnome-panel/3704f4680301a60004b20f94e0b5b8c7ff1484a9 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang gnome-panel
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gnome-panel
/usr/bin/gnome-panel

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-panel.desktop
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.clock.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.fish.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.initial-settings.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.launcher.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.menu-button.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.window-list.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.workspace-switcher.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.object.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.toplevel.gschema.xml
/usr/share/gnome-panel/fish/fishanim.fish
/usr/share/gnome-panel/fish/fishanim.png
/usr/share/gnome-panel/fish/footguy.fish
/usr/share/gnome-panel/fish/footguy.png
/usr/share/gnome-panel/fish/monkey.fish
/usr/share/gnome-panel/fish/monkey.png
/usr/share/gnome-panel/fish/oldwanda.fish
/usr/share/gnome-panel/fish/oldwanda.png
/usr/share/gnome-panel/fish/wanda.fish
/usr/share/gnome-panel/fish/wanda.png
/usr/share/gnome-panel/layouts/default.layout
/usr/share/icons/hicolor/16x16/apps/gnome-panel-clock.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel-fish.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel-force-quit.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel-hibernate.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel-launcher.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel-notification-area.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel-separator.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel-suspend.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel-window-list.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel-window-menu.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel-workspace-switcher.png
/usr/share/icons/hicolor/16x16/apps/gnome-panel.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-clock.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-fish.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-force-quit.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-hibernate.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-launcher.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-notification-area.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-separator.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-suspend.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-window-list.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-window-menu.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel-workspace-switcher.png
/usr/share/icons/hicolor/22x22/apps/gnome-panel.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-clock.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-fish.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-force-quit.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-hibernate.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-launcher.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-notification-area.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-separator.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-suspend.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-window-list.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-window-menu.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel-workspace-switcher.png
/usr/share/icons/hicolor/24x24/apps/gnome-panel.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-clock.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-fish.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-force-quit.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-hibernate.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-launcher.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-notification-area.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-separator.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-suspend.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-window-list.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-window-menu.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel-workspace-switcher.png
/usr/share/icons/hicolor/32x32/apps/gnome-panel.png
/usr/share/icons/hicolor/48x48/apps/gnome-panel-hibernate.png
/usr/share/icons/hicolor/48x48/apps/gnome-panel-suspend.png
/usr/share/icons/hicolor/48x48/apps/gnome-panel.png
/usr/share/icons/hicolor/scalable/apps/gnome-panel-clock.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel-fish.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel-force-quit.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel-hibernate.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel-launcher.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel-notification-area.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel-separator.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel-suspend.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel-window-list.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel-window-menu.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel-workspace-switcher.svg
/usr/share/icons/hicolor/scalable/apps/gnome-panel.svg

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-panel/libgnome-panel/gp-action.h
/usr/include/gnome-panel/libgnome-panel/gp-applet-info.h
/usr/include/gnome-panel/libgnome-panel/gp-applet.h
/usr/include/gnome-panel/libgnome-panel/gp-enum-types.h
/usr/include/gnome-panel/libgnome-panel/gp-image-menu-item.h
/usr/include/gnome-panel/libgnome-panel/gp-initial-setup-dialog.h
/usr/include/gnome-panel/libgnome-panel/gp-lockdown.h
/usr/include/gnome-panel/libgnome-panel/gp-macros.h
/usr/include/gnome-panel/libgnome-panel/gp-module.h
/usr/include/gnome-panel/libgnome-panel/gp-utils.h
/usr/lib64/libgnome-panel.so
/usr/lib64/pkgconfig/libgnome-panel.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/clock/figures/clock_applet.png
/usr/share/help/C/clock/index.docbook
/usr/share/help/C/clock/legal.xml
/usr/share/help/C/fish/figures/fish_applet.png
/usr/share/help/C/fish/index.docbook
/usr/share/help/C/fish/legal.xml
/usr/share/help/ar/clock/figures/clock_applet.png
/usr/share/help/ar/clock/index.docbook
/usr/share/help/ar/clock/legal.xml
/usr/share/help/ca/clock/figures/clock_applet.png
/usr/share/help/ca/clock/index.docbook
/usr/share/help/ca/clock/legal.xml
/usr/share/help/ca/fish/figures/fish_applet.png
/usr/share/help/ca/fish/index.docbook
/usr/share/help/ca/fish/legal.xml
/usr/share/help/cs/clock/figures/clock_applet.png
/usr/share/help/cs/clock/index.docbook
/usr/share/help/cs/clock/legal.xml
/usr/share/help/cs/fish/figures/fish_applet.png
/usr/share/help/cs/fish/index.docbook
/usr/share/help/cs/fish/legal.xml
/usr/share/help/da/clock/figures/clock_applet.png
/usr/share/help/da/clock/index.docbook
/usr/share/help/da/clock/legal.xml
/usr/share/help/da/fish/figures/fish_applet.png
/usr/share/help/da/fish/index.docbook
/usr/share/help/da/fish/legal.xml
/usr/share/help/de/clock/figures/clock_applet.png
/usr/share/help/de/clock/index.docbook
/usr/share/help/de/clock/legal.xml
/usr/share/help/de/fish/figures/fish_applet.png
/usr/share/help/de/fish/index.docbook
/usr/share/help/de/fish/legal.xml
/usr/share/help/el/clock/figures/clock_applet.png
/usr/share/help/el/clock/index.docbook
/usr/share/help/el/clock/legal.xml
/usr/share/help/el/fish/figures/fish_applet.png
/usr/share/help/el/fish/index.docbook
/usr/share/help/el/fish/legal.xml
/usr/share/help/en_GB/clock/figures/clock_applet.png
/usr/share/help/en_GB/clock/index.docbook
/usr/share/help/en_GB/clock/legal.xml
/usr/share/help/en_GB/fish/figures/fish_applet.png
/usr/share/help/en_GB/fish/index.docbook
/usr/share/help/en_GB/fish/legal.xml
/usr/share/help/es/clock/figures/clock_applet.png
/usr/share/help/es/clock/index.docbook
/usr/share/help/es/clock/legal.xml
/usr/share/help/es/fish/figures/fish_applet.png
/usr/share/help/es/fish/index.docbook
/usr/share/help/es/fish/legal.xml
/usr/share/help/eu/clock/figures/clock_applet.png
/usr/share/help/eu/clock/index.docbook
/usr/share/help/eu/clock/legal.xml
/usr/share/help/eu/fish/figures/fish_applet.png
/usr/share/help/eu/fish/index.docbook
/usr/share/help/eu/fish/legal.xml
/usr/share/help/fi/clock/figures/clock_applet.png
/usr/share/help/fi/clock/index.docbook
/usr/share/help/fi/clock/legal.xml
/usr/share/help/fi/fish/figures/fish_applet.png
/usr/share/help/fi/fish/index.docbook
/usr/share/help/fi/fish/legal.xml
/usr/share/help/fr/clock/figures/clock_applet.png
/usr/share/help/fr/clock/index.docbook
/usr/share/help/fr/clock/legal.xml
/usr/share/help/fr/fish/figures/fish_applet.png
/usr/share/help/fr/fish/index.docbook
/usr/share/help/fr/fish/legal.xml
/usr/share/help/hu/clock/figures/clock_applet.png
/usr/share/help/hu/clock/index.docbook
/usr/share/help/hu/clock/legal.xml
/usr/share/help/hu/fish/figures/fish_applet.png
/usr/share/help/hu/fish/index.docbook
/usr/share/help/hu/fish/legal.xml
/usr/share/help/id/clock/figures/clock_applet.png
/usr/share/help/id/clock/index.docbook
/usr/share/help/id/clock/legal.xml
/usr/share/help/it/clock/figures/clock_applet.png
/usr/share/help/it/clock/index.docbook
/usr/share/help/it/clock/legal.xml
/usr/share/help/it/fish/figures/fish_applet.png
/usr/share/help/it/fish/index.docbook
/usr/share/help/it/fish/legal.xml
/usr/share/help/ja/clock/figures/clock_applet.png
/usr/share/help/ja/clock/index.docbook
/usr/share/help/ja/clock/legal.xml
/usr/share/help/ja/fish/figures/fish_applet.png
/usr/share/help/ja/fish/index.docbook
/usr/share/help/ja/fish/legal.xml
/usr/share/help/ko/clock/figures/clock_applet.png
/usr/share/help/ko/clock/index.docbook
/usr/share/help/ko/clock/legal.xml
/usr/share/help/ko/fish/figures/fish_applet.png
/usr/share/help/ko/fish/index.docbook
/usr/share/help/ko/fish/legal.xml
/usr/share/help/nl/clock/figures/clock_applet.png
/usr/share/help/nl/clock/index.docbook
/usr/share/help/nl/clock/legal.xml
/usr/share/help/oc/clock/figures/clock_applet.png
/usr/share/help/oc/clock/index.docbook
/usr/share/help/oc/clock/legal.xml
/usr/share/help/oc/fish/figures/fish_applet.png
/usr/share/help/oc/fish/index.docbook
/usr/share/help/oc/fish/legal.xml
/usr/share/help/pa/clock/figures/clock_applet.png
/usr/share/help/pa/clock/index.docbook
/usr/share/help/pa/clock/legal.xml
/usr/share/help/pt/clock/figures/clock_applet.png
/usr/share/help/pt/clock/index.docbook
/usr/share/help/pt/clock/legal.xml
/usr/share/help/pt_BR/clock/figures/clock_applet.png
/usr/share/help/pt_BR/clock/index.docbook
/usr/share/help/pt_BR/clock/legal.xml
/usr/share/help/pt_BR/fish/figures/fish_applet.png
/usr/share/help/pt_BR/fish/index.docbook
/usr/share/help/pt_BR/fish/legal.xml
/usr/share/help/ru/clock/figures/clock_applet.png
/usr/share/help/ru/clock/index.docbook
/usr/share/help/ru/clock/legal.xml
/usr/share/help/ru/fish/figures/fish_applet.png
/usr/share/help/ru/fish/index.docbook
/usr/share/help/ru/fish/legal.xml
/usr/share/help/sl/clock/figures/clock_applet.png
/usr/share/help/sl/clock/index.docbook
/usr/share/help/sl/clock/legal.xml
/usr/share/help/sl/fish/figures/fish_applet.png
/usr/share/help/sl/fish/index.docbook
/usr/share/help/sl/fish/legal.xml
/usr/share/help/sr/clock/figures/clock_applet.png
/usr/share/help/sr/clock/index.docbook
/usr/share/help/sr/clock/legal.xml
/usr/share/help/sv/clock/figures/clock_applet.png
/usr/share/help/sv/clock/index.docbook
/usr/share/help/sv/clock/legal.xml
/usr/share/help/sv/fish/figures/fish_applet.png
/usr/share/help/sv/fish/index.docbook
/usr/share/help/sv/fish/legal.xml
/usr/share/help/te/clock/figures/clock_applet.png
/usr/share/help/te/clock/index.docbook
/usr/share/help/te/clock/legal.xml
/usr/share/help/th/clock/figures/clock_applet.png
/usr/share/help/th/clock/index.docbook
/usr/share/help/th/clock/legal.xml
/usr/share/help/th/fish/figures/fish_applet.png
/usr/share/help/th/fish/index.docbook
/usr/share/help/th/fish/legal.xml
/usr/share/help/uk/clock/figures/clock_applet.png
/usr/share/help/uk/clock/index.docbook
/usr/share/help/uk/clock/legal.xml
/usr/share/help/uk/fish/figures/fish_applet.png
/usr/share/help/uk/fish/index.docbook
/usr/share/help/uk/fish/legal.xml
/usr/share/help/zh_CN/clock/figures/clock_applet.png
/usr/share/help/zh_CN/clock/index.docbook
/usr/share/help/zh_CN/clock/legal.xml
/usr/share/help/zh_CN/fish/figures/fish_applet.png
/usr/share/help/zh_CN/fish/index.docbook
/usr/share/help/zh_CN/fish/legal.xml
/usr/share/help/zh_HK/clock/figures/clock_applet.png
/usr/share/help/zh_HK/clock/index.docbook
/usr/share/help/zh_HK/clock/legal.xml
/usr/share/help/zh_TW/clock/figures/clock_applet.png
/usr/share/help/zh_TW/clock/index.docbook
/usr/share/help/zh_TW/clock/legal.xml

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.action-button.so
/V3/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.clock.so
/V3/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.fish.so
/V3/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.launcher.so
/V3/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.menu.so
/V3/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.notification-area.so
/V3/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.separator.so
/V3/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.status-notifier.so
/V3/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.wncklet.so
/V3/usr/lib64/libgnome-panel.so.3.0.0
/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.action-button.so
/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.clock.so
/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.fish.so
/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.launcher.so
/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.menu.so
/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.notification-area.so
/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.separator.so
/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.status-notifier.so
/usr/lib64/gnome-panel/modules/org.gnome.gnome-panel.wncklet.so
/usr/lib64/libgnome-panel.so.3
/usr/lib64/libgnome-panel.so.3.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-panel/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/gnome-panel/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-panel.1

%files locales -f gnome-panel.lang
%defattr(-,root,root,-)

