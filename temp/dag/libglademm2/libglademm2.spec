# Authority: freshrpms
%define rname libglademm

Summary: C++ wrappers for libglade, for use with gtkmm.
Name: libglademm2
Version: 2.0.1
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.sourceforge.net/pub/sourceforge/gtkmm/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtkmm2-devel >= 2.0, libsigc++ >= 1.2, glib2-devel >= 2.0
BuildRequires: pango-devel >= 1.0, freetype-devel >= 2.0
BuildRequires: atk-devel >= 1.0, libglade2 >= 2.0, libxml2 >= 2.0

%description
libglademm provides C++ wrappers for libglade, for use with gtkmm.

%package devel
Summary: Headers for developing programs that will use %{rname}.
Group: Development/Libraries

%description devel
This package contains the static libraries and header files needed for
developing gtkmm applications.

%prep
%setup -n %{rname}-%{version}

%build
%configure \
	--enable-static \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libglademm-2.0/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/libglademm-2.0/
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%changelog
* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Initial package. (using DAR)
