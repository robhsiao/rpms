Name:		luv-luajit
Version:	2.0.3
Release:	1%{?dist}
Summary:	a Just-In-Time Compiler for Lua
Group:		Development/Language

License:	MIT
URL:		http://luajit.org/
Source0:	http://luajit.org/download/LuaJIT-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc

%description
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language. Lua is a powerful, dynamic and light-weight programming language. It may be embedded or used as a general-purpose, stand-alone language.


%prep
# http://www.rpm.org/max-rpm/s1-rpm-inside-macros.html
%setup -q -n LuaJIT-%{version}


%build
make PREFIX=%{_prefix}

%install
rm -rf %{buildroot}
make install PREFIX=%{_prefix} DESTDIR=%{buildroot} INSTALL_LIB=%{buildroot}%{_libdir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/luajit
%{_bindir}/luajit-%{version}
%{_mandir}/man1/luajit.1.gz

%{_includedir}/luajit-*/
%{_libdir}/libluajit-*
%{_datadir}/luajit-*
%{_libdir}/pkgconfig/luajit.pc

%changelog

