Summary: A fast compressor/decompressor
Name: snappy
Version: 1.1.6
Release: 1%{?dist}
License: BSD-type license
Group: Libraries/Databases
URL: https://github.com/google/snappy

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
#Requires: pango

%description
Snappy, a fast compressor/decompressor.

Categories:
  - Library

%package devel
Summary: snappy development headers and static library
Group: Development/Libraries
#Requires: %{name} = %{version}

%description devel
Snappy, a fast compressor/decompressor. This
package provides libraries and headers for development

%prep
%setup -q -n %{name}-%{version}/snappy
patch -p0 < ../readme.patch

%build
%{__make} clean || true

./autogen.sh

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%configure 

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n snappy -p /sbin/ldconfig

%postun -n snappy -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%exclude %{_defaultdocdir}/snappy
%{_libdir}/libsnappy*.so*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/snappy*.h
%{_libdir}/libsnappy.a
%{_libdir}/pkgconfig/snappy.pc
%exclude %{_libdir}/libsnappy.la

%changelog
* Wed Jan 18 2017 rinigus <rinigus.git@gmail.com> - 1.1.3-1
- initial packaging release for SFOS
