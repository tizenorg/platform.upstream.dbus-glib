Name:       dbus-glib
Summary:    GLib bindings for D-Bus
Version:    0.100
Release:    1
Group:      System/Libraries
License:    AFL/GPL
URL:        http://www.freedesktop.org/software/dbus/
Source0:    http://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-%{version}.tar.gz
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libtool
BuildRequires:  expat-devel
BuildRequires:  gettext-tools
BuildRequires:  autoconf

%description
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package devel
Summary:    Libraries and headers for the D-Bus GLib bindings
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Headers and static libraries for the D-Bus GLib bindings

%prep
%setup -q 

%build

%configure --disable-tests \
    --enable-verbose-mode=yes \
    --enable-asserts=yes \
    --disable-gtk-doc

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

# don't care about bash completion in a consumer device
rm -rf $RPM_BUILD_ROOT/etc/bash_completion.d/dbus-bash-completion.sh
rm -rf $RPM_BUILD_ROOT/usr/libexec/dbus-bash-completion-helper

%doc_package

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/*glib*.so.*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/dbus-glib-1.pc
%{_includedir}/dbus-1.0/dbus/*
%{_bindir}/dbus-binding-tool

