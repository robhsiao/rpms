Name:		luv-tengine
Version:	2.0.3
Release:	1%{?dist}
Summary:	A distribution of Nginx with some advanced features.

Group:		System Environment/Daemons
License:	BSD
URL:		http://tengine.taobao.org/
Source0:	http://tengine.taobao.org/download/tengine-%{version}.tar.gz
Source1:    init.d
Source2:    logrotate.d
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc,pcre-devel,zlib-devel,openssl-devel,GeoIP-devel,jemalloc-devel,luv-luajit
Requires:	luv-luajit, jemalloc, logrotate

%description


%prep
%setup -q -n tengine-%{version}


%build
./configure \
        --prefix=/var/www \
        --includedir=/usr/include/nginx \
        --sbin-path=/usr/sbin/nginx \
        --dso-tool-path=/usr/sbin/dso_tool \
        --conf-path=/etc/nginx/nginx.conf \
        --pid-path=/var/run/nginx.pid \
        --lock-path=/var/lock/subsys/nginx.lock \
        --http-log-path=/var/log/nginx/access.log \
        --error-log-path=/var/log/nginx/error.log \
        --user=luv \
        --group=luv \
        --dso-path=/var/lib/nginx/modules \
        --http-client-body-temp-path=%{_tmppath}/nginx/client_body/ \
        --http-proxy-temp-path=%{_tmppath}/nginx/proxy/ \
        --http-fastcgi-temp-path=%{_tmppath}/nginx/fastcgi/ \
        --http-uwsgi-temp-path=%{_tmppath}/nginx/uwsgi \
        --http-scgi-temp-path=%{_tmppath}/nginx/scgi \
        --with-http_ssl_module \
        --with-http_realip_module \
        --with-http_geoip_module \
        --with-http_sub_module \
        --with-http_gzip_static_module \
        --with-http_stub_status_module \
        --without-mail_pop3_module \
        --without-mail_imap_module \
        --without-mail_smtp_module \
        --without-http_empty_gif_module\
        \
        --with-jemalloc \
        --with-http_lua_module \
        --with-luajit-inc=%{_includedir}/luajit-2.0/ \
        --with-luajit-lib=%{_libdir}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%{__mkdir_p} %{buildroot}/etc/init.d/
%{__install} -m 0755 %{SOURCE1} %{buildroot}/etc/init.d/nginx

%{__mkdir_p} %{buildroot}/etc/logrotate.d/
%{__install} -m 0644 %{SOURCE2} %{buildroot}/etc/logrotate.d/nginx

%{__install} -d %{buildroot}/etc/nginx/vhosts/
%{__install} -d %{buildroot}/var/log/nginx/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/sbin/nginx
/usr/sbin/dso_tool
%config(noreplace) /etc/nginx/
/etc/init.d/nginx
/etc/logrotate.d/nginx
%{_includedir}/nginx/
/var/www/html/
/var/log/nginx/
/var/lib/nginx/modules/

%pre
id luv >& /dev/null
if [ $? -gt 0 ]; then
    useradd luv
fi

%post
# http://www.ibm.com/developerworks/library/l-rpm2/
if [ "$1" = "1" ]; then
    install -d /var/tmp/nginx/
    install -d /var/tmp/nginx/client_body/
    install -d /var/tmp/nginx/proxy/
    install -d /var/tmp/nginx/fastcgi/
    install -d /var/tmp/nginx/uwsgi/
    install -d /var/tmp/nginx/scgi/

    test -x /etc/init.d/nginx && /etc/init.d/nginx start
else
    test -x /etc/init.d/nginx && /etc/init.d/nginx reload
fi
true

%preun
if [ "$1" = "0" ]; then
    test -x /etc/init.d/nginx && /etc/init.d/nginx stop
    rm -rf /var/tmp/nginx
fi
true

%changelog

