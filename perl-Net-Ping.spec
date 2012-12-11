%define upstream_name    Net-Ping
%define upstream_version 2.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	TCP, UDP, or ICMP ping
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test)
BuildArch:	noarch

%description
This module contains methods to test the reachability of remote hosts on a
network. A ping object is first created with optional parameters, a
variable number of hosts may be pinged multiple times and then the
connection is closed.

You may choose one of six different protocols to use for the ping. The
"tcp" protocol is the default. Note that a live remote host may still fail
to be pingable by one or more of these protocols. For example,
www.microsoft.com is generally alive but not "icmp" pingable.

With the "tcp" protocol the ping() method attempts to establish a
connection to the remote host's echo port. If the connection is
successfully established, the remote host is considered reachable. No data
is actually echoed. This protocol does not require any special privileges
but has higher overhead than the "udp" and "icmp" protocols.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 2.360.0-4mdv2011.0
+ Revision: 658540
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.360.0-3mdv2011.0
+ Revision: 551999
- rebuild

* Wed Jun 17 2009 Jérôme Quelin <jquelin@mandriva.org> 2.360.0-2mdv2010.0
+ Revision: 386750
- using %%perl_convert_version
- fix license

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.36-1mdv2010.0
+ Revision: 384245
- update to new version 2.36

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 2.35-1mdv2010.0
+ Revision: 374546
- import perl-Net-Ping


* Mon May 11 2009 cpan2dist 2.35-1mdv
- initial mdv release, generated with cpan2dist

