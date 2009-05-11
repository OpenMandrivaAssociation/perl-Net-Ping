
%define realname   Net-Ping
%define version    2.35
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    TCP, UDP, or ICMP ping
Source:     http://www.cpan.org/modules/by-module/Net/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Test)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


