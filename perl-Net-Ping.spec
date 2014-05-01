%define	modname	Net-Ping
%define	modver	2.41

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	2

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	TCP, UDP, or ICMP ping
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Net/%{modname}-%{modver}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(JSON::PP) >=  %{perl_convert_version 2.27103}
BuildRequires:	perl(Socket)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::HiRes)
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
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
