
Name:           dbus-glib
Version:        0.100.2
Release:        0
License:        AFL-2.1 or GPL-2.0+
Summary:        GLib bindings for D-Bus
Url:            http://www.freedesktop.org/software/dbus/
Group:          System/Libraries
Source0:        http://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-%{version}.tar.gz
Source1001: 	dbus-glib.manifest
BuildRequires:  autoconf
BuildRequires:  expat-devel
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)

%description
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package devel
Summary:        Libraries and headers for the D-Bus GLib bindings
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
Headers and static libraries for the D-Bus GLib bindings

%prep
%setup -q
cp %{SOURCE1001} .

%build

%configure --disable-tests \
    --enable-verbose-mode=yes \
    --enable-asserts=yes \
    --disable-gtk-doc

make %{?_smp_mflags}

%install
%make_install

# don't care about bash completion in a consumer device
rm -rf %{buildroot}%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
rm -rf %{buildroot}%{_prefix}/libexec/dbus-bash-completion-helper

%docs_package

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license COPYING
%{_libdir}/*glib*.so.*

%files devel
%manifest %{name}.manifest
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/dbus-glib-1.pc
%{_includedir}/dbus-1.0/dbus/*
%{_bindir}/dbus-binding-tool

