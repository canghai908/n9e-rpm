Name:		n9e
Version:	1.2.0
Release: 	g59f2bb0%{?alphatag:.%{alphatag}}%{?dist}
Summary:	A Distributed and High-Performance Monitoring System
Group:		Applications/Internet
License:	Apache-2.0
URL:		https://n9e.didiyun.com/
Source0:	n9e-%{version}%{?alphatag:%{alphatag}}.tar.gz
Source1:	n9e-collector.init
Source2:	n9e-judge.init
Source3:	n9e-index.init
Source4:	n9e-monapi.init
Source5:	n9e-transfer.init
Source6:	n9e-tsdb.init
Source7:	n9e-collector.service
Source8:	n9e-judge.service
Source9:	n9e-index.service
Source10:	n9e-monapi.service
Source11:	n9e-transfer.service
Source12:	n9e-tsdb.service

Buildroot:	%{_tmppath}/n9e-%{version}-%{release}-root-%(%{__id_u} -n)


%if 0%{?rhel} >= 7
BuildRequires:	systemd
%endif

%description
Nightingale is a distributed and high-performance monitoring system

%package collector
Summary:			Nightingale collector
Group:				Applications/Internet
Requires(pre):		/usr/sbin/useradd
%if 0%{?rhel} >= 7
Requires:			net-tools
Requires(post):		systemd
Requires(preun):	systemd
Requires(preun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Obsoletes:			Nightingale

%description collector
Nightingale collector.

%package index
Summary:			Nightingale index
Group:				Applications/Internet
Requires(pre):		/usr/sbin/useradd
%if 0%{?rhel} >= 7
Requires:			net-tools
Requires(post):		systemd
Requires(preun):	systemd
Requires(preun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Obsoletes:			Nightingale

%description index
Nightingale index.

%package judge
Summary:			Nightingale judge
Group:				Applications/Internet
Requires(pre):		/usr/sbin/useradd
%if 0%{?rhel} >= 7
Requires:			net-tools
Requires(post):		systemd
Requires(preun):	systemd
Requires(preun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Obsoletes:			Nightingale

%description judge
Nightingale judge.

%package monapi
Summary:			Nightingale monapi
Group:				Applications/Internet
Requires(pre):		/usr/sbin/useradd
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	systemd
Requires(preun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Obsoletes:			Nightingale

%description monapi
Nightingale monapi.



%package transfer
Summary:			Nightingale transfer
Group:				Applications/Internet
Requires(pre):		/usr/sbin/useradd
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	systemd
Requires(preun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Obsoletes:			Nightingale

%description transfer
Nightingale transfer.


%package tsdb
Summary:			Nightingale tsdb
Group:				Applications/Internet
Requires(pre):		/usr/sbin/useradd
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	systemd
Requires(preun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Obsoletes:			Nightingale

%description tsdb
Nightingale tsdb.

%package sql
Summary:			Nightingale sql
Group:				Applications/Internet

%description sql
Nightingale sql files

%package nginx-conf
Summary:			Nightingale sql
Group:				Applications/Internet

%description nginx-conf
Nightingale nginx-conf files

%package web
Summary:			Nightingale sql
Group:				Applications/Internet

%description web
Nightingale web files

%global debug_package %{nil}

%prep
%setup0 -q -n n9e-%{version}%{?alphatag:%{alphatag}}

%build

%install

rm -rf $RPM_BUILD_ROOT

# install necessary directories
mkdir -p $RPM_BUILD_ROOT%{_prefix}/local/n9e
mkdir -p $RPM_BUILD_ROOT%{_prefix}/local/n9e/etc
mkdir -p $RPM_BUILD_ROOT%{_prefix}/local/n9e/sql
mkdir -p $RPM_BUILD_ROOT%{_prefix}/local/n9e/pub/static
mkdir -p $RPM_BUILD_ROOT%{_prefix}/local/n9e/plugin

# install  binaries
install -m 0755 -p n9e-collector $RPM_BUILD_ROOT%{_prefix}/local/n9e/
install -m 0755 -p n9e-index $RPM_BUILD_ROOT%{_prefix}/local/n9e/
install -m 0755 -p n9e-judge $RPM_BUILD_ROOT%{_prefix}/local/n9e/
install -m 0755 -p n9e-monapi $RPM_BUILD_ROOT%{_prefix}/local/n9e/
install -m 0755 -p n9e-transfer $RPM_BUILD_ROOT%{_prefix}/local/n9e/
install -m 0755 -p n9e-tsdb $RPM_BUILD_ROOT%{_prefix}/local/n9e/
install -m 0755 -p control $RPM_BUILD_ROOT%{_prefix}/local/n9e/

# install  conf
install -m 0755 -p etc/address.yml $RPM_BUILD_ROOT%{_prefix}/local/n9e/etc/
install -m 0755 -p etc/collector.yml $RPM_BUILD_ROOT%{_prefix}/local/n9e/etc/
install -m 0755 -p etc/index.yml $RPM_BUILD_ROOT%{_prefix}/local/n9e/etc/
install -m 0755 -p etc/judge.yml $RPM_BUILD_ROOT%{_prefix}/local/n9e/etc/
install -m 0755 -p etc/monapi.yml $RPM_BUILD_ROOT%{_prefix}/local/n9e/etc/
install -m 0755 -p etc/mysql.yml $RPM_BUILD_ROOT%{_prefix}/local/n9e/etc/
install -m 0755 -p etc/transfer.yml $RPM_BUILD_ROOT%{_prefix}/local/n9e/etc/
install -m 0755 -p etc/tsdb.yml $RPM_BUILD_ROOT%{_prefix}/local/n9e/etc/
install -m 0755 -p etc/nginx.conf $RPM_BUILD_ROOT%{_prefix}/local/n9e/etc/

# install  plugin
cp -a plugin/* $RPM_BUILD_ROOT%{_prefix}/local/n9e/plugin/

# install  sql
cp -a sql/* $RPM_BUILD_ROOT%{_prefix}/local/n9e/sql/

# install  web
cp -a pub/* $RPM_BUILD_ROOT%{_prefix}/local/n9e/pub/

# install startup scripts
%if 0%{?rhel} >= 7
install -Dm 0644 -p %{SOURCE7} $RPM_BUILD_ROOT%{_unitdir}/n9e-collector.service
install -Dm 0644 -p %{SOURCE8} $RPM_BUILD_ROOT%{_unitdir}/n9e-judge.service
install -Dm 0644 -p %{SOURCE9} $RPM_BUILD_ROOT%{_unitdir}/n9e-index.service
install -Dm 0644 -p %{SOURCE10} $RPM_BUILD_ROOT%{_unitdir}/n9e-monapi.service
install -Dm 0644 -p %{SOURCE11} $RPM_BUILD_ROOT%{_unitdir}/n9e-transfer.service
install -Dm 0644 -p %{SOURCE12} $RPM_BUILD_ROOT%{_unitdir}/n9e-tsdb.service
%else
install -Dm 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/n9e-collector
install -Dm 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/n9e-judge
install -Dm 0644 -p %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/n9e-index
install -Dm 0644 -p %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/n9e-monapi
install -Dm 0644 -p %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/n9e-transfer
install -Dm 0644 -p %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/n9e-tsdb
%endif

exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%pre collector
getent group n9e > /dev/null || groupadd -r n9e
getent passwd n9e > /dev/null || \
	useradd -r -g n9e -d %{_localstatedir}/lib/n9e -s /sbin/nologin \
	-c "n9e Monitoring System" n9e
:

%pre index
getent group n9e > /dev/null || groupadd -r n9e
getent passwd n9e > /dev/null || \
	useradd -r -g n9e -d %{_localstatedir}/lib/n9e -s /sbin/nologin \
	-c "n9e Monitoring System" n9e
:

%pre judge
getent group n9e > /dev/null || groupadd -r n9e
getent passwd n9e > /dev/null || \
	useradd -r -g n9e -d %{_localstatedir}/lib/n9e -s /sbin/nologin \
	-c "n9e Monitoring System" n9e
:

%pre monapi
getent group n9e > /dev/null || groupadd -r n9e
getent passwd n9e > /dev/null || \
	useradd -r -g n9e -d %{_localstatedir}/lib/n9e -s /sbin/nologin \
	-c "n9e Monitoring System" n9e
:

%pre transfer
getent group n9e > /dev/null || groupadd -r n9e
getent passwd n9e > /dev/null || \
	useradd -r -g n9e -d %{_localstatedir}/lib/n9e -s /sbin/nologin \
	-c "n9e Monitoring System" n9e
:

%pre tsdb
getent group n9e > /dev/null || groupadd -r n9e
getent passwd n9e > /dev/null || \
	useradd -r -g n9e -d %{_localstatedir}/lib/n9e -s /sbin/nologin \
	-c "n9e Monitoring System" n9e
:

%define __debug_install_post   \
   %{_rpmconfigdir}/find-debuginfo.sh %{?_find_debuginfo_opts} "%{_builddir}/%{?buildsubdir}"\
%{nil}

%files collector
%defattr(-,root,root,-)
%config(noreplace) %{_prefix}/local/n9e/etc/collector.yml
%config(noreplace) %{_prefix}/local/n9e/etc/address.yml
%dir %{_prefix}/local/n9e/etc
%dir %{_prefix}/local/n9e/plugin
%{_prefix}/local/n9e/plugin/60_plugin_status.py
%{_prefix}/local/n9e/plugin/60_uptime.sh
%attr(0755,n9e,n9e) %dir %{_prefix}/local/n9e
%{_prefix}/local/n9e/control
%{_prefix}/local/n9e/n9e-collector
%if 0%{?rhel} >= 7
%{_unitdir}/n9e-collector.service
%else
%{_sysconfdir}/init.d/n9e-collector
%endif

%files index
%defattr(-,root,root,-)
%config(noreplace) %{_prefix}/local/n9e/etc/index.yml
%config(noreplace) %{_prefix}/local/n9e/etc/mysql.yml
%dir %{_prefix}/local/n9e/etc
%attr(0755,n9e,n9e) %dir %{_prefix}/local/n9e
%{_prefix}/local/n9e/control
%{_prefix}/local/n9e/n9e-index
%if 0%{?rhel} >= 7
%{_unitdir}/n9e-index.service
%else
%{_sysconfdir}/init.d/n9e-index
%endif

%files judge
%defattr(-,root,root,-)
%config(noreplace) %{_prefix}/local/n9e/etc/judge.yml
%config(noreplace) %{_prefix}/local/n9e/etc/mysql.yml
%config(noreplace) %{_prefix}/local/n9e/etc/address.yml
%dir %{_prefix}/local/n9e/etc
%attr(0755,n9e,n9e) %dir %{_prefix}/local/n9e
%{_prefix}/local/n9e/control
%{_prefix}/local/n9e/n9e-judge
%if 0%{?rhel} >= 7
%{_unitdir}/n9e-judge.service
%else
%{_sysconfdir}/init.d/n9e-judge
%endif

%files monapi
%defattr(-,root,root,-)
%config(noreplace) %{_prefix}/local/n9e/etc/monapi.yml
%config(noreplace) %{_prefix}/local/n9e/etc/mysql.yml
%config(noreplace) %{_prefix}/local/n9e/etc/address.yml
%dir %{_prefix}/local/n9e/etc
%attr(0755,n9e,n9e) %dir %{_prefix}/local/n9e
%{_prefix}/local/n9e/control
%{_prefix}/local/n9e/n9e-monapi
%if 0%{?rhel} >= 7
%{_unitdir}/n9e-monapi.service
%else
%{_sysconfdir}/init.d/n9e-monapi
%endif

%files transfer
%defattr(-,root,root,-)
%config(noreplace) %{_prefix}/local/n9e/etc/transfer.yml
%config(noreplace) %{_prefix}/local/n9e/etc/mysql.yml
%config(noreplace) %{_prefix}/local/n9e/etc/address.yml
%dir %{_prefix}/local/n9e/etc
%attr(0755,n9e,n9e) %dir %{_prefix}/local/n9e
%{_prefix}/local/n9e/control
%{_prefix}/local/n9e/n9e-transfer
%if 0%{?rhel} >= 7
%{_unitdir}/n9e-transfer.service
%else
%{_sysconfdir}/init.d/n9e-transfer
%endif

%files tsdb
%defattr(-,root,root,-)
%config(noreplace) %{_prefix}/local/n9e/etc/tsdb.yml
%config(noreplace) %{_prefix}/local/n9e/etc/mysql.yml
%config(noreplace) %{_prefix}/local/n9e/etc/address.yml
%dir %{_prefix}/local/n9e/etc
%attr(0755,n9e,n9e) %dir %{_prefix}/local/n9e
%{_prefix}/local/n9e/control
%{_prefix}/local/n9e/n9e-tsdb
%if 0%{?rhel} >= 7
%{_unitdir}/n9e-tsdb.service
%else
%{_sysconfdir}/init.d/n9e-tsdb
%endif

%files sql
%defattr(-,root,root,-)
%attr(0755,n9e,n9e) %dir %{_prefix}/local/n9e
%{_prefix}/local/n9e/sql/

%files nginx-conf
%defattr(-,root,root,-)
%dir %{_prefix}/local/n9e/etc
%attr(0755,n9e,n9e) %dir %{_prefix}/local/n9e
%{_prefix}/local/n9e/etc/nginx.conf

%files web
%defattr(-,root,root,-)
%attr(0755,n9e,n9e) %dir %{_prefix}/local/n9e
%{_prefix}/local/n9e/pub