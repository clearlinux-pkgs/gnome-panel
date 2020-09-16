#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-panel
Version  : 3.36.2
Release  : 28
URL      : https://download.gnome.org/sources/gnome-panel/3.36/gnome-panel-3.36.2.tar.xz
Source0  : https://download.gnome.org/sources/gnome-panel/3.36/gnome-panel-3.36.2.tar.xz
Summary  : libgnome-panel
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: gnome-panel-bin = %{version}-%{release}
Requires: gnome-panel-data = %{version}-%{release}
Requires: gnome-panel-lib = %{version}-%{release}
Requires: gnome-panel-license = %{version}-%{release}
Requires: gnome-panel-locales = %{version}-%{release}
Requires: gnome-panel-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(cairo-xlib)
BuildRequires : pkgconfig(dconf)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gdm)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gweather-3.0)
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

%description


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
%setup -q -n gnome-panel-3.36.2
cd %{_builddir}/gnome-panel-3.36.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600285835
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1600285835
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-panel
cp %{_builddir}/gnome-panel-3.36.2/COPYING %{buildroot}/usr/share/package-licenses/gnome-panel/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/gnome-panel-3.36.2/COPYING-DOCS %{buildroot}/usr/share/package-licenses/gnome-panel/4f485ab7059ac53d9e3818278ad82217ce976a36
cp %{_builddir}/gnome-panel-3.36.2/COPYING.LESSER %{buildroot}/usr/share/package-licenses/gnome-panel/3704f4680301a60004b20f94e0b5b8c7ff1484a9
cp %{_builddir}/gnome-panel-3.36.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/gnome-panel/ba8966e2473a9969bdcab3dc82274c817cfd98a1
%make_install
%find_lang gnome-panel

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-panel

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-panel.desktop
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.clock.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.fish.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.initial-settings.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.menu-button.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.window-list.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.applet.workspace-switcher.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-panel.launcher.gschema.xml
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
/usr/include/gnome-panel/libgnome-panel/gp-module.h
/usr/include/gnome-panel/libgnome-panel/gp-utils.h
/usr/include/gnome-panel/libpanel-applet/panel-applet-enums.h
/usr/include/gnome-panel/libpanel-applet/panel-applet.h
/usr/lib64/libgnome-panel.so
/usr/lib64/libpanel-applet.so
/usr/lib64/pkgconfig/libgnome-panel.pc
/usr/lib64/pkgconfig/libpanel-applet.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libgnome-panel/GpApplet.html
/usr/share/gtk-doc/html/libgnome-panel/annotation-glossary.html
/usr/share/gtk-doc/html/libgnome-panel/api-index-full.html
/usr/share/gtk-doc/html/libgnome-panel/ch01.html
/usr/share/gtk-doc/html/libgnome-panel/home.png
/usr/share/gtk-doc/html/libgnome-panel/index.html
/usr/share/gtk-doc/html/libgnome-panel/left-insensitive.png
/usr/share/gtk-doc/html/libgnome-panel/left.png
/usr/share/gtk-doc/html/libgnome-panel/libgnome-panel-GpAppletInfo.html
/usr/share/gtk-doc/html/libgnome-panel/libgnome-panel-Module.html
/usr/share/gtk-doc/html/libgnome-panel/libgnome-panel.devhelp2
/usr/share/gtk-doc/html/libgnome-panel/object-tree.html
/usr/share/gtk-doc/html/libgnome-panel/right-insensitive.png
/usr/share/gtk-doc/html/libgnome-panel/right.png
/usr/share/gtk-doc/html/libgnome-panel/style.css
/usr/share/gtk-doc/html/libgnome-panel/up-insensitive.png
/usr/share/gtk-doc/html/libgnome-panel/up.png
/usr/share/gtk-doc/html/libpanel-applet/add_to_panel.png
/usr/share/gtk-doc/html/libpanel-applet/annotation-glossary.html
/usr/share/gtk-doc/html/libpanel-applet/api-index-full.html
/usr/share/gtk-doc/html/libpanel-applet/ch10.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.concepts.applet-instances.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.concepts.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.context-menu.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.context-menu.setup.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.example.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.in-out-process.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.install.build-system.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.install.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.integration.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.intro.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.introspection.html
/usr/share/gtk-doc/html/libpanel-applet/getting-started.settings.html
/usr/share/gtk-doc/html/libpanel-applet/home.png
/usr/share/gtk-doc/html/libpanel-applet/index.html
/usr/share/gtk-doc/html/libpanel-applet/left-insensitive.png
/usr/share/gtk-doc/html/libpanel-applet/left.png
/usr/share/gtk-doc/html/libpanel-applet/libpanel-applet-Panel-Applet-Factory.html
/usr/share/gtk-doc/html/libpanel-applet/libpanel-applet-Panel-Applet.html
/usr/share/gtk-doc/html/libpanel-applet/libpanel-applet.devhelp2
/usr/share/gtk-doc/html/libpanel-applet/object-tree.html
/usr/share/gtk-doc/html/libpanel-applet/overview.html
/usr/share/gtk-doc/html/libpanel-applet/port-gnome2.dbus.html
/usr/share/gtk-doc/html/libpanel-applet/port-gnome2.dbus.migrate-menus-to-gaction.html
/usr/share/gtk-doc/html/libpanel-applet/port-gnome2.dbus.remove-libbonobo-factory.html
/usr/share/gtk-doc/html/libpanel-applet/port-gnome2.html
/usr/share/gtk-doc/html/libpanel-applet/reference.html
/usr/share/gtk-doc/html/libpanel-applet/right-insensitive.png
/usr/share/gtk-doc/html/libpanel-applet/right.png
/usr/share/gtk-doc/html/libpanel-applet/style.css
/usr/share/gtk-doc/html/libpanel-applet/up-insensitive.png
/usr/share/gtk-doc/html/libpanel-applet/up.png
/usr/share/help/C/clock/index.docbook
/usr/share/help/C/clock/legal.xml
/usr/share/help/C/fish/index.docbook
/usr/share/help/C/fish/legal.xml
/usr/share/help/ar/clock/index.docbook
/usr/share/help/ar/clock/legal.xml
/usr/share/help/ca/clock/index.docbook
/usr/share/help/ca/clock/legal.xml
/usr/share/help/ca/fish/index.docbook
/usr/share/help/ca/fish/legal.xml
/usr/share/help/cs/clock/index.docbook
/usr/share/help/cs/clock/legal.xml
/usr/share/help/cs/fish/index.docbook
/usr/share/help/cs/fish/legal.xml
/usr/share/help/da/clock/index.docbook
/usr/share/help/da/clock/legal.xml
/usr/share/help/da/fish/index.docbook
/usr/share/help/da/fish/legal.xml
/usr/share/help/de/clock/index.docbook
/usr/share/help/de/clock/legal.xml
/usr/share/help/de/fish/index.docbook
/usr/share/help/de/fish/legal.xml
/usr/share/help/el/clock/index.docbook
/usr/share/help/el/clock/legal.xml
/usr/share/help/el/fish/index.docbook
/usr/share/help/el/fish/legal.xml
/usr/share/help/en_GB/clock/index.docbook
/usr/share/help/en_GB/clock/legal.xml
/usr/share/help/en_GB/fish/index.docbook
/usr/share/help/en_GB/fish/legal.xml
/usr/share/help/es/clock/index.docbook
/usr/share/help/es/clock/legal.xml
/usr/share/help/es/fish/index.docbook
/usr/share/help/es/fish/legal.xml
/usr/share/help/eu/clock/index.docbook
/usr/share/help/eu/clock/legal.xml
/usr/share/help/eu/fish/index.docbook
/usr/share/help/eu/fish/legal.xml
/usr/share/help/fi/clock/index.docbook
/usr/share/help/fi/clock/legal.xml
/usr/share/help/fi/fish/index.docbook
/usr/share/help/fi/fish/legal.xml
/usr/share/help/fr/clock/index.docbook
/usr/share/help/fr/clock/legal.xml
/usr/share/help/fr/fish/index.docbook
/usr/share/help/fr/fish/legal.xml
/usr/share/help/hu/clock/index.docbook
/usr/share/help/hu/clock/legal.xml
/usr/share/help/hu/fish/index.docbook
/usr/share/help/hu/fish/legal.xml
/usr/share/help/id/clock/index.docbook
/usr/share/help/id/clock/legal.xml
/usr/share/help/it/clock/index.docbook
/usr/share/help/it/clock/legal.xml
/usr/share/help/it/fish/index.docbook
/usr/share/help/it/fish/legal.xml
/usr/share/help/ja/clock/index.docbook
/usr/share/help/ja/clock/legal.xml
/usr/share/help/ja/fish/index.docbook
/usr/share/help/ja/fish/legal.xml
/usr/share/help/ko/clock/index.docbook
/usr/share/help/ko/clock/legal.xml
/usr/share/help/ko/fish/index.docbook
/usr/share/help/ko/fish/legal.xml
/usr/share/help/nl/clock/index.docbook
/usr/share/help/nl/clock/legal.xml
/usr/share/help/oc/clock/index.docbook
/usr/share/help/oc/clock/legal.xml
/usr/share/help/oc/fish/index.docbook
/usr/share/help/oc/fish/legal.xml
/usr/share/help/pa/clock/index.docbook
/usr/share/help/pa/clock/legal.xml
/usr/share/help/pt/clock/index.docbook
/usr/share/help/pt/clock/legal.xml
/usr/share/help/pt_BR/clock/index.docbook
/usr/share/help/pt_BR/clock/legal.xml
/usr/share/help/pt_BR/fish/index.docbook
/usr/share/help/pt_BR/fish/legal.xml
/usr/share/help/ru/clock/index.docbook
/usr/share/help/ru/clock/legal.xml
/usr/share/help/ru/fish/index.docbook
/usr/share/help/ru/fish/legal.xml
/usr/share/help/sl/clock/index.docbook
/usr/share/help/sl/clock/legal.xml
/usr/share/help/sl/fish/index.docbook
/usr/share/help/sl/fish/legal.xml
/usr/share/help/sr/clock/index.docbook
/usr/share/help/sr/clock/legal.xml
/usr/share/help/sv/clock/index.docbook
/usr/share/help/sv/clock/legal.xml
/usr/share/help/sv/fish/index.docbook
/usr/share/help/sv/fish/legal.xml
/usr/share/help/te/clock/index.docbook
/usr/share/help/te/clock/legal.xml
/usr/share/help/th/clock/index.docbook
/usr/share/help/th/clock/legal.xml
/usr/share/help/th/fish/index.docbook
/usr/share/help/th/fish/legal.xml
/usr/share/help/uk/clock/index.docbook
/usr/share/help/uk/clock/legal.xml
/usr/share/help/uk/fish/index.docbook
/usr/share/help/uk/fish/legal.xml
/usr/share/help/zh_CN/clock/index.docbook
/usr/share/help/zh_CN/clock/legal.xml
/usr/share/help/zh_CN/fish/index.docbook
/usr/share/help/zh_CN/fish/legal.xml
/usr/share/help/zh_HK/clock/index.docbook
/usr/share/help/zh_HK/clock/legal.xml
/usr/share/help/zh_TW/clock/index.docbook
/usr/share/help/zh_TW/clock/legal.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-panel/modules/clock.so
/usr/lib64/gnome-panel/modules/fish.so
/usr/lib64/gnome-panel/modules/menu.so
/usr/lib64/gnome-panel/modules/notification-area.so
/usr/lib64/gnome-panel/modules/separator.so
/usr/lib64/gnome-panel/modules/status-notifier.so
/usr/lib64/gnome-panel/modules/wncklet.so
/usr/lib64/libgnome-panel.so.0
/usr/lib64/libgnome-panel.so.0.0.0
/usr/lib64/libpanel-applet.so.3
/usr/lib64/libpanel-applet.so.3.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-panel/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/gnome-panel/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/gnome-panel/4f485ab7059ac53d9e3818278ad82217ce976a36
/usr/share/package-licenses/gnome-panel/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-panel.1

%files locales -f gnome-panel.lang
%defattr(-,root,root,-)

