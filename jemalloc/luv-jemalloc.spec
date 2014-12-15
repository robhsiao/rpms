Name:		luv-jemalloc
Version:	3.6.0
Release:	1%{?dist}
Summary:	General-purpose scalable concurrent malloc implementation

Group:		System Environment/Libraries
License:	BSD
URL:		http://www.canonware.com/jemalloc/
Source0:	http://www.canonware.com/download/jemalloc/jemalloc-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
jemalloc is a general purpose malloc(3) implementation that emphasizes fragmentation avoidance and scalable concurrency support.


%prep
%setup -q -n jemalloc-%{version}

%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/jemalloc.sh
%{_bindir}/pprof
%{_includedir}/jemalloc/
%{_libdir}/libjemalloc*
%{_docdir}/jemalloc/jemalloc.html
%{_mandir}/man3/jemalloc.3.gz



%changelog

